import argparse
import logging
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def load_env(path=Path(".env")):
    env = {}
    if path.is_file():
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def setting(env, key, default=None):
    return os.environ.get(key, env.get(key, default))


def find_ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return shutil.which("ffmpeg")


def run_ffmpeg(ffmpeg, args):
    result = subprocess.run(
        [ffmpeg, "-y", "-loglevel", "error", *args],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"ffmpeg exited with code {result.returncode}")


def convert_mp4_to_gif(ffmpeg, input_path, output_path, fps, width):
    filters = [f"fps={fps}"]
    if width:
        filters.append(f"scale={width}:-1:flags=lanczos")
    filter_chain = ",".join(filters)

    with tempfile.TemporaryDirectory() as tmp:
        palette = str(Path(tmp) / "palette.png")
        run_ffmpeg(ffmpeg, [
            "-i", str(input_path),
            "-vf", f"{filter_chain},palettegen",
            palette
        ])
        run_ffmpeg(ffmpeg, [
            "-i", str(input_path),
            "-i", palette,
            "-filter_complex", f"{filter_chain}[x];[x][1:v]paletteuse",
            str(output_path)
        ])


def main():
    env = load_env()

    parser = argparse.ArgumentParser(
        description="Batch-convert the .mp4 files in a directory into palette-optimized .gif animations."
    )
    parser.add_argument("input_dir", nargs="?", default=setting(env, "INPUT_DIR", "input"),
                        help="directory containing .mp4 files (default: %(default)s)")
    parser.add_argument("output_dir", nargs="?", default=setting(env, "OUTPUT_DIR", "output"),
                        help="directory to write .gif files to, created if missing (default: %(default)s)")
    parser.add_argument("--fps", type=float, default=setting(env, "FPS", 12),
                        help="frame rate of the output GIFs (default: %(default)s)")
    parser.add_argument("--width", type=int, default=setting(env, "WIDTH") or None,
                        help="output width in pixels, height scales to match (default: source size)")
    parser.add_argument("--force", action="store_true",
                        default=str(setting(env, "FORCE", "")).strip().lower() in ("1", "true", "yes"),
                        help="re-convert files whose .gif already exists")
    parser.add_argument("--log-file",
                        default=setting(env, "LOG_FILE") or str(Path(__file__).with_name("conversion.log")),
                        help="file that collects the logs of every run (default: %(default)s)")
    args = parser.parse_args()

    if not args.input_dir or not args.output_dir:
        parser.error("input_dir and output_dir are required, either as arguments or as INPUT_DIR/OUTPUT_DIR in a .env file")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(args.log_file),
            logging.StreamHandler()
        ]
    )

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    logging.info(f"Run started: input={input_dir} output={output_dir} fps={args.fps} width={args.width or 'source'} force={args.force}")

    if not input_dir.is_dir():
        logging.error(f"Input directory does not exist: {input_dir}")
        return 1

    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        logging.error("ffmpeg not found: run `pip install -r requirements.txt` or install ffmpeg system-wide")
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    videos = sorted(p for p in input_dir.iterdir()
                    if p.is_file() and p.suffix.lower() == ".mp4")
    if not videos:
        logging.warning(f"No .mp4 files found in {input_dir}")
        return 0

    logging.info(f"Found {len(videos)} .mp4 file(s) in {input_dir}")

    converted = skipped = failed = 0
    for video in videos:
        output_path = output_dir / (video.stem + ".gif")

        if output_path.exists() and not args.force:
            logging.info(f"Skipping {video.name}: {output_path} already exists (use --force to overwrite)")
            skipped += 1
            continue

        try:
            logging.info(f"Processing file: {video}")
            convert_mp4_to_gif(ffmpeg, video, output_path, args.fps, args.width)
            logging.info(f"Successfully converted {video} to {output_path}")
            converted += 1
        except Exception as e:
            logging.error(f"Failed to convert {video} - Error: {e}")
            failed += 1

    logging.info(f"Done: {converted} converted, {skipped} skipped, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

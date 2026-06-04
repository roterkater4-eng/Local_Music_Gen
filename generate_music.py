from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from local_music_gen import create_random_melody


def main() -> None:
    output_file = Path("generated_music.mid")
    result = create_random_melody(output_file, bars=8, tempo_bpm=110)
    print(f"Generated MIDI file: {result.resolve()}")


if __name__ == "__main__":
    main()

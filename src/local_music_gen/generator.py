from pathlib import Path
from random import choice, randint
from mido import Message, MetaMessage, MidiFile, MidiTrack, bpm2tempo

MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]


def create_random_melody(
    output_path: str | Path = "generated_music.mid",
    bars: int = 8,
    tempo_bpm: int = 100,
    program: int = 0,
) -> Path:
    """Generate a simple random melody as a MIDI file."""
    output_path = Path(output_path)
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    track.append(Message("program_change", program=program, time=0))
    track.append(MetaMessage("set_tempo", tempo=bpm2tempo(tempo_bpm), time=0))

    base_note = choice([60, 62, 64, 65, 67])
    ticks_per_beat = midi.ticks_per_beat
    note_duration = ticks_per_beat

    for _ in range(bars * 4):
        scale_offset = choice(MAJOR_SCALE)
        note = base_note + scale_offset
        velocity = randint(64, 96)

        track.append(Message("note_on", note=note, velocity=velocity, time=0))
        track.append(Message("note_off", note=note, velocity=0, time=note_duration))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    midi.save(output_path)
    return output_path

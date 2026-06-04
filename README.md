# Local_Music_Gen

Ein einfacher lokaler Musikgenerator in Python. Das Projekt kann eine erste MIDI-Datei erstellen und dient als Basis für weitere Musik- oder KI-Features.

## Erste Schritte

1. Installiere die Abhängigkeiten:
   ```bash
   python -m pip install -r requirements.txt
   ```

2. Erzeuge eine MIDI-Datei:
   ```bash
   python generate_music.py
   ```

3. Öffne die erstellte Datei `generated_music.mid` in einem MIDI-Player oder DAW.

## Projektstruktur

- `generate_music.py`: Startskript zur MIDI-Erzeugung
- `src/local_music_gen/generator.py`: Melodie-Generator
- `requirements.txt`: Python-Abhängigkeiten

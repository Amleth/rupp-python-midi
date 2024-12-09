import csv
from mido import bpm2tempo, Message, MidiFile, MidiTrack, second2tick

bpm = 60

mid = MidiFile()
track_left = MidiTrack()
track_right = MidiTrack()
mid.tracks.append(track_left)
mid.tracks.append(track_right)


def convert_note_name_to_midi_value(x):
    x = x.strip()
    x = x.lower()

    notes = {
        "d": 2,
        "e": 4,
        "g": 7,
        "a": 9,
        "b": 11
    }
    note_name = x[0]
    return notes[note_name] + 12 * int(x[1:])


def process_track(f, t):
    with open(f, mode='r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            pitch = convert_note_name_to_midi_value(row[0])
            duration = float(row[1])
            duration = second2tick(duration, mid.ticks_per_beat, bpm2tempo(bpm))

            t.append(Message('note_on', note=pitch, velocity=64, time=0))
            t.append(Message('note_off', note=pitch, velocity=64, time=duration))


process_track('left.csv', track_left)
process_track('right.csv', track_right)

mid.save('file.mid')

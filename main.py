import csv
from mido import bpm2tempo, Message, MidiFile, MidiTrack, second2tick

bpm = 60

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        pitch = int(row[0])
        duration = float(row[1])
        duration = second2tick(duration, mid.ticks_per_beat, bpm2tempo(bpm))

        track.append(Message('note_on', note=pitch, velocity=64, time=0))
        track.append(Message('note_off', note=pitch, velocity=64, time=duration))

mid.save('file.mid')

import csv
from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        pitch = int(row[0])
        duration = int(row[1])
        track.append(Message('note_on', note=pitch, velocity=64, time=0))
        track.append(Message('note_off', note=pitch, velocity=64, time=duration * 480))

mid.save('file.mid')

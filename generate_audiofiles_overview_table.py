#!/usr/bin/python3
# coding: utf-8
import os
import librosa
import pandas as pd
import datetime


def get_audio_duration(filename):
    ''' Calculates the duration of an audio file in seconds'''
    # Load wav file:
    y, sr = librosa.load(filename)
    # Get duration:
    duration = librosa.get_duration(y=y, sr=sr)
    return duration, sr


if __name__ == "__main__":
    total_duration = 0
    num_of_files = 0
    df = pd.DataFrame(
        columns=["Filename", "Location", "Duration [s]", "Samplerate", "Hash"])

    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for filename in files:
            if filename.endswith(".wav"):
                num_of_files += 1
                duration, samplerate = get_audio_duration(
                    os.path.join(root, filename))

                total_duration += duration

                filehash = hash(
                    open(os.path.join(root, filename), 'rb').read())

                df = df.append(pd.DataFrame({
                    'Filename': filename,
                    'Location': root,
                    'Duration [s]': duration,
                    'Samplerate': samplerate,
                    'Hash': filehash}, index=[0]), sort=False)

    print("Number of files found = {}".format(num_of_files))

    # Reformat total duration from seconds into days, hours, minutes
    total_duration = str(datetime.timedelta(seconds=total_duration))
    print("Total duration [HH:MM:SS] = {}".format(total_duration))

    # Save table as csv:
    df.to_csv('Overview_audiofiles.csv', sep=',', encoding='utf-8')

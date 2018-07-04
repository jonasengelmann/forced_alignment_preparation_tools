#!/usr/bin/python3
# coding: utf-8
import os
import datetime
import fnmatch

import pandas as pd
import librosa


def get_audio_duration(filename):
    '''
    Calculates the duration of an audio file in seconds.
    Also returns samplerate.
    '''
    # Load wav file:
    y, sr = librosa.load(filename)
    # Get duration:
    duration = librosa.get_duration(y=y, sr=sr)
    return duration, sr


def find_wav_file(directory=None):
    '''
    Runs through directory and subdirectories to return all wav files.
    If no directory is passed, it will take the current directory.
    '''
    if not directory:
        directory = os.getcwd()
    assert os.path.isdir(directory)
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, '*.wav'):
            yield os.path.join(root, filename)


if __name__ == "__main__":
    total_duration, num_of_files = 0, 0
    all_filehashes = []
    df = pd.DataFrame()

    for filename in find_wav_file():

        num_of_files += 1

        duration, samplerate = get_audio_duration(filename)

        total_duration += duration

        # Calculate hash to find potential duplicates:
        file_hash = hash(open(filename, 'rb').read())
        all_filehashes.append(file_hash)

        # Append information to result table:
        df = df.append(pd.DataFrame({
            'Filename': os.path.basename(filename),
            'Location': os.path.dirname(filename),
            'Duration [s]': duration,
            'Samplerate': samplerate,
            'Hash': file_hash}, index=[0]), sort=False)

    print("Number of files found = {}".format(num_of_files))

    print("Number of unique files = {}".format(len(set(all_filehashes))))

    # Reformat total duration from seconds into days, hours, minutes
    total_duration = str(datetime.timedelta(seconds=total_duration))
    print("Total duration [HH:MM:SS] = {}".format(total_duration))

    # Save table as csv:
    df.to_csv('Overview_audiofiles.csv', sep=',', encoding='utf-8')

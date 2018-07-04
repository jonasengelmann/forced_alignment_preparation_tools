#!/usr/bin/python3
# coding: utf-8
import os
import codecs

def extract_words(file):
    '''Extracts words of a simple transcription file and returns
    them in a list without punctuation'''

    # Load file:
    with codecs.open(file, 'r', encoding="utf-8") as txtfile:
        transcript = txtfile.read()

    # Remove Punctuation:
    transcript = transcript.replace(",", "")
    transcript = transcript.replace(".", "")
    transcript = transcript.replace("?", "")
    transcript = transcript.replace("!", "")

    # Remove possible double space:
    transcript = transcript.replace("  ", " ")

    # Lower capital letters:
    transcript = transcript.lower()

    # Return single words in a list:
    return transcript.split(" ")


if __name__ == "__main__":
    current_dir = os.getcwd()
    words = []

    for file in os.listdir(current_dir):
        if file.endswith(".txt", ".lab"):
            words += extract_words(file)

    # Make list of words unique:
    words = list(set(words))

    # Sort alphabetically:
    words = sorted(words)

    # Save to text file:
    with codecs.open("Dictionary.txt", 'w', encoding="utf-8") as output:
        output.write("\n".join(words))

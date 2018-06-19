#!/usr/bin/python3
# coding: utf-8
import os
import codecs

"""Simple template script that phonetically transcribes entries from
a dictionary according to a simple rule based system. """

# Dictionary filename with entries to phonetically transcribe:
dictionary_file = "./Dictionary.txt"

result = []

with codecs.open(dictionary_file, "r", encoding="utf-8") as file:
    text = file.read()

# Split into words:
words = text.split("\n")

# Cycle through each word:
for word in words:
    single_letters = list(word)
    length = len(single_letters)
    phonetic_transcription = []
    skip_next_letter = False

    # Create phonetic transcription letter by letter:
    for idx, letter in enumerate(single_letters):

        if skip_next_letter:
            skip_next_letter = False
            continue

        # Multiple letters:
        # Example:
        # ch -> x
        if idx < length - 1 and letter == "c" and single_letters[idx + 1] == "h":
            phonetic_transcription.append("x")
            skip_next_letter = True

        # Single letters:
        # Example:
        # c -> ts
        # ć -> s
        elif letter == "c":
            phonetic_transcription.append("ts")

        elif letter == "ć":
            phonetic_transcription.append("s")

        # Final position:
        # Example:
        # final b->p
        elif letter == "b" and idx == length - 1:
            phonetic_transcription.append("p")

        # If no rule, take over single letter:
        else:
            phonetic_transcription.append(letter)

    result.append(word + " " + " ".join(phonetic_transcription))

# Save to text file:
with codecs.open("Dictionary_with_transcription.txt", 'w', encoding="utf-8") as output:
    output.write("\n".join(result))

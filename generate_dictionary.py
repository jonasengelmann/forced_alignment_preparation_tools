#!/usr/bin/python3
# coding: utf-8
import os
import codecs

current_dir = os.getcwd()
words = []

for file in os.listdir(current_dir):
    if file.endswith(".txt") or file.endswith(".lab"):
        with codecs.open(file, 'r', encoding="utf-8") as txtfile:
            transcripttext = txtfile.read()

        # Remove Punctuation
        transcripttext = transcripttext.replace(",", "")
        transcripttext = transcripttext.replace(".", "")
        transcripttext = transcripttext.replace("?", "")
        transcripttext = transcripttext.replace("!", "")

        # Remove possible double space:
        transcripttext = transcripttext.replace("  ", " ")

        # Lower capital letters:
        transcripttext = transcripttext.lower()

        # Split in words and save in list:
        words = words + transcripttext.split(" ")

# Make list of words unique:
words = list(set(words))

# Sort alphabetically:
words = sorted(words)

# Save to text file:
with codecs.open("Dictionary.txt", 'w', encoding="utf-8") as output:
    output.write("\n".join(words))

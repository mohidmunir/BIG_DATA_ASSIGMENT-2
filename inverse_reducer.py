#!/usr/bin/env python

import sys

# Reducer function for Inverse Document Frequency
current_word = None
doc_count = 0

# Process each key-value pair from the mapper
for line in sys.stdin:
    # Split the input line into word and count
    word, _ = line.strip().split('\t', 1)
    
    # If the word is the same as the current word, increment the document count
    if current_word == word:
        doc_count += 1
    else:
        # If this is a new word, emit the inverse document frequency for the previous word
        if current_word:
            inverse_document_frequency = doc_count  # Assuming doc_count represents inverse document frequency
            print(f"{current_word}\t{inverse_document_frequency}")
        # Update the current word and reset the document count
        current_word = word
        doc_count = 1

# Output the inverse document frequency for the last word
if current_word:
    inverse_document_frequency = doc_count  # Assuming doc_count represents inverse document frequency
    print(f"{current_word}\t{inverse_document_frequency}")

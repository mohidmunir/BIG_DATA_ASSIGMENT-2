#!/usr/bin/env python

import sys

# Reducer function for Term Frequency
current_word = None
total_count = 0

# Process each key-value pair from the mapper
for line in sys.stdin:
    # Split the input line into word and count
    word, count = line.strip().split('\t', 1)
    
    # Convert count to an integer
    count = int(count)
    
    # If the word is the same as the current word, accumulate the count
    if current_word == word:
        total_count += count
    else:
        # If this is a new word, emit the term frequency for the previous word
        if current_word:
            term_frequency = total_count  # Assuming total_count represents term frequency
            print(f"{current_word}\t{term_frequency}")
        # Update the current word and reset the total count
        current_word = word
        total_count = count

# Output the term frequency for the last word
if current_word:
    term_frequency = total_count  # Assuming total_count represents term frequency
    print(f"{current_word}\t{term_frequency}")

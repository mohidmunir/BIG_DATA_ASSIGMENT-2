#!/usr/bin/env python

import sys

current_word = None
current_count = 0

# Read input from standard input
for line in sys.stdin:
    # Split the input into word and count
    word, count = line.strip().split('\t', 1)
    
    # Convert count to integer
    try:
        count = int(count)
    except ValueError:
        # If count is not a number, continue to the next iteration
        continue
    
    # If the word is the same as the current word, increment count
    if current_word == word:
        current_count += count
    else:
        # If the word is different, emit the current word and count
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Emit the last word and count
if current_word:
    print(f"{current_word}\t{current_count}")

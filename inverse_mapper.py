#!/usr/bin/env python

import sys

# Mapper function for Inverse Document Frequency
for line in sys.stdin:
    # Split the input line into word and count
    word, _ = line.strip().split('\t', 1)
    # Emit the word with count 1 for Inverse Document Frequency calculation
    print(f"{word}\t1")
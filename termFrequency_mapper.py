#!/usr/bin/env python

import sys

# Mapper function for Term Frequency
for line in sys.stdin:
    # Split the input line into word and count
    word, count = line.strip().split('\t', 1)
    # Emit the word and count for Term Frequency calculation
    print(f"{word}\t{count}")
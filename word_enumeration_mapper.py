#!/usr/bin/env python

import sys

# Read input from standard input
for line in sys.stdin:
    # Split the line into ARTICLE_ID and SECTION_TEXT
    article_id, section_text = line.strip().split('\t', 1)
    # Tokenize the text into words
    words = section_text.split()
    # Emit each word along with a count of 1
    for word in words:
        print(f"{word}\t1")
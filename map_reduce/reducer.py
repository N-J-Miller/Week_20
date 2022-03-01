#!/usr/bin/env python
# ^ shebang

# Dependencies:
import sys

# count mapper output
current_word = None
current_count = 0
word = None


for line in sys.stdin:
    line = line.strip()

    word, count = line.split("\t", 1)

    count = int(count)

    if current_word == word:
        current_count += count
    else:
        # handles the None exception
        if current_word:
            print(current_word + "\t" + str(current_count))

        # reset for next loop
        current_count = count 
        current_word = word

# edge case
if current_word == word:
    print(current_word + "\t" + str(current_count))       


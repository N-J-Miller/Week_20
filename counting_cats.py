#!/usr/bin/env python
# ^shebang line

# Dependencies and modules:
import sys
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from collections import Counter

# read in an input text file and remove beginning/ending whitespaces:
input_text = [line.strip() for line in sys.stdin]

#convert list to a string for tokenization:
text = str(input_text)

# tokenize input text:
tokens = word_tokenize(text)

# convert all tokens to lowercase for better countability:
tokens_lower = [token.lower() for token in tokens]

# count 'em up!
token_count = Counter(tokens_lower)

# sort by frequency and print results:
for token, value in token_count.most_common():
    print(token, value)
#!/usr/bin/env python
# ^shebang line 

# Dependencies:
import sys 

# iterate by line in each "standard input":
for line in sys.stdin:
    #remove white spaces at beginning and end of line
    line = line.strip()

    # seperate elements:
    words = line.split()

    
    for word in words:
        print(word + "\t1")



# mapper - maps the elements as I wish them to be
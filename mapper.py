#!/usr/bin/env python3
import sys
import re


for line in sys.stdin:
    
    words = re.split(r"[ .,:;')(?!]+", line.strip().lower())

    
    for word in words:
        if word:  
            print(f"{word}\t1")
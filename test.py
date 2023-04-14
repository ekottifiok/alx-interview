#!/usr/bin/env python3
from sys import stdin

for line in stdin:
    if 'Exit' == line.rstrip():
        break
    print(line.rstrip())
print("Done")

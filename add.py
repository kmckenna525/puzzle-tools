#!/usr/local/bin/python3
import sys
from lib.chrmath import toletter, tonumber, addlines, addfilecontents


def process_chars(args: list):
    tot = 0
    for arg in args:
        for char in arg:
            val = tonumber(char)
            tot += val
    print(toletter(tot))

def process_words(args: list):
    a = args[0]
    b = args[1]
    print(addlines(a,b))

def process_files(args: list):
    a = None
    b = None

    with open(args[0]) as f:
        a = f.readlines()

    with open(args[1]) as f:
        b = f.readlines()

    print(addfilecontents(a, b))

if __name__ == "__main__":
    option = sys.argv[1]
    if option in ['--file','-f']:
        process_files(sys.argv[2:])
    elif option in ['--word','-w']:
        process_words(sys.argv[2:])
    elif option in ['--char','-c']:
        process_chars(sys.argv[2:])
    else:
        process_chars(sys.argv[1:])

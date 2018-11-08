#!/usr/bin/env python3
import sys
import os.path


def is_palindrome(string):
    i = 0
    j = len(string) - 1
    while i <= j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    file = sys.argv[-1]
    if not os.path.isfile(file):
        raise ValueError("Please use an existing file")
    with open(file, 'r') as text_file:
        for line in text_file:
            if is_palindrome(line.lower().rstrip()):
                print(line)


if __name__ == '__main__':
    main()
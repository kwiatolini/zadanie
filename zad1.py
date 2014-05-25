#!/usr/bin/env python
# encoding: utf-8

def counter(b,e):
    while b < e:
        yield b
        b += 1

def main():
    n = int(input())
    for i in counter(0, n):
        b, e = eval(input())
        print(sum(counter(b, e)))

if __name__ == '__main__':
    main()

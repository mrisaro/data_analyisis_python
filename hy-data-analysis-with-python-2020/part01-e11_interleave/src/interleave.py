#!/usr/bin/env python3

def interleave(*lists):
    l = []
    for j in zip(lists):
        l.extend(j)
    return j

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()

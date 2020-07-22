#!/usr/bin/env python3

def distinct_characters(L):
    l = []
    for i in L:
        l.append((i,len(set(i))))
    return dict(l)

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()

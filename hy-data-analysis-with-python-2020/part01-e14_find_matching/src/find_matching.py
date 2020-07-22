#!/usr/bin/env python3

def find_matching(L, pattern):
    ind = []
    for i, x in enumerate(L):
        if ("en" in x):
            ind.append(i)

    return ind

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"],'en'))


if __name__ == "__main__":
    main()

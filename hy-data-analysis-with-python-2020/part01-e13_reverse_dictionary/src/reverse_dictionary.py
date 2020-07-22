#!/usr/bin/env python3

def reverse_dictionary(d):
    rev = []
    for k,v in d.items():
        for j in v:
            rev.append((j,k))
    print(dict(rev))

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reverse_dictionary(d)

if __name__ == "__main__":
    main()

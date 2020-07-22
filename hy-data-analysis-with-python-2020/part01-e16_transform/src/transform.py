#!/usr/bin/env python3

def transform(s1, s2):
    sp1 = list(map(int,s1.split()))
    sp2 = list(map(int,s2.split()))
    l=[]
    for i,j in zip(sp1,sp2):
        l.append(i*j)
    return l

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()

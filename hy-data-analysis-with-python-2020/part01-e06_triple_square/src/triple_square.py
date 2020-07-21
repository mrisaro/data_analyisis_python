#!/usr/bin/env python3
def triple(x):
        return x*3

def square(x):
        return x**2

def main():

    for i in range(1,11):
        sq = square(i)
        tr = triple(i)
        if sq<=tr:
             print(f'triple({i})=={tr} square({i})=={sq}')
        else:
            break

if __name__ == "__main__":
    main()

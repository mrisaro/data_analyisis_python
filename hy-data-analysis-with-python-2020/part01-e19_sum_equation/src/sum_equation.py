#!/usr/bin/env python3

def sum_equation(L):
    if L==[]:
        return "0 = 0"
    else:
        tup = (" + ".join([str(x) for x in L]),str(sum(L)))
        return " = ".join(tup)

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()

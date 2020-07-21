#!/usr/bin/env python3

def fun_sort(L):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                # Swap the elements
                L[i], L[i + 1] = L[i + 1], L[i]
                # Set the flag to True so we'll loop again
                swapped = True

def merge(L1, L2):
    L = L1+L2
    fun_sort(L)
    return L

def main():
    L1 = [10,5,6,8]
    L2 = [8,9,4,5,8,7]
    print(merge(L1,L2))
    L1 = [1,8,5,2]
    L2 = [11,7,6,5]
    print(merge(L1,L2))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    # get possible combinations of two dice that sum to 5.
    for i in range(1,7):
        for j in range(1,7):
            sum = i+j
            if sum==5:
                print(f'({i},{j})')



if __name__ == "__main__":
    main()

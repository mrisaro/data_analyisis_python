#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while True:
        obj = input('Choose a shape (triangle, rectangle, circle): ')

        if obj == '':
            break

        elif obj=='triangle':
            base_in = float(input('Give base of the triangle: '))
            heig_in = float(input('Give height of the triangle: '))
            area = base_in*heig_in/2
            print(f"The area is {area:.6f}")

        elif obj == 'rectangle':
            wid_in = float(input('Give width of the rectangle: '))
            hei_in = float(input('Give height of the rectangle: '))
            area = wid_in*hei_in
            print(f"The area is {area:.6f}")

        elif obj == 'circle':
            rad_in = float(input('Give radius of the circle: '))
            area = math.pi*rad_in**2
            print(f"The area is {area:.6f}")

        else:
            print(f"Unknown shape!")



if __name__ == "__main__":
    main()

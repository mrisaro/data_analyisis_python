# File with different excercises

from math import sqrt, log
l=[1,3,65,3,-1,56,-10]
for x in l:
    if x < 0:
        continue
    print(f"Square root of {x} is {sqrt(x):.3f}")
    print(f"Natural logarithm of {x} is {log(x):.4f}")

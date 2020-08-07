#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    pat=r"(?:\[(\s*?[-+]?\d+\s*?)\])"
    l = re.findall(pat,s)
    l_int = []
    for a in l:
        l_int.append(int(a))
    return l_int

def main():
    print(integers_in_brackets("  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx!"))

if __name__ == "__main__":
    main()

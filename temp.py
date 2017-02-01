import os
import sys


def permute(s, l, r):
    if (l == r):
        print ("".join(s))
    else:
        for i in range(l, r+1):
            s[l],s[i] = s[i],s[l]
            permute(s, l+1, r)
            s[i],s[l] = s[l],s[i]

def main():
    s = list("ABC")
    permute(s, 0, len(s)-1)

if __name__ == "__main__":
    main()

    

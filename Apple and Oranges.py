import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    c1=0
    c2=0
    for i in range(0,len(apples)):
        apples[i]+=a
        if(apples[i]>=s and apples[i]<=t):
            c1+=1
    for i in range(0,len(oranges)):
        oranges[i]+=b
        if(oranges[i]>=s and oranges[i]<=t):
            c2+=1
    print(c1)
    print(c2)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
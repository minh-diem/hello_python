import sys


def min(list):
    a=sys.maxsize
    index = 0

    for i in range(0, len(list)):
        if list[i]<a:
            a=list[i]
            index=i
    return index

print(max([-2,-9, -15, 7, -3])) # 9
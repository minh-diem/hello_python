"""
Return min and max of list in one iteration
"""
import sys
def find_min_max(list):
    # cur_min=sys.maxsize
    # cur_max=-sys.maxsize-1

    # for x in list:
    #     cur_min = min(cur_min, x)
    #     cur_max = max(cur_max, x)

    return list.index(min(list))


print(find_min_max([2,5,8,4,9])) # [2,9]

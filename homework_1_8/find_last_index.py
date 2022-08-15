"""
Return last index if element x if exists
Otherwise return None
"""

def find_index(list, x):
    for index in range(len(list)-1,-1,-1):
        if list[index]==x:
            return index
    return None



print(find_index([2,5,8,4,9], 4)) 
print(find_index([2,4,5,8,4,9], 4)) 
print(find_index([2,5,8,4,9], 1)) 

list1 = [3,1,2,6,4,5]
list2 = [10,3,22,61,42,53]

count = 0
for y in list2:
    for x in list1:
        if x + y == 7:
            count+=1
    print()
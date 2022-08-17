def longest_word(list):
    a=""
    for x in list:
        if len(x)>len(a):
            a=x
    return a


print(longest_word(["abc", "banana", "fruits", "helloworld"]))
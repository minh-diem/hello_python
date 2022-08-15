def f():
    for p in range(1,10):
        print(' ', p, "|", end = "")
        for x in range(1,10):
            if x*p<10:
                print(" ", end="")
            print(x*p, end=" ")
        print()

f()
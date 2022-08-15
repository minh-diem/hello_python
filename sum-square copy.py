def sum_square(n):
    x=n
    sum=0
    while x>=1:
        sum+=x**2
        x-=1
    
    return sum

print(sum_square(5))
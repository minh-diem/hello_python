import is_prime
def prime(n):
    x=2
    count=0
    while x<n:
        if is_prime.is_prime(x):
            count+=1
        x+=1
    return count

print(prime(17))
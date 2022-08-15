def fizzBuzz(x):
    if x%3==0 and x%5==0:
        return 'FizzBuzz'
    elif x%5==0:
        return 'Buzz'
    elif x%3==0:
        return 'Fizz'
    else: 
        return x

# print(3, fizzBuzz(3))
# print(5, fizzBuzz(5))
# print(9, fizzBuzz(9))
# print(15, fizzBuzz(15))
# print(17, fizzBuzz(17))
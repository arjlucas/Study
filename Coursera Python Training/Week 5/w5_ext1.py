# Coursera Python Training 1
# Lucas Silva
# Week 5 - Exercício Extra 1 - FizzBuzz

def fizzbuzz(n):
    v1 = "Fizz"
    v2 = "Buzz"
    v3 = "FizzBuzz"
    if n % 3 == 0:
        if n % 5 == 0:
            return v3
        elif n % 5 != 0:
            return v1
    elif n % 5 == 0:
        return v2
    else:
        return n
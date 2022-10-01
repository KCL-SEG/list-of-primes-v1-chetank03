"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 0
    num = 2
    while count < number_of_primes:
       
        for i in range(2,(num//2)+1):
            if num%i==0: 
                break
        else:
            list.append(num);
            count+=1
        num+=1

    return list


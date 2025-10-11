import math as mt
upperBound = int(input("Enter a number: "))

sum = 0

def checkPrime(num):
    end = int(mt.sqrt(num))
    count = 0
    for val in range(1, end+1):
        if(num%val == 0):
            count = count + 1
    
    if count > 1:
        return False
    else:
        return True


for number in range(2, upperBound+1):
    if checkPrime(number):
        sum = sum + number
    else:
        continue

print(f"Sum of prime numbers upto {upperBound} is {sum}")
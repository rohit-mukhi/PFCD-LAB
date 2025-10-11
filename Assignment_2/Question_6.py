import math as mt

number = int(input("Enter a number: "))

end = int(mt.sqrt(number))
count = 0
for val in range(1, end):
    if(number%val == 0):
        count = count + 1
    
if count > 1:
    print(f"{number} is a composite number")
else:
    print(f"{number} is a prime number")
number = int(input("Enter a number: "))

while number < 0:
    number = int(input("Enter a positive number please: "))

if number%2 == 0:
    print(f"Result: {number*2}")
else:
    print(f"Result: {number ** 2}")
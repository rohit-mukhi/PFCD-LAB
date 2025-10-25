import random

n = int(input("Enter size of list: "))
arr = [random.randint(1, 100) for _ in range(n)]

print(f"The list is: {arr}\n")

val = int(input("Enter value to remove: "))

new_arr = [item for item in arr if item != val]

print(f"New list: {new_arr}")


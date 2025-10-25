# The sum and average of numbers in a list

import statistics as st

arr = []

number_of_elements = int(input("Enter number of elements: "))

for idx in range(0, number_of_elements):
    val = int(input("Enter an integer: "))
    arr.append(val)

sum_of_elements = sum(arr)
average = st.mean(arr)

print(f"The sum of all elements is: {sum_of_elements}")
print(f"The average is: {average}")




# The sum and average of numbers in a list

import statistics as st
import random

number_of_elements = int(input("Enter number of elements: "))

arr = [random.randint(1,100) for _ in range(number_of_elements)]

sum_of_elements = sum(arr)
average = st.mean(arr)

print(f"The list is: {arr}")
print(f"The sum of all elements is: {sum_of_elements}")
print(f"The average is: {average}")







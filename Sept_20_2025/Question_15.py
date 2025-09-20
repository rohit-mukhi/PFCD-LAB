import math as mt

print("Enter amount: ")
investment = float(input())
amount_10 = investment * (pow((1+12), 10))
amount_20 = investment * (pow((1+12), 20))
amount_30 = investment * (pow((1+12), 30))
print(f"Amount received after 10 years: {amount_10}")
print(f"Amount received after 20 years: {amount_20}")
print(f"Amount received after 30 years: {amount_30}")

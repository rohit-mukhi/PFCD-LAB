import math as mt

val_1 = pow(mt.e, mt.pi)
print(f"Value of e raised to power pi is {val_1}")
val_2 = pow(mt.pi, mt.e)
print(f"Value of pi raised to power e is {val_2}")

if val_1 > val_2:
    print("Ok")
else:
    print("Ok anyway")

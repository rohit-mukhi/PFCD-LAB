marks = int(input("Enter marks: "))

grade = ""
remarks = ""

if 90 <= marks <= 100:
    grade = "A"
    remarks = "Excellent"
elif 80 <= marks <90:
    grade = "B"
    remarks = "Good"
elif 70 <= marks <80:
    grade = "C"
    remarks = "Average"
elif 60 <= marks <70:
    grade = "D"
    remarks = "Needs improvement"
elif 0 <= marks < 60:
    grade = "F"
    remarks = "Failing"
else:
    print("Invalid marks!")

print(f"Your grade is: {grade}")
print(f"Remarks: {remarks}")
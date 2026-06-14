name = input("Student Name: ")
marks = float(input("Marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print("\n----- RESULT -----")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)

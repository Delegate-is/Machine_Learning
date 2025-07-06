# Write program to find user marks and grade accordingl
marks = int(input("Enter your marks: "))
if marks >= 95:
    grade = 'A+'
elif marks >= 80:
    grade = 'A'
elif marks >= 70:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
elif marks < 60:
    grade = 'Fail'
print(f"Your grade is: {grade}")
# Note: The last line in the original code has a syntax error.

# Program to get scale from employer and display salary accordingly
scale = input("Enter your scale (9, 12, 15, 18, 20): ").upper()
if scale == '9':
    salary = '10,000'
elif scale == '12':
    salary = '20,000'
elif scale == '15':
    salary = '40,000'
elif scale == '18':
    salary = '50,000'
elif scale == '20':
    salary = '70,000'
else:
    salary = 0
    print("Invalid scale entered.")
print(f"Your salary for scale {scale} is: {salary}")

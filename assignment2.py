# Interactive Student Registration and Score Calculator

# 1. Student's first name and surname
first_name = input("joseph: ")
surname = input("obi: ")

# 2. Student's age
age = int(input("24: "))

# 3. Student's department
department = input("geology: ")

# 4. Scores for three subjects (using float allows decimal scores like 85.5)
stratigraphy = float(input("75: "))
geophysics = float(input("80 "))
paleontology = float(input("89 "))

# 5. Total score
total_score = stratigraphy + geophysics + paleontology

# 6. Average score
average_score = total_score / 3

# 6. Average score
average_score = total_score / 3

# 7. Display student information using f-strings
print("\n--- Student Registration & Score Summary ---")
print(f"Full Name: {first_name.title()} {surname.title()}")
print(f"Age: {age}")
print(f"Department: {department.title()}")
print(f"Scores -> Stratigraphy: {stratigraphy}, Geophysics: {geophysics}, Paleontology: {paleontology}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.2f}")
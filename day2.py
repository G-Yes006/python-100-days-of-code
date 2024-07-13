two_digit_number = input("Enter a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
print("Sum of the digits is", int(
    two_digit_number[0])+int(two_digit_number[1]))


# 1st input: enter height in meters e.g: 1.65
height = input("Enter Height in meters: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Enter weight in KG: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = int(weight) / (float(height)*float(height))

# or

BMI = int(weight) / (float(height)**2)
print("Your BMI is: ", int(BMI))

print(2/3)  # 0.6666666666666666
print(4/3)  # 1.3333333333333333
print(4//3)  # 1

# f string
name_va = "G"
age_va = 22
print(f"Hello your name is {name_va} and your age is {age_va}")


def your_weeks(age):
    lived_weeks = (age*52)
    weeks_left = 4000-lived_weeks
    return print(f"You have {weeks_left} weeks left.")


your_weeks(29)

# #  Which number do you want to check?
# number = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


age = 4
if age < 18:
    print("You are not Adult")
    if age <= 10:
        print("you are a Kid")
    elif age < 5:
        print("You are a baby")
else:
    print("You are an adult")


# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters (e.g., 1.55): "))
# Enter your weight in kilograms e.g., 72
weight = float(input("Enter your weight in kilograms (e.g., 72): "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Calculate the BMI using the formula: weight / (height^2)
BMI = weight / (height ** 2)

# Check the BMI category and print the corresponding message
if BMI < 18.5:
    print(f"Your BMI is {BMI:.1f}, you are underweight.")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI:.1f}, you have a normal weight.")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI:.1f}, you are slightly overweight.")
elif 30 <= BMI < 35:
    print(f"Your BMI is {BMI:.1f}, you are obese.")
else:
    print(f"Your BMI is {BMI:.1f}, you are clinically obese.")

year = 2024

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

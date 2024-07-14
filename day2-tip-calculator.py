

# Tip Calculator Program

# Print a welcome message
print("Welcome to the tip calculator")

# Get the total bill amount from the user
total_bill = input("What was the total bill? : ")

# Get the tip percentage the user wants to give
tip_percentage = input(
    "How much tip would you like to give in percentage? 10%, 12%, or 15%: ")

# Get the number of people to split the bill with
people = input("How many people to split the bill?: ")

# Calculate the amount of tip to add to the total bill
tip_to_add = float(total_bill) * (int(tip_percentage) / 100)

# Calculate the total amount each person needs to pay, rounded to 2 decimal places
split_amount = round((float(total_bill) + tip_to_add) / int(people), 2)

# Print the amount each person should pay
print(f"Each person should pay: ${split_amount}")


# print("Welcome to the tip calculator")
# total_bill = input("What was the total bill? : ")
# tip_percentage = input(
#     f"how much tip would you like to give in percentage? 10% 12% or 15%: ")
# people = input("How many people to split the bill?: ")

# tip_to_add = float(total_bill) * (int(tip_percentage)/100)
# split_amount = round((float(total_bill) + tip_to_add)/int(people), 2)


# print(f"Each person should pay: ${split_amount}")

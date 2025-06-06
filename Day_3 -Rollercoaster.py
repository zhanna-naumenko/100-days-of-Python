#Printing the title
# print("Even or Odd")
#
# #Asking user to pick the number
# user_number = int(input("Please write a whole number: "))
#
# # Check if the user's number is odd or even using the modulo operator.
# # If the remainder when dividing by 2 is 1, it's an odd number; otherwise, it's even.
# if user_number % 2 == 1:
#     print(f"The number {user_number} is an odd number.")
# else:
#     print(f"The number {user_number} is even.")


#Printing welcoming
print("Welcome to the Rollercoaster!")

# Ask the user to input their height in centimeters and convert it to an integer.
height = int(input("Please enter your height in cm: "))

# Initialize the total bill to 0.
total_bill = 0

# Check if the user is tall enough to ride the rollercoaster (minimum height required is 120 cm).
if height > 120:
    print("You can ride a rollercoaster!")

    # Ask the user for their age to determine the ticket price.
    age = int(input("What is your age? "))

    # Determine ticket price based on age group.
    if age <= 12:
        total_bill += 5  # Children ticket price.
    elif age <= 18:
        total_bill += 7  # Teen ticket price.
    else:
        total_bill += 12  # Adult ticket price.

    # Ask if the user wants a photo, and add $3 to the bill if they do.
    photo = input("Do you want to take a photo? Type 'y' for Yes and 'n' for No: ")
    if photo == 'y':
        total_bill += 3

    # Print the total bill amount.
    print(f"Your total bill is {total_bill}$")

else:
    # If the user is not tall enough, display a message.
    print("Sorry, you need to grow up to ride the rollercoaster.")



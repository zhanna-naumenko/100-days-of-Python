import random
import string

#asking the user about the number of letters in the password
number_of_letters = int(input("How many letter would you like in your password? "))

#asking the user about the number of numbers in the password
number_of_numbers = int(input("How many numbers would you like in your password? "))

#asking the user about the number of punctuations in the password
number_of_punctuation = int(input("How many punctuations would you like in your password? "))

#create a list of all uppercase and lowercase letters
alphabet = list(string.ascii_letters)

#create a list of digits from 0 to 9
list_numbers = list(string.digits)

# create a list of punctuation/special character
list_punctuation = list(string.punctuation)

# ______________________________________________________________
# empty string that will store all characters of the password
user_password = ""

# add random letters to the password list
for val in range(number_of_letters):
    user_password += random.choice(alphabet)

# add random numbers to the password list
for val in range(number_of_numbers):
    user_password += random.choice(list_numbers)

# add random punctuation characters to the password list
for val in range(number_of_punctuation):
    user_password += random.choice(list_punctuation)

# making a list from a string to shuffle the characters
user_password_list = list(user_password)

# shuffling the characters
random.shuffle(user_password_list)

# making the string from the shuffled list
user_password = ''.join(user_password_list)

# print the password for user
print(user_password)

# ________________________________________________________________
# empty list that will store all characters of the password
list_of_password = []

# add random letters to the password list
for num in range(1, number_of_letters +1):
    random_letter = random.randint(0, len(alphabet) - 1)
    list_of_password.append(alphabet[random_letter])

# add random numbers to the password list
for num in range(1, number_of_numbers +1):
    random_number = random.randint(0, len(list_numbers) - 1)
    list_of_password.append(list_numbers[random_number])

# add random punctuation characters to the password list
for num in range(1, number_of_punctuation +1):
    random_punctuation = random.randint(0, len(list_punctuation) - 1)
    list_of_password.append(list_punctuation[random_punctuation])

# print the password characters before shuffling
print(list_of_password)

# shuffle the list to randomize the order of character
random.shuffle(list_of_password)

# convert the list of characters into a single string password
user_password = ""
for val in list_of_password:
    user_password += val
print(user_password)

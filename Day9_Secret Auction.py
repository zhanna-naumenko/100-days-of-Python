import Day9_art

# Print the program logo from the imported module
print(Day9_art.logo)

# Welcome message for the user
print("Welcome to the secret auction program.")

# Dictionary to store bidder names as keys and their bids as values
name_and_bid = {}

# Boolean flag to control the auction loop
auction_on = True

# Keep asking for bids while the auction is active
while auction_on:
    # Ask the user for their name
    user_name = input("What is your name? ")

    # Ask the user for their bid amount and convert it to an integer
    user_bid = int(input("What is your bid? $"))

    # Store the name and bid in the dictionary
    name_and_bid[user_name] = user_bid

    # Ask if there are any other bidders
    other_bidders = input("Are there other bidders? Type 'yes' or 'no': ").lower()

    # Clear the screen by printing multiple new lines (simple console clear)
    print("\n" * 20)

    # If there are no more bidders, end the auction
    if other_bidders == 'no':
        auction_on = False

# Find the bidder with the highest bid
max_key = max(name_and_bid, key=name_and_bid.get)

# Get the highest bid value
max_value = name_and_bid[max_key]

# Announce the winner of the auction
print(f"The winner is {max_key} with a bid of ${max_value}.")
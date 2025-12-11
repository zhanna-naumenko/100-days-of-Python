#printing welcoming
print("Welcome to Python Pizza Deliveries!")

final_price = 0

# pizza size
while True:
    size = input("What size pizza do you want? S, M or L: ").upper()
    if size in ["S", "M", "L"]:
        break
    else:
        print("Invalid input. Please choose S, M, or L.")

# add price based on size
if size == "S":
    final_price += 15
elif size == "M":
    final_price += 20
else:
    final_price += 25

# pepperoni choice
while True:
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
    if pepperoni in ["Y", "N"]:
        break
    else:
        print("Invalid input. Please choose Y or N.")

# add pepperoni price
if pepperoni == "Y":
    if size == "S":
        final_price += 2
    else:
        final_price += 3

# extra cheese choice
while True:
    extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
    if extra_cheese in ["Y", "N"]:
        break
    else:
        print("Invalid input. Please choose Y or N.")

# add cheese price
if extra_cheese == "Y":
    final_price += 1
#printing final price
print(final_price)

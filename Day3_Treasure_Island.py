#welcoming
print("Welcome to Treasure Island. Your mission is to find the treasure.")

#choosing the direction
choice_direction = input("Your are standing on the desert land and you need to choose which direction you will go. Choose 'right' or 'left':").lower()

if choice_direction == "left":
    # choosing the action
    choice_action = input("You reached the lake. Choose will you 'swim' or 'wait' for the boat: ").lower()
    if choice_action == "wait":
        # choosing the door
        choice_door = input("You reached the abandoned house. Choose which door you will enter: 'red', 'blue' or 'yellow': ").lower()
        if choice_door =="yellow":
            print("Congratulation! You WIN!")
        elif choice_door == "red" or choice_door == "blue":
            print("You fell into a deep, bottomless pit. Game over!")
        else:
            print("Your input is wrong. Please try again")
    elif choice_action == "swim":
        print("A giant fish swallowed you. Game over!")
    else:
        print("Your input is wrong. Please try again")
elif choice_direction == "right":
    print("You came across a giant spider and lost the battle. Game over!")
else:
    print("Your input is wrong. Please try again")

import random
import Day14_art
import Day14_game_data

# Print the game logo
print(Day14_art.logo)

def random_numb():
    """
    Returns a random index from the game_data list.
    We subtract 1 because list indexes start from 0.
    """
    random_number = random.randint(0, len(Day14_game_data.data) - 1)
    return random_number

def get_two_choices():
    """
    Returns two different random indexes.
    Ensures that choice A and choice B are not the same.
    """
    first_choice = random_numb()
    second_choice = random_numb()

    # Keep generating the second choice until it is different
    while first_choice == second_choice:
        second_choice = random_numb()

    return first_choice, second_choice

def get_winner(choice_a, choice_b):
    """
    Compares follower counts of two choices
    and returns 'a' if A has more followers,
    otherwise returns 'b'.
    """
    if choice_a["follower_count"] > choice_b["follower_count"]:
        return "a"
    else:
        return "b"


# Initialize score and game state
user_score = 0
game_on = True


# Get initial two choices
a_index, b_index = get_two_choices()
choice_a = Day14_game_data.data[a_index]
choice_b = Day14_game_data.data[b_index]


while game_on:
    # Display comparison for choice A
    print(f"Compare A: {choice_a["name"]}, a {choice_a["description"]}, from {choice_a["country"]}")
    print(Day14_art.vs)
    # Display comparison for choice B
    print(f"Compare B: {choice_b["name"]}, a {choice_b["description"]}, from {choice_b["country"]}")

    # Get user's guess
    user_choice = input("Who has more followers? ").lower()

    # Determine the correct answer
    winner = get_winner(choice_a, choice_b)

    # Check if the user is correct
    if user_choice == winner:
        user_score += 1
        print(f"Correct! Current score: {user_score}")

        # Keep the winner and replace the loser
        if winner == "a":
            choice_b = Day14_game_data.data[random_numb()]
        else:
            choice_a = Day14_game_data.data[random_numb()]
    else:
        # End the game if the user is wrong
        game_on = False
        print("You lose!")

import random
from question_c import test_get_random_number, get_random_number

test_get_random_number()

while True:
    while True:
        bot_number = get_random_number()
        user_guess = int(input("Guess the number (1-5): "))

        if user_guess == bot_number:
            print(f"Good Job! The correct number is ({bot_number}).")
            break
        else:
            print("Wrong, that is not the correct number. Try again.")

    
    replay = input("Would you like to replay? (y/n): ")
    if replay != "y":
        break
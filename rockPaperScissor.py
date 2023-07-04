import random
user_score = 0
com_score = 0
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_score+=1
        else:
            print("Paper covers rock! computer win.")
            com_score+=1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_score+=1
        else:
            print("Scissors cuts paper! computer win.")
            com_score+=1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_score+=1
        else:
            print("Rock smashes scissors! computer win.")
            com_score+=1

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    if com_score == 3 or user_score == 3:
        break
    else:
        continue
if com_score>user_score:
    print(f"Computer win the match with {com_score} score")
elif com_score<user_score:
    print(f"User win the match with {user_score} score")
else:
    print("It's tie!")
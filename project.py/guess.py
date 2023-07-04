import random
print("Welcome to number guessing game!")
def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == 'easy':
        count = 10
        print(f"You have {count} attempts remaining to guess the number.")
    elif level == 'hard':
        count = 5
        print(f"You have {count} attempts remaining to guess the number.")
guess = True
number = random.randint(1,100)
def game():
    while guess:
        num = int(input("guess a number"))
        if num>number:
            print("to high")
            count -= 1
            print(f"You have {count} attempts remaining to guess the number.")

        elif num<number:
            print("to low")
            count -= 1
            print(f"You have {count} attempts remaining to guess the number.")
        elif number==num:
            print(f"you got it! The number is {number} ")
            guess = input("Guess again? y/n")
            if guess.lower() == 'y':
              continue
            else:
              break
        else:
            print("you not guess the number")
            
        if count <= 0:
            print("you've run out of guesses,you lose.")
            break
                
game()       

        
        


                    
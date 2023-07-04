def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious room. There are two doors, one on the left and one on the right.")
    
    choice = input("Which door do you choose? (left/right) ")

    if choice.lower() == "left":
        print("You enter the left door and find a treasure chest!")
    elif choice.lower() == "right":
        print("You enter the right door and encounter a ferocious monster!")
    else:
        print("Invalid choice. Try again.")
adventure_game()
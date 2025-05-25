def game():
    import random
    computer_guess = random.randint(1,100)
    tried = 0
    user_input =  None
    while(user_input != computer_guess):
        user_input = int(input("Enter a  number (1-100): "))
        tried += 1
        if(computer_guess>user_input):
            print("You have enterd a smaller nunber")
        elif(computer_guess<user_input):
            print("You have enterd a bigger number")
        else:
            print("Congo, right answer!")

    print(f"Total number of tried {tried}")
print("Welcome to Number Guessing game")
choice = None
while(choice != 2):
    print("1.Start the game\n2.Exit")
    c = int(input("Enter a number: "))
    if(c == 1):
        game()
    elif(c == 2):
        print("Exitting. Thank you!")
        exit()
    else:
        print("Enter a valid choice.")
    
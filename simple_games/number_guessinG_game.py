import random
print("lets play number guessing game . computer will assume a number (1-100) and find out the number of attempt to guess the number")
computer_assume=random.randrange(1,101)
print("computer assume a number between 1-100")

while True:
    attempt=0
    while True:
        user_guess=int(input("enter your guess:"))
        attempt+=1
        if user_guess==computer_assume:
            print(f"you guessed it right in {attempt} attempt")
            break
        elif user_guess>(computer_assume+30):
            print("your guess is too high")
        elif user_guess<(computer_assume-30):
            print("your guess is too Low")
        elif user_guess>(computer_assume+15):
            print("your guess is high")
        elif user_guess<(computer_assume-15):
            print("your guess is low")
        elif user_guess>(computer_assume+7):
            print("your guess is nearly hi")
        elif user_guess<(computer_assume-7):
            print("your guess is nearly low")
        elif user_guess>computer_assume:
            print("your guess is almost there but little hi")
        elif user_guess<computer_assume:
            print("your guess is almost there but little low")

    play_agin=input("Do you want to play again(y/n): ")
    if play_agin.lower()=="n":
        break

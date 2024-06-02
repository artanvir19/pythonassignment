import random
print("lets play rock paper scissors ")
while True:
   user_choice=input("Enter a choice(rock,paper,scissor): ")
   possible_choice=["rock","paper","scissor"]
   computer_choice=random.choice(possible_choice)
   if user_choice in possible_choice:
        print(f"computer choice is {computer_choice}")
        if user_choice==computer_choice:
            print("This is a tie ")
        elif computer_choice=="rock":
            if user_choice=="paper":
                print("you win")
            else:
                print("you lose")
        elif computer_choice=="paper":
            if user_choice=="scissor":
                print("you win")
            else:
                print("you lose")
        elif computer_choice=="scissor":
            if user_choice=="rock":
                print("you win")
            else:
                print("you lose")
   else:
       print("invalid input")
   play_again=input("Do you want to play again? (y/n) ")
   if play_again.lower()=="n":
       break

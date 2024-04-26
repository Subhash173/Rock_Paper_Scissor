import random

print("\n----------Welcome to the game.----------")

option = ("rock","paper","scissor")

while True:
   
    user = input("\nEnter the option (rock, paper, scissor):")

    computer = random.choice(option)

    print("\nUser choice : ", user )
    print("Computer choice :",computer)

    if user == computer:
        print("\nIts Tie!!\n")

    elif user == "rock" and computer == "paper\n":
        print("Computer won!!\n")
        
    elif user == "paper" and computer == "scissor\n":
        print("Computer won!!")

    elif user == "scissor" and computer == "rock\n":
        print("\nComputer won!!")

    elif user not in option:
        print("\nPlease select from (rock, paper, scissor) options.")    

    else:
        print("\nUser won!!")

    play_again = input("\nDo you want to play again (y/n) :")
    if play_again == "y":
        print("")

    elif play_again == "n":
        print("\n----------Game Over---------")
        break
    
    else:
        print("\nPlease select (y/n).")


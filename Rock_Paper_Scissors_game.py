import random
options = ["Rock", "Paper", "Scissors"]

def Rock_Paper_Scissors_game(options):
    user_s = 0
    computer_s = 0

    for i in range(3):
        computer = random.choice(options)
        user = input("Rock, Paper, or Scissors?: ").replace(" ", "").capitalize()

        if user not in options:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        else:
            if user == computer:
                print("Tie! Computer chose",computer)
            else:
                if user == "Rock":
                    if computer == "Paper":
                        print("You Lose!", computer, "covers", user)
                        computer_s += 1
                if user == "Rock":
                    if computer == "Scissors":
                        print("You Win!", user, "smashes", computer)
                        user_s += 1

                if user == "Paper":
                    if computer == "Rock":
                        print("You Win!", user, "covers", computer)
                        user_s += 1
                if user == "Paper":
                    if computer == "Scissors":
                        print("You Lose!", computer, "cuts", user)
                        computer_s += 1

                if user == "Scissors":
                    if computer == "Rock":
                        print("You Lose!", computer, "smashes", user)
                        computer_s += 1
                if user == "Scissors":
                    if computer == "Paper":
                        print("You Win!", user, "cuts", computer)
                        user_s += 1       
                        
        if i < 2: 
            print("Computer Score:",computer_s,"| User Score:",user_s)
    print("-----------FINAL SCORE-----------")
    print("Computer Score:",computer_s,"| User Score:",user_s)


Rock_Paper_Scissors_game(options)
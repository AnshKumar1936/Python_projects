import random

item_list = ["Rock" , "Paper" , "Scissor"]

user_choice = input("Enter your move Rock Paper Scissor:")
comp_choice = random.choice(item_list)

print("User choice:",user_choice, "Computer choice:", comp_choice)

if(user_choice == comp_choice):
    print("Both Choses the same: Match Tie")

elif(user_choice == "Rock"):
    if(comp_choice == "Paper"):
        print("Paper cover Rock: Computer Wins")
    else:
        print("Rock Smashes Scissor: You Win")

elif(user_choice == "Paper"):
    if(comp_choice == "Scissor"):
        print("Scissor cuts Paper: Computer Wins")
    else:
        print("Paper covers Rock: You Win")

elif(user_choice == "Scissor"):
    if(comp_choice == "Rock"):
        print("Rock break Scissor: Computer Wins")
    else:
        print("Scissor cut Paper: You Win")



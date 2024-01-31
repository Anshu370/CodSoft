import random

choices = {1: "Rock", 2: "Paper", 3: "Scissor"}

stop = 1
com, user = 0, 0
while stop != 0:
    print("<---* Points *--->")
    print(f"<---* Computer {com} *--->")
    print(f"<---* User {user} *--->")
    comp_choice = random.randint(1, 3)
    print("Select Any one option")
    user_Choice = int(input(choices))

    if user_Choice == comp_choice:
        print("Match Draw")
    else:
        if user_Choice == 1 and comp_choice == 3:
            user += 1
            print("You Won this Match")
        elif user_Choice == 2 and comp_choice == 1:
            user += 1
            print("You Won this Match")
        elif user_Choice == 3 and comp_choice == 2:
            user += 1
            print("You Won this Match")
        else:
            com += 1
            print("Computer Won This Match")

    stop = int(input("If you want to stop enter 0 Or if want to continue enter 1"))

print("You Ended")
print("Final Score")
print(f"<----- Computer -> {com}")
print(f"<----- User -> {user}")


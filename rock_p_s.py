from random import randint
t=['Rock','Paper','Scissors']
computer=t[randint(0,2)]
player=False
while player==False:
    player=input("Rock,Paper,Scissors?")
    if player==computer:
        print("Tie!")
    elif player=="Rock" or player=="rock":
        if computer=="paper":
            print("You lose!",computer,"covers",player)
        else:
            print("You win!",player,"smashes",computer)
    elif player=="Paper" or player=="paper":
        if computer=="Scissors":
            print("You lose!",computer,"cut",player)
        else:
            print("You win!",player,"covers",computer)
    elif player=="Scissors" or player =="scissors":
        if computer=="Rock":
            print("You lose...",computer,"smashes",player)
        else:
            print("You win!",player,"cut",computer)
    else:
        print("That's not a valid play.Check your spelling!")
    player=False
    computer=t[randint(0,2)]
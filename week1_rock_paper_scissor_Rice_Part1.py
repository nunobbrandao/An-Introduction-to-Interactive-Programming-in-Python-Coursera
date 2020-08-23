import random

def name_to_number(name):
    if name == "rock":
        number=0
    elif name == "Spock":
        number=1
    elif name == "paper":
        number=2
    elif name == "lizard":
        number=3
    elif name == "scissors":
        number = 4
    else:
        number = "Error: name is not supported"
    return number

def number_to_name(number):
    if number == 0:
        name="rock"
    elif number ==1:
        name="Spock"
    elif number ==2 :
        name="paper"
    elif number == 3:
        name="lizard"
    elif number == 4:
        name = "scissors"
    else:
        name = "Error: number btn 0 and 4 (inclusive)"
    return name

def rpsls(name):
    player=name_to_number(name)
    computer=random.randint(0, 4)
    print "Player has chosen", name
    print "Computer has chosen" , number_to_name(computer)
    if (player-computer)%5 == 0:
        print "Player and computer tied"
        print " "
    elif (player-computer)%5 <=2:
        print "Player wins"
        print " "
    else:
        print "Computer wins"
        print " "
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



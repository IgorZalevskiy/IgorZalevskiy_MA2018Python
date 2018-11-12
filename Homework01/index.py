import random
print("Game RSPLS\n")


def name_to_number(name):
    if name == "rock":
        name = 0
        return name
    elif name == "Spock":
        name = 1
        return name
    elif name == "paper":
        name = 2
        return name
    elif name == "lizard":
        name = 3
        return name
    elif name == "scissors":
        name = 4
        return name
    else:
        return "Error: You have entered an incorrect name."


def number_to_name(number):
    if number == 0:
        number = "rock"
        return number
    elif number == 1:
        number = "Spock"
        return number
    elif number == 2:
        number = "paper"
        return number
    elif number == 3:
        number = "lizard"
        return number
    elif number == 4:
        number = "scissors"
        return number
    else:
        return "Error: Please enter the correct number."


def rpsls(player_choice):
    print ("You chooses"), player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 4)
    comp_choice = number_to_name(comp_number)
    print ("Computer chooses"), comp_choice
    difference = (comp_number-player_number) % 5
    if difference == 1 or difference == 2:
        print ("Computer wins!\n")
    elif difference == 3 or difference == 4:
        print ("You wins!\n")
    elif player_number == comp_number:
        print ("You and computer tie!\n")
    else:
        print ("Error: Something might be wrong!\n")
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

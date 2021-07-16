import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("You are trying to go to The Town of Pearl, your home.")
    print_pause("You approach a crossroad.")


def play_again():
    while True:
        print_pause("Would you like to play again? y/n")
        player_response = input()
        if player_response == 'y':
            play_game()
        elif player_response == 'n':
            print_pause("Okay, goodbye for now!")
            break


def choice(right, left, monster):
    weapons = ["a sword", "a bow and arrow", "a dagger"]
    player_weapon = weapons[random.randint(0, 2)]
    print_pause("You have " + player_weapon + " as your weapon")
    print_pause("Would you like to fight? y/n")
    response = input()
    if response == 'y':
        fight(monster, player_weapon)
    elif response == 'n':
        crossroad(right, left, monster)
    else:
        choice(right, left, monster)


def defeated(monster, player_weapon):
    print_pause("Do you want to retreat for now? y/n")
    p_choice = input()
    if p_choice == 'y':
        print_pause("You fled!")
        retreat(monster, player_weapon)
    else:
        print_pause("You didn't flee, and though you fought well, "
                    "you perish at the hands of the " + monster)
        play_again()


def fight(monster, player_weapon):
    print_pause("You try to fight the " + monster)
    win_lose = [1, 2, 3, 4, 5, 6]
    random_outcome = win_lose[random.randint(0, 5)]
    if random_outcome % 2 == 0 or player_weapon == 'Dagger of Truth':
        print_pause("You were able to beat it with " + player_weapon + "!")
        print_pause("You return to The Town of Pearl!")
        play_again()
    else:
        print_pause("You were unable to beat it with " + player_weapon + ".")
        defeated(monster, player_weapon)


def retreat(monster, player_weapon):
    print_pause("You retreat to a small cavern")
    print_pause("A small glint of light catches your eye")
    print_pause("Imbeded in the wall, you find the Dagger of Truth!")
    print_pause("This is a far better weapon"
                "to fight the " + monster + " with than "
                "your " + player_weapon + ".")
    player_weapon = 'Dagger of Truth'
    fight_again(monster, player_weapon)


def fight_again(monster, player_weapon):
    print_pause("Do you want to go back to try "
                "and fight the " + monster + " again? y/n")
    choice = input()
    if choice == 'y':
        fight(monster, player_weapon)
    elif choice == 'n':
        print_pause("While it pains you to forget "
                    "about going back to your town, you prefer living")
        play_again()
    else:
        fight_again(monster, player_weapon)


def crossroad(right, left, monster):
    print_pause("Please enter the number of the road you want to take")
    print_pause("1. " + right)
    print_pause("2. " + left)
    monsters = ["dragon", "wolf", "ghost"]
    monster = monsters[random.randint(0, 2)]
    player_choice = input()
    if player_choice == '1':
        print_pause("You travel down the road to the " + right)
        print_pause("As you cross the " + right + ", "
                    "you encounter the " + monster + " of the " + right + "!")
        choice(right, left, monster)
    elif player_choice == '2':
        print_pause("You travel down the road to the " + left)
        print_pause("As you cross the " + left + ", "
                    "you encounter the " + monster + " of the " + left + "!")
        choice(right, left, monster)
    else:
        crossroad(right, left, monster)


def play_game():
    intro()
    right_choices = ["mountain", "forest", "valley"]
    left_choices = ["cave", "plains", "tunnel"]
    right = right_choices[random.randint(0, 2)]
    left = left_choices[random.randint(0, 2)]
    print_pause("To your right is a road to the " + right)
    print_pause("To your left is a road to the " + left)
    crossroad(right, left, '')


play_game()

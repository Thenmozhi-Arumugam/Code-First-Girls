# This is a Top Trumps card game using Pokemon API
# Imports
import random
import requests
from pprint import pprint
from time import sleep
import time
import sys

# game aesthetics - delay in printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

# Pokemon Top Trumps card game introduction
name_input = True
delay_print("Hello!")
print("")
name = input("Welcome to Pokemon Top-Trumps Card Game! Please enter your name: ")
while name_input:
    if name == "":
        name = input("Uh..Oh.. Name can't be empty. Please enter your name: ")
    else:
        name_input = False

input((f"""{name}, here's how to play...
              1. Enter number of rounds you would like to play
              2. Choose a pokemon from randomly generated 3 pokemons
              3. Choose the stat you want to compete with
              4. Value of the stat selected will be compared against opponent's
              5. A Win = 2 points!
              ------PRESS ENTER TO CONTINUE-------"""))
print("You will be playing against the Computer")
print("Are you ready...")
sleep(1)
print("3");
sleep(1)
print("2");
sleep(1)
print("1");
sleep(1)
delay_print("Let's begin!");
sleep(1)
print("")


# Defining random pokemon
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience'],
    }

# Defining score count
your_score = 0
opponent_score = 0
game_Count = 0

# Defining main game controls
def run():
    # Rounds
    rounds_input = True
    rounds = input("How many rounds would you like to play? ")
    while rounds_input:
        try:
            rounds = int(rounds)
            while rounds not in range(1, 6):
                try:
                    rounds = int(input("Please enter a number between 1 and 5: "))
                except:
                    print("Value should be a number and between 1 and 5")
            if rounds in range(1, 6):
                time.sleep(1)
                print("")
                rounds_input = False
        except ValueError:
            print("Value should be a number")
            rounds = input("Please enter a number: ")

    for i in range(rounds):
        global your_score
        global opponent_score
        global game_Count
        print("        ")

        delay_print("ROUND " + str(game_Count + 1) + " of " + str(rounds) + " Rounds")

        print("        ")
        random_pokemon_1 = random_pokemon()
        random_pokemon_2 = random_pokemon()
        random_pokemon_3 = random_pokemon()
        pokemon_list = []
        pokemon_list.append(random_pokemon_1['name'])
        pokemon_list.append(random_pokemon_2['name'])
        pokemon_list.append(random_pokemon_3['name'])
        print('Your pokemon choices are: {}, {}, {} '.format(random_pokemon_1['name'], random_pokemon_2['name'], random_pokemon_3['name']))
        pokemon_choose = True
        while pokemon_choose:
            pokemon_choice = input('Which pokemon do you want to use? ')
            pokemon_choice = pokemon_choice.lower()
            if pokemon_choice in pokemon_list:
                pokemon_choose = False
                if pokemon_choice == random_pokemon_1['name']:
                    my_pokemon = random_pokemon_1
                elif pokemon_choice == random_pokemon_2['name']:
                    my_pokemon = random_pokemon_2
                elif pokemon_choice == random_pokemon_3['name']:
                    my_pokemon = random_pokemon_3
            else:
                print("Please enter pokemon within the given choices.")

        # Show Pokemon stats
        print("Pokemon Stats:")
        sleep(1)
        print("Pokemon ID:", my_pokemon["id"]);
        sleep(1)
        print("Pokemon Height", my_pokemon["height"]);
        sleep(1)
        print("Pokemon Weight:", my_pokemon["weight"]);
        sleep(1)
        print("Pokemon Base Experience:", my_pokemon["base_experience"]);
        sleep(1)
                
        stat_list = ['id','height','weight','base_experience']
        stat_choose = True
        while stat_choose:
            stat_choice = input('Which stat do you want to use? (id, height, weight, base_experience): ');
            stat_choice = stat_choice.lower()
            if stat_choice in stat_list:
                stat_choose = False
            else:
                print("Please enter stats in the given list.")
        sleep(1)

        print("""

        """)
        opponent_pokemon = random_pokemon()

        print('The opponent chose {}'.format(opponent_pokemon['name']));
        sleep(1)
        # Show Opponent Pokemon stats
        print("Opponent Pokemon Stats:")
        sleep(1)
        print("Pokemon ID:", opponent_pokemon["id"]);
        sleep(1)
        print("Pokemon Height", opponent_pokemon["height"]);
        sleep(1)
        print("Pokemon Weight:", opponent_pokemon["weight"]);
        sleep(1)
        print("Pokemon Base experience:", opponent_pokemon["base_experience"]);
        sleep(1)

        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]
        if my_stat > opponent_stat:
            your_score += 2
            game_Count += 1
            delay_print("*** You Win! ***")

        elif my_stat < opponent_stat:
            game_Count += 1
            opponent_score += 2
            delay_print("*** You Lose! ***")

        else:
            your_score += 1
            opponent_score += 1
            game_Count += 1
            delay_print("*** It's a Draw! ***")
    print("            ")
    print("Total Games Played:", game_Count);
    sleep(1)
    print("Your Final Score:", your_score);
    sleep(1)
    print("Opponent Score:", opponent_score);
    sleep(1)
    if (your_score > opponent_score):
        print("Congratulations.. You won!")
        sleep(1)
    elif (opponent_score > your_score):
        print("Better Luck Next Time.. You Lost!")
    else:
        print("Both won.. It's a Draw")

run()

# Play again (same number of rounds)
while True:
    print("             ")
    answer = input("Do you want to play again(y/n)? ")
    if answer == "y":
        your_score = 0
        opponent_score = 0
        game_Count = 0
        run()
    elif answer == "n":
        break
print("End Game")
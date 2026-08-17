import pickle
import random

# function for saving sadiator attributes to file
def save_data(sadiator):
    # save data
    with open(f'./character_data/{sadiator.name}.pkl', 'wb') as f:
        pickle.dump(sadiator, f)

# function for loading sadiator attributes to file
def load_data(path):
    # load data
    with open(path, 'rb') as f:
        return pickle.load(f)

# actually restores the load data
def load_character(name):
    return load_data(f'./character_data/{name}.pkl')

# used to check for records
def record_check(path, new):
    with open(path, 'r') as f:
        old = f.readline()
        old = int(old)
        
        # write new value
        if new > old:
            with open(path, 'w') as f:
                f.write(str(new))

# this is the game
def play_game(player1,player2):

    print(f'starting a new game between {player1.name} and {player2.name}')
    # ensure the players don't have a .card value or .rw value
    player1.card = 0
    player2.card = 0
    player1.rw = 0 
    player2.rw = 0
    
    # stalemate == players have equal valued cards
    stalemate = 0 
    
    # tracks total rounds per game
    rounds = 0

    # control flow
    light = False
    
    while not light:

        # give each player a 'card'
        player1.card = random.randint(1,10)
        player2.card = random.randint(1,10)
        print(f'{player1.name} has a {player1.card}')
        print(f'{player2.name} has a {player2.card}')

        # see who has larger value
        if player1.card > player2.card:
            player1.rw += 1
            print(f'{player1.name} = {player1.rw} rounds won')

            rounds += 1

            if player1.rw == 2:
                print(f'{player1.name} wins.')
                player1.wins += 1
                player2.losses += 1

                light = True

        if player2.card > player1.card:
            player2.rw += 1
            print(f'{player2.name} = {player2.rw} rounds won')
            
            rounds += 1

            if player2.rw == 2:
                print(f'{player2.name} wins.')
                player2.wins += 1
                player1.losses += 1

                light = True

        # stalemate
        if player1.card == player2.card:

            stalemate += 1
            rounds += 1

            print(f'players had equal cards...')

    return rounds, stalemate

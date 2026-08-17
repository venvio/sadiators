import functions as f

s_path = './data/most_stalemates.txt'
r_path = './data/most_rounds.txt'

# load sadiator objects
joshua = f.load_character('joshua')
walt = f.load_character('walt')

# play the game
# returns number of rounds and stalemates (players had equal cards)
rounds, stalemates = f.play_game(joshua, walt)

# check for records
f.record_check(s_path, stalemates)
f.record_check(r_path, rounds)

# save the data
f.save_data(joshua)
f.save_data(walt)

with open('./data/wins.txt', 'w') as w:
    w.write(f'Joshua wins: {joshua.wins}\n')
    w.write(f'Walt wins: {walt.wins}\n')

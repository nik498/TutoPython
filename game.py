from random import choice

# valid_choices = ['scissors', 'rock', 'paper']

winning_cases = {
    'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

name = input("Enter your name:")
print("Hello, {}".format(name))
rating_file = open('rating.txt', 'r')
user_rating = 0
for line in rating_file:
    line_list = line.split()
    if name == line_list[0]:
        user_rating = int(line_list[1].rstrip('\n'))

options = input().split(',')
if(len(options)) < 2:
    options = ['rock', 'paper', 'scissors']

print("Okay, let's start")

continue_game = True

while continue_game:
    user_choice = input()
    computer_choice = choice(list(options))

    if user_choice == '!exit':
        print('Bye!')
        continue_game = False
        break
    elif user_choice == '!rating':
        print('Your rating: {}'.format(user_rating))
        continue
    elif user_choice not in options:
        print('Invalid input')
        continue

    if user_choice == computer_choice:
        print(f'There is a draw ({user_choice})')
        user_rating += 50
    elif computer_choice not in winning_cases[user_choice]:
        print(f'Sorry, but the computer chose {computer_choice}')
    else:
        print(f'Well done. The computer chose {computer_choice} and failed')
        user_rating += 100

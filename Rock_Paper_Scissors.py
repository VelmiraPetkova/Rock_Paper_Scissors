import random

move = ("rock", "paper", "scissors")
rock = 1
paper = 2
scissors = 3

draw = "Draw!"
player_wins = "You win!"
computer_wins = "You lose!"
result = 0

print(f'Are you ready for play?')
print(f'You can choose move: r-for rock, p-for paper and s-for scissors')


player_choose = input()
player_choose=player_choose.lower()
player_move = " "
while player_choose not in ('r','p','s'):
    print("Invalid selection!!! Try again:")
    print(f'You can choose move: r-for rock, p-for paper and s-for scissors')
    player_choose = input()
    player_choose = player_choose.lower()

if player_choose == 'r':
    player_move = rock ##1
elif player_choose == 'p':
    player_move = paper ##2
elif player_choose == 's':
    player_move = scissors ##3

computer_random_move = random.randint(1,3)
print(f'Computer choose: {move[computer_random_move - 1]}')

if player_move == 1 and computer_random_move == 3:
    result = player_wins
elif player_move == 3 and computer_random_move == 1:
    result = computer_wins
elif player_move == computer_random_move:
    result = draw
elif player_move > computer_random_move:
    result = player_wins
else:
    result = computer_wins

print(result)

import random
user_wins = 0
computer_wins = 0

print("Kon'nichiwa")

options = ['rock','paper','scissors']

while True:
    user_input = input('type: Rock/Parper/Scissors or Q to Quit..').lower()
    if user_input == 'q':
        print('you Quit')
        break
    if user_input not in['rock','paper','scissors']:
        print('You can only enter- Rock/Parper/Scissors')
        continue

    random_number = random.randint(0,2)
    # rock:0, paper:1, scissor:2

    computer = options[random_number]
    print('computer picked',computer +'..')

    if user_input == 'rock' and computer == 'scissors':
        print('you won :)')
        user_wins += 1
    
    elif user_input == 'paper' and computer == 'rock':
        print('you won :)')
        user_wins += 1
    
    elif user_input == 'scissors' and computer == 'paper':
        print('you won :)')
        user_wins += 1

    elif user_input == computer :
        print("It's a tie ")    
    
    else :
        print('You lost :(')
        computer_wins += 1


print('you won',user_wins,'times')
print('computer won',computer_wins,'times')
print('sayonara')


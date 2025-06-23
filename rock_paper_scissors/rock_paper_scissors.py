import random

print('===================')
print('Rock Paper Scissors')
print('===================')
print()
print()
print('1) ✊')
print('2) ✋')
print('3) ✌️')

number = int(input('Choose a number!! '))

numberRobot = random.randint(1, 3)

win = "You Win!! "
lose = "You lose!! "
draw = "It's a draw!! "
choices = {1: '✊', 2: '✋', 3: '✌️'}


if number == numberRobot:
    print(draw)
elif (number == 1 and numberRobot == 3) or (number == 2 and numberRobot == 1) or (number == 3 and numberRobot == 2):
    print(win)
else:
    print(lose)
    
print(f'Robot chose: {choices[numberRobot]}')
print(f'You chose: {choices[number]}')

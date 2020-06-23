import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you you see 2 caves. In one cave, the dragon is friendly and will share his treasure with you. In the other cave the dragon is hungry and greedy and will eat you on site.''')
    print()

def chooseCave():
        cave = ''
        while cave != '1' and cave != '2':
            print('Which cave do you want to go into? (1 or 2)')
            cave = input()

        return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('it is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaw and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
       print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again (yes or no)')
    playAgain = input()
"""
Import random function and declare global symbol
variables for the game.
"""

import random
symbols = ['€', '£', '$']
# taxman = ['@']

# """
# Set wallet variable for new game and establish main game
# infinite while loop to ensure the program runs continuously
# after each successful game/execution.
# Output user info and instructions
# """

# while True:

wallet = 100

print('The Python ONE ARM BANDIT\n')
print()
print('(Orig. US,gambling) A gaming machine\n')
print('having a long arm-like handle at one\n')
print('side that a player pulls down to make\n')
print('reels spin; the player wins money or\n')
print('tokens when certain combinations of\n')
print('symbols line up on these reels.\n')
print()
print('AKA: Fruit machine, slot machine\n')
print()
print('• https://en.wiktionary.org/wiki/\n')
print('  one-armed_bandit\n')
print()
print('****************************************\n')
print('MATCH THREE SYMBOLS:\n')
print('£££ / $$$ / €€€\n')
print('WIN wager x 3!!!\n')
print()
print('MATCH TWO SYMBOLS:\n')
print('££- / $$- / €€- and -££ / -$$ / -€€\n')
print('WIN wager x 2!!\n')
print()
username = input('What is your name? ')
print()
print(f'Hey {username}, you have {wallet} credits in your wallet!\n')
print('Minimum wager is 1 credit.\n')

while wallet > 0:
    try:
        wager = int(input('How much do you want to wager? \n'))
    except:
        print('Please wager a whole number of credits.\n')
        continue
    if wager > wallet:
        print(f'Sorry {username}, insufficient credits!\n')
        continue
    else:
        wallet -= wager
        reel_1 = random.choice(symbols)
        reel_2 = random.choice(symbols)
        reel_3 = random.choice(symbols)
    
    print(f'     |{random.choice(symbols)}|{random.choice(symbols)}|{random.choice(symbols)}|')
    print(f' WIN•|{reel_1}|{reel_2}|{reel_3}|•LINE')
    print(f'     |{random.choice(symbols)}|{random.choice(symbols)}|{random.choice(symbols)}|\n')

    if reel_1 == reel_2 and reel_2 == reel_3:
        winnings = wager * 3
        print(f'Awesome, you matched three and won {winnings} credits!\n')
        wallet += winnings
    elif reel_1 == reel_2 or reel_2 == reel_3:
        winnings = wager * 2
        print(f'Not bad, you matched two and won {winnings} credits!\n')
        wallet += winnings
    else:
        print('Unlucky, you lost that spin.\n')
    print('********************')
    print()
    print(f'You have {wallet} credits.\n')

print(f"Sorry {username}, you're broke :(\n")
print('Thank you for playing\n')

"""
Import random function and declare global symbol
variables for the game.
"""

import random
symbols = ['€', '£', '$', '¥']
# taxman = ['@']

# """
# Set wallet variable for new game and establish main game
# infinite while loop to ensure the program runs continuously
# after each successful game/execution.
# Output user info and instructions
# """

while True:

    wallet = 100

    print()
    print('############################• T H E   P Y T H O N •############################')
    print('#                                                                             #')
    print('#   #     ##   ###   #   #  ####  ###     ###    ##   #  #  ###   ###  #####  #')
    print('#  ##    #  #  #  #  ## ##  #     #  #    #  #  #  #  ## #  #  #   #     #    #')
    print('#   # ## ####  ###   # # #  ###   #  #    ###   ####  # ##  #  #   #     #    #')
    print('#   #    #  #  #  #  #   #  #     #  #    #  #  #  #  #  #  #  #   #     #    #')
    print('#  ###   #  #  #  #  #   #  ####  ###     ###   #  #  #  #  ###   ###    #    #')
    print('#                                                                             #')
    print('###############################################################################')
    print()
    print('  https://en.wiktionary.org/wiki/one-armed_bandit:')
    print()
    print('  From one-armed (“having only one arm”) + bandit (“one who robs others in')
    print('  a lawless area, especially as part of a group; one who cheats others”),')
    print('  referring to the fact that the machine is operated by a single handle')
    print('  and “steals” money from losing players.')
    print()
    print('  (Orig. US, gambling) A gaming machine having a long arm-like handle at one')
    print('  side that a player pulls down to make reels spin; the player wins money or')
    print('  tokens when certain combinations of symbols line up on these reels.')
    print()
    print('  AKA: Fruit machine, poker machine/pokie/pokie machine, slot machine')
    print()
    print('•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
    print('  MATCH THREE SYMBOLS:    •   MATCH TWO SYMBOLS:')
    print('  €€€ / £££ / $$$ / ¥¥¥   •   €€- / ££- / $$- / ¥¥- or -€€ / -££ / -$$ / -¥¥')
    print('  WIN WAGER x3!           •   WIN WAGER x2!')
    print('•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
    print()
    username = input("  What's your name? ")
    print()
    print(f'                Hey {username}, you have {wallet} credits in your wallet!')
    print('                          Minimum wager is 1 credit.')
    print()

    while wallet > 0:
        try:
            wager = int(input('                     How much would you like to wager..? '))
        except:
            print('                     Please wager a whole number of credits.\n')
            continue
        if wager > wallet:
            print(f'                    Sorry {username}, insufficient credits!\n')
            continue
        else:
            wallet -= wager
            reel_1 = random.choice(symbols)
            reel_2 = random.choice(symbols)
            reel_3 = random.choice(symbols)
        
        print()
        print('                        ••••••••••••••••••••••••••••••')
        print(f'                       •        | {random.choice(symbols)} | {random.choice(symbols)} | {random.choice(symbols)} |         •')
        print('                      •         —————————————          •')
        print(f'                     •    WIN • | {reel_1} | {reel_2} | {reel_3} | • LINE    •')
        print('                      •         —————————————          •')
        print(f'                       •        | {random.choice(symbols)} | {random.choice(symbols)} | {random.choice(symbols)} |         •')
        print('                        ••••••••••••••••••••••••••••••')
        print()


        if reel_1 == reel_2 and reel_2 == reel_3:
            winnings = wager * 3
            print(f'                Awesome, you matched three and won {winnings} credits!')
            wallet += winnings
        elif reel_1 == reel_2 or reel_2 == reel_3:
            winnings = wager * 2
            print(f'                 Not bad, you matched two and won {winnings} credits!')
            wallet += winnings
        else:
            print('                         Unlucky, you lost that spin.')
        print()
        print(f'                             You have {wallet} credits.')

    print(f"             Sorry {username}, you're broke! :( Thank you for playing.")


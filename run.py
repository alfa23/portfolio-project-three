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
    print(
          '    #########• T H E   P Y T H O N •#########\n'
          '    #                                       #\n'
          '    #   #     ##   ###   #   #  ####  ###   #\n'
          '    #  ##    #  #  #  #  ## ##  #     #  #  #\n'
          '    #   # ## ####  ###   # # #  ###   #  #  #\n'
          '    #   #    #  #  #  #  #   #  #     #  #  #\n'
          '    #  ###   #  #  #  #  #   #  ####  ###   #\n'
          '    #                                       #\n'
          '    #  ###    ##   #   #  ###   ###  #####  #\n'
          '    #  #  #  #  #  ##  #  #  #   #     #    #\n'
          '    #  ###   ####  # # #  #  #   #     #    #\n'
          '    #  #  #  #  #  #  ##  #  #   #     #    #\n'
          '    #  ###   #  #  #   #  ###   ###    #    #\n'
          '    #                                       #\n'
          '    #########################################\n')
    print()
    print('  https://en.wiktionary.org/wiki/one-armed_bandit:')
    print()
    print('  From one-armed (“having only one arm”) + bandit (“one\n'
          '  who robs others in a lawless area, especially as part\n'
          '  of a group; one who cheats others”),referring to the\n'
          '  fact that the machine is operated by a single handle\n'
          '  and “steals” money from losing players.\n')
    print()
    print('  (Orig. US, gambling) A gaming machine having a long\n'
          '  arm-like handle at one side that a player pulls down to\n'
          '  make reels spin; the player wins money or tokens when\n'
          '  certain combinations of symbols line up on these reels.\n')
    print()
    print('  AKA: Fruit machine, poker machine, slot machine')
    print()
    print('•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n')
    print('  MATCH TWO SYMBOLS:')
    print('  €€- / ££- / $$- / ¥¥- or -€€ / -££ / -$$ / -¥¥')
    print('  WIN WAGER x2!')
    print()
    print('  MATCH THREE SYMBOLS:')
    print('  €€€ / £££ / $$$ / ¥¥¥')
    print('  WIN WAGER x3!')
    print('•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n')
    print()
    username = input("  What's your name? ")
    print()
    print(f'  Hey {username}, you have {wallet} credits in your wallet!')
    print('  Minimum wager is 1 credit.')
    print()

    while wallet > 0:
        try:
            wager = int(input('  How much would you like to wager..? '))
        except:
            print('  Please wager a whole number of credits.\n')
            continue
        if wager > wallet:
            print(f'  Sorry {username}, insufficient credits!\n')
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
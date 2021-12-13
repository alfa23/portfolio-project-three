"""
Import random function and declare global symbol
variables for the game.
"""

import random
symbols = ["€", "£", "$", "¥"]

"""
Set wallet variable for new game and establish main game
infinite while loop to ensure the program runs continuously
after each successful game/execution.
Output user info and instructions
"""


def introduction():
    """
    This method is called when an
    introduction is required
    """
    print()
    print(
          "    #########• T H E   P Y T H O N •#########\n"
          "    #                                       #\n"
          "    #   #     ##   ###   #   #  ####  ###   #\n"
          "    #  ##    #  #  #  #  ## ##  #     #  #  #\n"
          "    #   # ## ####  ###   # # #  ###   #  #  #\n"
          "    #   #    #  #  #  #  #   #  #     #  #  #\n"
          "    #  ###   #  #  #  #  #   #  ####  ###   #\n"
          "    #                                       #\n"
          "    #  ###    ##   #   #  ###   ###  #####  #\n"
          "    #  #  #  #  #  ##  #  #  #   #     #    #\n"
          "    #  ###   ####  # # #  #  #   #     #    #\n"
          "    #  #  #  #  #  #  ##  #  #   #     #    #\n"
          "    #  ###   #  #  #   #  ###   ###    #    #\n"
          "    #                                       #\n"
          "    #########################################\n")
    print(" https://en.wiktionary.org/wiki/one-armed_bandit:\n")
    print(' From one-armed (“having only one arm”) + bandit (“one\n'
          ' who robs others in a lawless area, especially as part\n'
          ' of a group; one who cheats others”),referring to the\n'
          ' fact that the machine is operated by a single handle\n'
          ' and “steals” money from losing players.\n')
    print(" (Orig. US, gambling) A gaming machine having a long\n"
          " arm-like handle at one side that a player pulls down to\n"
          " make reels spin; the player wins money or tokens when\n"
          " certain combinations of symbols line up on these reels.\n")
    print(" AKA: Fruit machine, poker machine, slot machine.\n")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n"
          " MATCH TWO SYMBOLS:\n"
          " €€- / ££- / $$- / ¥¥- or -€€ / -££ / -$$ / -¥¥\n"
          " WIN WAGER x2!\n")
    print(" MATCH THREE SYMBOLS:\n"
          " €€€ / £££ / $$$ / ¥¥¥\n"
          " WIN WAGER x3!\n"
          "•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n")
    username = input("What's your name? \n")

    return username


# def get_leaderboard():


def game(username: str, wallet: int = 100):
    """
    Method to hold the running game
    Default wallet value = 100
    Sets number of plays and max credits held
    variables to 0 for each new game
    """
    while True:
        plays = 0
        max_credits = 0

        while wallet > 0:
            print()
            print(f"Hey {username}, you have {wallet} credits "
                  "in your wallet!\n"
                  "Minimum wager is 1 credit.\n")
            try:
                wager = int(input("How much would you like to wager..? \n"))
            except ValueError:
                print("Please wager a whole number of credits.\n")
                continue
            if wager > wallet:
                print(f"Sorry {username}, insufficient credits!\n")
                continue
            elif wager < 0:
                print("Please enter a positive number")
            else:
                plays += 1
                wallet -= wager
                reel_1 = random.choice(symbols)
                reel_2 = random.choice(symbols)
                reel_3 = random.choice(symbols)

            print()
            # print(f"             {plays}")
            print("   ••••••••••••••••••••••••••••••")
            print(f"  •        | {random.choice(symbols)} "
                  f"| {random.choice(symbols)} |"
                  f" {random.choice(symbols)} |         •")
            print(" •         —————————————          •")
            print(f"•    WIN • | {reel_1} | {reel_2} | {reel_3} | • LINE    •")
            print(" •         —————————————          •")
            print(f"  •        | {random.choice(symbols)} "
                  f"| {random.choice(symbols)} |"
                  f" {random.choice(symbols)} |         •")
            print("   ••••••••••••••••••••••••••••••")
            print()

            if reel_1 == reel_2 and reel_2 == reel_3:
                winnings = wager * 3
                print(f"Awesome, you matched three and won"
                      f" {winnings} credits!\n")
                wallet += winnings
            elif reel_1 == reel_2 or reel_2 == reel_3:
                winnings = wager * 2
                print(f"Not bad, you matched two and won"
                      f" {winnings} credits!\n")
                wallet += winnings
            else:
                print("Unlucky, you lost that spin.\n")

            if wallet > max_credits:
                max_credits = wallet

            print(f"You have played {plays} games and held a maximum of "
                  f"{max_credits} credits...\n")

        print(f"Sorry {username}, you're broke! :(\n")

        choices = input("Please choose...\n"
                        "1 to play again\n"
                        "2 to see Leaderboard\n"
                        "3 to quit playing\n")

        for choice in choices:
            if choice == "1":
                game(username)
            elif choice == "2":
                print("get_leaderboard()")
                # get_leaderboard()
                break
            elif choice == "3":
                print()
                print(f"Thanks for playing, {username}!\n")
                main()
            else:
                print()
                print("Please enter 1, 2, or 3!\n")
                continue

    return None


def main():
    """
    Method to hold all above functions / methods
    """
    wallet = 100
    username = introduction()
    game(username, wallet)


if __name__ == "__main__":
    # Call main function if this file is the entry point
    main()

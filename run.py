"""
Import random function.
Import regular expressions (re) for username check.
Import gspread and google-auth packages to access &
update best_players records.
Set constant vars for SCOPE, CREDS, GSPREAD_CLIENT and
SHEET to access Google Sheets data (process & code
copied & modified from Love Sandwiches project.)
Declare global symbol vars for the game.
"""

import re
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_bandits')
SYMBOLS = ["€", "£", "$", "¥"]


def get_username():
    """
    Fuction to collect and verify username
    when required (new game start).
    """
    introduction()
    while True:
        username = input("Enter your name to play "
                         "(max. 8 characters): \n")
        if not re.match("^[A-Z, a-z]*$", username):
            print("\nError! Only letters allowed!\n")
            continue
        elif len(username) < 1 or len(username) > 8:
            print("\nError! 1-8 letters required!\n")
            continue
        else:
            break

    return username


def introduction():
    """
    This method is called when an introduction
    is required (new game start).
    """
    print("\n        ...ENUMERATING SCORES DATABASE...\n")
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


def get_best_players(username):
    """
    Function to access python_bandits Google sheet and
    keep track of user scores for best players data.
    """
    scoreboard = SHEET.worksheet('scoreboard')
    data = scoreboard.get_all_records()

    # Access gsheet, reverse-sort by maxcredits, assign hi_scorer name & score.
    hi_score = sorted(data, key=lambda i: i['maxcredits'], reverse=True)
    hi_scorer = next(iter(hi_score))
    hs_name = hi_scorer['username']
    hs_credits = hi_scorer['maxcredits']

    # Output hi_scorer data.
    print()
    print(" * ALL-TIME BEST BANDIT BEATERS *")
    print()
    print(f"{hs_name} has amassed the biggest wallet, with"
          f" {hs_credits} credits held!\n")

    # Access gsheet, reverse-sort by #turns, assign long_player name & score.
    play_streak = sorted(data, key=lambda i: i['turns'], reverse=True)
    long_player = next(iter(play_streak))
    lp_name = long_player['username']
    lp_turns = long_player['turns']

    # Output long_player data, inform user their score is saved.
    print(f"{lp_name} has the longest play streak, with"
          f" {lp_turns} games played!\n"
          "\nThe scores database has been updated with your"
          " latest score...\n")

    # End-of-game user choices & validation.
    choices = input("Please choose...\n"
                    "1 to play again\n"
                    "2 to quit playing\n")

    for choice in choices:
        if choice == "1":
            game(username)
        elif choice == "2":
            print()
            print(f"Thanks for playing, {username}!\n")
            main()
        else:
            print()
            print("Please enter a valid response!\n")
            continue


def game(username: str, wallet: int = 100):
    """
    Method to hold the running game.
    Default wallet value = 100.
    Sets number of turns and max credits held variables
    to 0 for each new game.
    """
    while True:
        turns = 0
        maxcredits = 0

        while wallet > 0:
            print()
            print(f"Hey {username}, you have {wallet} credits "
                  "in your wallet!\n"
                  "Minimum wager is 10 credits.\n")
            try:   # Integer wager value input from user & validate.
                wager = int(input("How much would you like to wager..? \n"))
            except ValueError:
                print("Please wager a whole number of credits.\n")
                continue
            if wager > wallet:   # Check credits available.
                print("Insufficient credits!\n")
                continue
            elif wager < 0:   # Check wager is +ve.
                print("Please enter a positive number!\n")
                continue
            elif wager < 10:   # Check minimum wager value met.
                print("Minimum wager is 10 credits!\n")
                continue
            else:   # Increment turns & deduct wager from wallet.
                turns += 1
                wallet -= wager
                reel_1 = random.choice(SYMBOLS)
                reel_2 = random.choice(SYMBOLS)
                reel_3 = random.choice(SYMBOLS)

            # Spin the reels!
            print()
            print("   ••••••••••••••••••••••••••••••")
            print(f"  •        | {random.choice(SYMBOLS)} "
                  f"| {random.choice(SYMBOLS)} |"
                  f" {random.choice(SYMBOLS)} |         •")
            print(" •         —————————————          •")
            print(f"•    WIN • | {reel_1} | {reel_2} | {reel_3} | • LINE    •")
            print(" •         —————————————          •")
            print(f"  •        | {random.choice(SYMBOLS)} "
                  f"| {random.choice(SYMBOLS)} |"
                  f" {random.choice(SYMBOLS)} |         •")
            print("   ••••••••••••••••••••••••••••••")
            print()

            # Check result, calc winnings & update wallet as required.
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

            # Check and update maxcredits value as required.
            if wallet > maxcredits:
                maxcredits = wallet

            print(f"You have played {turns} games and held a maximum of "
                  f"{maxcredits} credits...\n")

        print(f"\nSorry {username}, you're broke! :(\n")

        # Collate user data for current game & append to gsheet.
        user_score = [username, maxcredits, turns]
        scoreboard = SHEET.worksheet("scoreboard")
        scoreboard.append_row(user_score)

        # End-of-game user choices & validation.
        choices = input("Please choose...\n"
                        "1 to play again\n"
                        "2 to see best players\n"
                        "3 to quit playing\n")

        for choice in choices:
            if choice == "1":
                game(username)
            elif choice == "2":
                get_best_players(username)
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
    Method to hold all above functions / methods.
    """
    wallet = 100
    username = get_username()
    game(username, wallet)


if __name__ == "__main__":
    # Call main function if this file is the entry point.
    main()

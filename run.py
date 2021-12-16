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

# External libraries imported to enhance program functionality
import re
import random
import gspread
from google.oauth2.service_account import Credentials

# SCOPE code & constants ammended & borrowed from Love Sandwiches
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

"""
All code below originated by Paul Whiteside. Any external
references & exceptions are detailed in the project README.md
"""


def get_username():
    """
    Fuction to collect and verify username
    when required (new game start).
    """
    introduction()
    while True:
        username = input("\033[1;34mEnter your name to play "
                         "(max. 8 letters): \n\033[0;0m")
        # Following if statement code repurposed from a Stack Overflow thread
        if not re.match("^[A-Z, a-z]*$", username):   # See README for details
            print("\n\033[1;31mError! Only letters allowed!\n\033[0;0m")
            continue
        elif len(username) < 1 or len(username) > 8:
            print("\n\033[1;31mError! 1-8 letters required!\n\033[0;0m")
            continue
        else:
            break

    return username


def introduction():
    """
    This method is called when an introduction
    is required (new game start).
    """
    print(
          "\n\033[1;34m    #########• T H E   P Y T H O N •#########\n"
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
          "    #########################################\n\033[0;0m")
    empty_input = input("\033[3;34m           > Press enter to "
                        "continue >\n\033[0;0m")
    print(" \033[4;33mhttps://en.wiktionary.org/wiki/one-armed_bandit:\n")
    print('\033[0;33m From one-armed (“having only one arm”) + bandit (“one\n'
          ' who robs others in a lawless area, especially as part\n'
          ' of a group; one who cheats others”),referring to the\n'
          ' fact that the machine is operated by a single handle\n'
          ' and “steals” money from losing players.\n')
    print(" (Orig. US, gambling) A gaming machine having a long\n"
          " arm-like handle at one side that a player pulls down to\n"
          " make reels spin; the player wins money or tokens when\n"
          " certain combinations of symbols line up on these reels.\n")
    print("\033[3;33m AKA: Fruit machine, poker machine,"
          " slot machine.\n\033[0;0m")
    empty_input = input("\033[3;34m           > Press enter to "
                        "continue >\n\033[0;0m")
    print("\033[1;34m••••••••••••••••••••••••••••••••••••"
          "•••••••••••••••••••••••\n"
          " MATCH TWO SYMBOLS:\n"
          "\033[1;32m €€- / ££- / $$- / ¥¥-\033[3;34m  or  \033[0;0m"
          "\033[1;32m-€€ / -££ / -$$ / -¥¥\n"
          "\033[1;34m WIN WAGER x2!\n")
    print(" MATCH THREE SYMBOLS:\n"
          " \033[1;32m€€€ / £££ / $$$ / ¥¥¥\n"
          "\033[1;34m WIN WAGER x3!\n"
          "•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n"
          "••••••••••••••••\033[1;32mENUMERATING SCORES DATABASE"
          "\033[1;34m••••••••••••••••\n\033[0;0m")

    return empty_input


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
    print("\033[1;34m * ALL-TIME BEST BANDIT BEATERS *")
    print()
    print(f"\033[1;33m{hs_name} has amassed the biggest wallet, with"
          f" {hs_credits} credits held!\n")

    # Access gsheet, reverse-sort by #turns, assign long_player name & score.
    play_streak = sorted(data, key=lambda i: i['turns'], reverse=True)
    long_player = next(iter(play_streak))
    lp_name = long_player['username']
    lp_turns = long_player['turns']

    # Output long_player data. Inform user their score is saved.
    print(f"{lp_name} has the longest play streak, with"
          f" {lp_turns} games played!\n\033[0;0m"
          "\n\033[1;32mThe scores database has been updated with your"
          " latest score...\n\033[0;0m"
          "\n\033[1;34mPlay some more and try to beat the all-time"
          " scores!\n\033[0;0m")

    # End-of-game user choices & validation.
    choice = input("Please enter...\n"
                   " \n"
                   "1 \033[1;34mto play again\n\033[0;0m"
                   "2 \033[1;34mto quit playing\n\033[0;0m")
    while choice not in ["1", "2"]:
        print()
        print("\033[1;31mPlease enter a valid response!\n\033[0;0m")
        break
    if choice == "1":
        game(username)
    elif choice == "2":
        print()
        print(f"\033[0;33mThanks for playing, {username}!\n\033[0;0m")
        main()


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

        while wallet > 0:   # Continuous loop while user has credit.
            print()   # Greet user and inform them of the game conditions.
            print(f"\033[0;33mHey {username}, you have {wallet} credits "
                  "in your wallet!\n"
                  "Minimum wager is 10 credits.\n\033[0;0m")
            try:   # Get wager integer value from user input & validate.
                wager = int(input("How much would you like to wager..? \n"))
            except ValueError:   # Check wager is a whole number.
                print("\033[1;31mPlease wager a whole number "
                      "of credits.\n\033[0;0m")
                continue
            if wager > wallet:   # Check credits are available.
                print("\033[1;31mInsufficient credits!\n\033[0;0m")
                continue
            elif wager < 0:   # Check wager is +ve.
                print("\033[1;31mPlease enter a positive number!\n\033[0;0m")
                continue
            elif wager < 10:   # Check minimum wager value is met.
                print("\033[1;31mMinimum wager is 10 credits!\n\033[0;0m")
                continue
            else:   # Increment turns/deduct wager from wallet/randomise reels.
                turns += 1
                wallet -= wager
                reel_1 = random.choice(SYMBOLS)
                reel_2 = random.choice(SYMBOLS)
                reel_3 = random.choice(SYMBOLS)

            # Spin the reels! Output randomised reels result.
            print()
            print("\033[1;34m   ••••••••••••••••••••••••••••••")
            print(f"  •        | {random.choice(SYMBOLS)} "
                  f"| {random.choice(SYMBOLS)} |"
                  f" {random.choice(SYMBOLS)} |         •")
            print(" •         —————————————          •")
            print(f"•\033[0;0m    WIN • | {reel_1} | {reel_2} "
                  f"| {reel_3} | • LINE    \033[1;34m•")
            print(" •         —————————————          •")
            print(f"  •        | {random.choice(SYMBOLS)} "
                  f"| {random.choice(SYMBOLS)} |"
                  f" {random.choice(SYMBOLS)} |         •")
            print("   ••••••••••••••••••••••••••••••\033[0;0m")
            print()

            # Check result, calc winnings & update wallet as required.
            if reel_1 == reel_2 and reel_2 == reel_3:
                winnings = wager * 3
                print(f"\033[1;32mAwesome, you matched three and won"
                      f" {winnings} credits!\n\033[0;0m")
                wallet += winnings
            elif reel_1 == reel_2 or reel_2 == reel_3:
                winnings = wager * 2
                print(f"\033[1;36mNot bad, you matched two and won"
                      f" {winnings} credits!\n\033[0;0m")
                wallet += winnings
            else:
                print("\033[1;31mUnlucky, you lost that spin.\n\033[0;0m")

            # Check and update maxcredits value as required.
            if wallet > maxcredits:
                maxcredits = wallet

            # Keeps user informed of game progress.
            if turns > 1:
                print(f"\033[1;33mYou have played {turns} games and held a "
                      f"maximum of {maxcredits} credits...\n\033[0;0m")
            else:
                print(f"\033[1;33mYou have played {turns} game and held a "
                      f"maximum of {maxcredits} credits...\n\033[0;0m")

        # End-of-game message.
        print(f"\n\033[1;33mSorry {username}, you're broke! :(\n\033[0;0m")

        # Collate user data for current game & append to gsheet.
        user_score = [username, maxcredits, turns]
        scoreboard = SHEET.worksheet("scoreboard")
        scoreboard.append_row(user_score)

        # End-of-game user choices & validation.
        choice = input("Please enter...\n"
                       " \n"
                       "1 \033[1;34mto play again\n\033[0;0m"
                       "2 \033[1;34mto see best players\n\033[0;0m"
                       "3 \033[1;34mto quit playing\n\033[0;0m")

        while choice not in ["1", "2", "3"]:
            print()
            print("\033[1;31mPlease enter 1, 2, or 3!\n\033[0;0m")
            break
        if choice == "1":
            game(username)
        elif choice == "2":
            get_best_players(username)
        elif choice == "3":
            print()
            print(f"\033[0;33mThanks for playing, {username}!\n\033[0;0m")
            main()

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

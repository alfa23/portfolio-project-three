# The Python One-Armed Bandit


----


![HEADER LOGO](assets/readme/game_screens/pp03_intro-1_head_gfx.jpg)


Visit the deployed application [here](https://python-bandit.herokuapp.com/).


## Table of Contents


----

- [The Python One-Armed Bandit](#the-python-one-armed-bandit)
  * [Table of Contents](#table-of-contents)
  * [USER EXPERIENCE (UX)](#user-experience--ux-)
    + [External User Goals: User Stories](#external-user-goals--user-stories)
    + [Project Goals](#project-goals)
  * [FLOWCHART](#flowchart)
  * [DESIGN CHOICES](#design-choices)
    + [Colours](#colours)
  * [TECHNOLOGIES](#technologies)
    + [Languages](#languages)
    + [Tools](#tools)
  * [FEATURES](#features)
    + [Introduction & Background Information](#introduction---background-information)
    + [Game Loop](#game-loop)
    + [End-of-Game User Choices](#end-of-game-user-choices)
  * [VERSION CONTROL](#version-control)
    + [Gitpod Workspaces](#gitpod-workspaces)
  * [TESTING](#testing)
    + [Testing Project Goals](#testing-project-goals)
    + [Testing External User Goals & Stories](#testing-external-user-goals---stories)
    + [Code Validation](#code-validation)
    + [Response Testing](#response-testing)
    + [Manual Testing](#manual-testing)
  * [BUGS & FIXES](#bugs---fixes)
    + [**Pressing Enter** during username input wasn't being caught...](#--pressing-enter---during-username-input-wasn-t-being-caught)
  * [DEPLOYMENT](#deployment)
- [CREDITS](#credits)
  * [Content](#content)
    + [Activate API Credentials](#activate-api-credentials)
    + [Connect Project To Worksheet](#connect-project-to-worksheet)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



----


## USER EXPERIENCE (UX) 


### External User Goals: User Stories

- As a user, I want an easy-to-pick-up yet challeging game of chance to pass time online.

- As a user, I want to easily identify the input required for each step.

- As a user, I want to receive clear feedback in the case of erroneous inputs.

- As a user, I want the option to play the game as many times as I wish.

- As a user, I want to try and better the All-Time Bandit Buster score and see my name at the top!

  Additional ***user expectations*** for consideration include:
  - Responsive: access site easily on any device


### Project Goals

- To deploy a command-line application to a cloud-based platform.

- To create an online game of chance that is easy and fun play.

- To ensure the game runs in a smooth loop, allowing users to play as many times as they wish.

- To provide a positive UX by ensuring users are kept informed of their current in-game status.

- To provide a positive UX by ensuring that any user input errors are effectively dealt with.

- To include a process to track/record the best user scores for the game & display the all-time best.


----


## FLOWCHART


![Flowchart](assets/readme/pp03_python_bandit_flowchart_opt.jpg) 

Flowchart generated in [LucidChart](https://lucidchart.com/)


[Back to top ???](#)
---- 


## DESIGN CHOICES


### Colours

To enhance user experience the decision was taken to add colour, which was applied by utilising the built-in ASCI Escape Sequence syntax. White copy was retained for highlighting user input points and the reel win-line.

Other colours used were: 

  ??? **Red - \033[1;31;m** for validation warning messages and losing spins.
  
  ??? **Green - \033[1;32;m** for confirmation messages and x3 winning spins.
  
  ??? **Yellow - \033[1;33;m** for informative text & messages.

  ??? **Blue - \033[1;34;m** for the main logo, 'structural' elements (lines & boxes) and instructive copy.

  ??? **Cyan - \033[1;36;m** for confirmation of x2 winning spins; added to provide slight differentiation from x3 winning spins.

  The value of 1 in the examples above denote bold styling; variations of this value were utilised to achieve different text styles, specifically 3 for italics, 4 for underlines and 0 for resetting (normal-ising) text.

ASCI EscSeq process and syntax informed by & referenced from: https://stackabuse.com/how-to-print-colored-text-in-python/


----


## TECHNOLOGIES

During the course of this project the following technologies were utilised:


### Languages

- [**Python**](https://www.python.org/) was used to build the application


### Tools

- [**Git**](https://git-scm.com/) was used for version control (commit to Git and push to GitHub).

- [**Gitpod**](https://www.gitpod.io/) was used to write the code; an online IDE linked to the GitHub repository.

- [**GitHub**](https://github.com/) was used to create the repository and store the project's code after being pushed from Git.

- [**LucidChart**](https://lucidchart.com/) used to generate project flowchart.

- [**Google Cloud Platform**](https://cloud.google.com/) was used to connect & configure the APIs used in the project; specifically for Google Drive and Google Sheets integration, including generation of the required credentials file (creds.json).

- [**amiresponsive**](http://ami.responsivedesign.is/) was used to check how responsive the application is on different devices.

- [**PEP8**](http://pep8online.com/) **Python Validator** used to validate all Python source code.

- [**Heroku**](https://heroku.com/) used to configure and deploy the final project.


[Back to top ???](#)
----


## FEATURES


### Introduction & Background Information

![Intro Header](assets/readme/game_screens/pp03_intro-1_head_gfx.jpg)

- Chip-art header logo announcing the chosen game of chance - to those users old enough to know the term... Program suspends awaitng user input to continue.


![Intro Copy](assets/readme/game_screens/pp03_intro-2_mid_copy.jpg)

- Wikipedia reference used as explainer for base concept of the game and the application name's origin, for all the rest of those users not old enough to know the term! 

- Program suspends awaitng user input to continue.


![Intro Footer](assets/readme/game_screens/pp03_intro-3_lower.jpg)

- Informs user of the conditions of the game. Introduces the symbol set used to play the game (based on units of currency: ???, ??, $ and ??) and details the winning combinations and their respective rewards. 

  - Added 'Enumerating Scores Database' copy to subtly hint to user that there is a mechanism for recording game scores.

  - Awaits first user input: Enter their name if they want to play...


### Game Loop

![Username & first wager](assets/readme/game_screens/pp03_gameloop-1_name.jpg)

- Successful submission of username (see: Manual Testing) initiates main game loop:

  - User is informed of their starting wallet balance and minimum wager condition (10 credits).

  - Awaits user input of initial wager...
      
  
![The reels](assets/readme/game_screens/pp03_gameloop-2_reels.jpg)

- Successful submission of wager amount (see: Manual Testing) initiates selection of three random 'winning' reels. The user's wallet balance has the wager value deducted and is updated. Turns value is incremented by 1.

  - The random reels result is compared to the winning conditions and, if required, rewards are calculated and ammended to the wallet value. 
  
    - Check if current credits > maxcredits and, if so, update maxcredits value.

  - The random reels are displayed to the user in a simple digital facsimilie of a one-armed bandit's reels with the win-line highlighted in white, out of the surrounding blue.

  
  ![Losing reels](assets/readme/game_screens/pp03_gameloop-2a_loss.jpg)

    - Below losing reels a commiseratory message to the user is displayed in red text.


  ![Win x2 reels](assets/readme/game_screens/pp03_gameloop-3_winx2.jpg)

    - Below x2 win reels a congratulatory message to the user is displayed in cyan text. The wager amount is doubled and ammended to the user's wallet value.


  ![Win x3 reels](assets/readme/game_screens/pp03_gameloop-4_winx3.jpg)

    - Below x3 win reels a congratulatory message to the user is displayed in green text. The wager amount is tripled and ammended to the user's wallet value.


- Yellow text is used to inform the user of current number of games played and maximum credits held.

- Then, while the user still has credits in their wallet, the game loop resets: The user is informed of their updated credit balance, reminded of the minimum wager and asked for their next wager amount. This loop will continues for as long as the user has credits to spin.


[Back to top ???](#)


### End-of-Game User Choices


![You're broke](assets/readme/game_screens/pp03_gameloop-5_broke.jpg)

- When the user eventually runs out of credits, a yellow-text-informative message apologises and lets them know they're broke. 

- Users are then asked to choose from three numbered options: 1, play again; 2, see best players and 3, quit playing.


  ![EoG user choices](assets/readme/game_screens/pp03_gameloop-6_eog_choices.jpg)

  - Successful submission of a choice (see: Manual Testing) initiates:  


  ![EoG play again](assets/readme/game_screens/pp03_gameloop-7_play_again.jpg)

  - **1 to play again** restarts the game loop using the current username, with fresh wallet and turns values. The game will continue infinitely on this main game loop until the user chooses another end-of-game option.


  ![EoG best players](assets/readme/game_screens/pp03_gameloop-8_best_players.jpg)

  - **2 to see best players** displays a simple message informing the player of the username and respective score for the All-Time Bandit Beater biggest wallet held and longest play streak during one game run.
  
  - Each game run this data is pulled & sorted fresh from the google spreadsheet linked to the application, which is also updated with every successfully completed game's username, maxcreds and turns data.
      
    - The user is informed that the scores database has been updated with their latest score and encouraged to play some more to try and beat the all-time bests.

    - An amended choice menu offers appropriate selection of 1 to play again and 2 to quit. 

  After getting the main game & validation sorted and nearing the end of development, I had started experimenting with an enhanced scoreboard feature. However, given the limited time remaining I decided to not try fixing something that wasn't broken, as the current code successfully demonstrates worksheet integration and the potential that APIs offer. 

  ![EoG quit playing](assets/readme/game_screens/pp03_gameloop-9_quit.jpg)

  - **3 to quit playing** (also **2 to quit playing**) displays a message thanking user for playing.

  - The main game loop then ends and a fresh instance of the program is initiated, returning to the opening main logo. 
      

----


## VERSION CONTROL

Managed within **GitHub** and **Gitpod** via regular commits pushed to GitHub remote servers:


### Gitpod Workspaces
1. Starting from GitHub, clone the Code Institute template by clicking Use This Template and copying to my repo. Launch Workspace by clicking GitPod button - this action is only performed once and the workspace is subsequently reopened through GitPod.

2. Start the Gitpod Workspace which opens an online IDE editor window.
    
    - Update GitHub by committing from GitPod

3. During editing save the code regularly, using git add ., git commit -m "commit message here" and git push Bash commands to push changes to the GitHub repository.

4. Meaningful commit messages allow easy roll-back of any changes to earlier versions.


[Back to top ???](#)


## TESTING 

### Testing Project Goals

- To deploy a command-line application to a cloud-based platform.  **PASSED**

  ![App-in-window](assets/readme/game_screens/pp03_app_window.jpg)

- To create an online game of chance that is easy and fun play.  **PASSED**

  ![Simple scoring](assets/readme/game_screens/pp03_feat-1_scoring.jpg)

- To ensure the game runs in a smooth loop, allowing users to play as many times as they wish.  **PASSED**

- To provide a positive UX by ensuring users are kept informed of their current in-game status.  **PASSED**

  ![Game stats](assets/readme/game_screens/pp03_feat-_game_stats.jpg)

- To provide a positive UX by ensuring that any user input errors are effectively dealt with.  **PASSED**

- To include a process to track/record the best user scores for the game & display the all-time best.  **PASSED**

  ![Best players](assets/readme/game_screens/pp03_feat-3_best_players.jpg)



### Testing External User Goals & Stories

- As a user, I want an easy-to-pick-up yet challeging game of chance to pass time online.  **PASSED**

  ![Reels](assets/readme/game_screens/pp03_feat-2_reels.jpg)


- As a user, I want to easily identify the input required for each step.  **PASSED**

- As a user, I want to receive clear feedback in the case of erroneous inputs.  **PASSED**

- As a user, I want the option to play the game as many times as I wish.  **PASSED**

- As a user, I want to try and better the All-Time Bandit Buster score and see my name at the top!  **PASSED**


### Code Validation  **PASSED** 

Python

- No errors were returned when passing through the [PEP8 validator](http://pep8online.com/)

![PEP8 validation screen](assets/readme/grab_screens/pp03_validation_pep8.jpg)


### Response Testing  **PASSED**

In order to test responsiveness to all device sizes, I used [amiresponsive](http://ami.responsivedesign.is/)

![amiresponsive](assets/readme/grab_screens/pp03_validation_amiresponsive.jpg)


### Manual Testing  **PASSED**


| FEATURE | OUTCOME | EXAMPLE | PASS/FAIL |
|---|---|:---:|:---:|
| Validate username inputs (str) | Checks: is not a number; is <8; is>0 | ![Username](assets/readme/mantest_screens/pp03_mantest-1_username_inputs.jpg) | PASS |
| Validate wager inputs (int) | Checks: is not 0; is positive | ![Wager1](assets/readme/mantest_screens/pp03_mantest-2a_wager_inputs.jpg) | PASS |
| Validate wager inputs (int) | Checks: is not a str or float | ![Wager2](assets/readme/mantest_screens/pp03_mantest-2b_wager_inputs.jpg) | PASS |
| Validate wager inputs (int) | Checks: meets min. wager value | ![Wager3](assets/readme/mantest_screens/pp03_mantest-2c_wager_inputs.jpg) | PASS |
| Validate main End of Game choice | Validate value is 1, 2 or 3 | ![EoG1](assets/readme/mantest_screens/pp03_mantest-3a_eog_main.jpg) | PASS |
| Validate best player End of Game choice | Validate value is 1 or 2 | ![EoG2](assets/readme/mantest_screens/pp03_mantest-3b_eog_bp.jpg) | PASS |
| Validate End of Game choice | Validate value is not a cat! | ![EoG3](assets/readme/mantest_screens/pp03_mantest-3c_eog_cat.jpg) | PASS |

- Verification also carried out for checking whether user can afford wager, else "Insufficient credits!" message. Missed getting a screenshot of that one!

- In addition to input validation the game has also been manually verified in respect of correct math and updating of values for the wallet, credits, maxcredits, turns user variables.


[Back to top ???](#)


## BUGS & FIXES

I am pleased to say that the application is, to the best of my knowledge following extensive testing, currently bug-free! One of the main bugs I encountered during the development of this project involved preventing unexpected results by restricting the user from "just hitting Enter" during the username input event:

  ### **Pressing Enter** during username input wasn't being caught...
  
  ??? *Issue:* Whilst playtesting during development it was discovered that "just pressing Enter" for username input wasn't being caught and allowed game continuation with a blank username...
  
  ??? *Fixed:* After much coding experimentation, followed by many fruitless googles, I eventually discovered this Stack Overflow thread: https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths, which contained an example of using regular expressions and the re import. Method and base code was borrowed from here, ammended and utilised within the username validation process.


[Back to top ???](#)


## DEPLOYMENT

![Heroku](assets/readme/grab_screens/pp03_heroku.jpg)

**Heroku** was used to deploy the final application by following these steps (from a modified process as originally utilised in the Love Sandwiches project):

??? Create requirements.txt file using `pip3 freeze > requirements.txt` in console

??? Commit changes; push to GitHub

??? Go to Heroku website

??? Click "Create new app" on Heroku dashboard

??? Enter app name; choose region (Europe); create app

??? Settings tab: "Reveal Config Vars"; add KEY: CREDS; paste contents of creds.json as VALUE

??? Add Config Var KEY: PORT with VALUE: 8000.

??? Under "Buildpacks" section select Python; save changes

??? Add NodeJS buildpack using the process above

??? Deploy tab: "Deployment method", select GitHub; connect

??? Search the repository to be deployed (portfolio-project-three); connect

??? Enable Automatic Deploys; initial Manual Deploy of application

Link to the deployed application [here](https://python-bandit.herokuapp.com/). 


[Back to top ???](#)


# CREDITS

Much appreciation and thanks to my mentor, Marcel Mulders, for his continued advice, support and encouragement.

## Content

??? **One-Armed Bandit copy & info** sourced from: https://en.wiktionary.org/wiki/one-armed_bandit

??? **ASCI color theory & syntax** referenced from: https://stackabuse.com/how-to-print-colored-text-in-python/

??? **Refresh of Python dictionary knowledge** referenced from: https://www.geeksforgeeks.org/python-get-the-first-key-in-dictionary/?ref=rp

??? **Input validation for catching just hitting Enter** utilises code sourced & repurposed from: https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths

??? **Google Cloud Platform** process for activating APIs (Application Programming Interfaces) and obtaining credentials was achieved by re-referencing & revisiting the Love Sandwiches project, as detailed below:

- Create Google Sheets project for application (pref. use personal gmail account).
  
![gsheets](assets/readme/grab_screens/pp03_gsheet.jpg)

### Activate API Credentials

![GCP](assets/readme/grab_screens/pp03_goog_cloud_plat.jpg)

??? Go to Google Cloud Platform dashboard

??? Name & create New Project; select project

??? Go to APIs and Services/Library; search Google Drive

??? Select Google Drive & enable API

??? Select Add Credentials to generate credentials file

??? "Which API are you using?" choose 'Google Drive API'

??? "What data will you be accessing?" choose 'Application Data'

??? Select 'No' for use with Compute Engine, Kubernetes Engine, App Engine or Cloud Functions

??? Click Next; Enter a Service Account Name & click create

??? Select Basic>Editor from Role dropdown

??? Click Continue; click Done

??? Next page: Select Service Account created

??? Next page: Click Keys tab 

??? Click Add Key; select Create New Key

??? Select JSON, then Create

??? jsonfile with API credentials downloaded to computer

??? Back to: APIs and Services/Library; search Google Sheets

??? Select Google Sheets API and enable (no creds required)

??? Drag & drop creds file to GitPod workspace; rename as creds.json

??? Open json file; locate & copy client email

??? Add client email to Share on python_bandits Google sheet
  - Allows for application to access data

??? Creds file contains sensitive data so add to gitignore file list to ensure it is never commited or sent to GitHub

??? Check that creds.json is not committed on next add by checking git status

### Connect Project To Worksheet 

??? Install dependencies in GitPod using `pip3 install gspread google-auth`

??? Set SCOPE and constants values using the code provided by Code Institute

??? Using GSPREAD connect to python_bandits worksheet; Test for access to worksheet - SUCCESSFUL!


[Back to top ???](#)

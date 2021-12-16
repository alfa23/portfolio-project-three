ToC HERE

----


# **INTRODUCTION**


----


![Python One Armed Bandit header](readme_media/)


# User Experience (UX) 


## PROJECT GOALS

**Python Bandit** aims to cater for... 


## External User Goals: User Stories: 

- As a user, I want 
- As a user, I want
- As a user, I want

  Additional ***user expectations*** for consideration include:
  - Responsive: access site easily on any device
  - Responsive: access site easily on any device


## Site Owner Goals:

- Develop a simple interactive game of chance that runs in the CLI 
- Give users the option to continue playing after the initial execution/first game
- Develop a simple interactive CLI game of chance 
  
  Additional ***stakeholder concerns*** for consideration: 
  - 
  -  
  -  


## Features To Include:

-  
- 


----


# FLOWCHART


![LucidChart](readme_media/) 

Flowchart generated in [LucidChart](https://)


---- 


# DESIGN CHOICES


## Colours

To provide a better user experience the decision was taken to add colour, which was applied by utilising the built-in ASCI Escape Sequence syntax. White copy was retained for highlighting user input points and the reel win line.

Other colours used were: 

  • **Red - \033[1;31;m** for validation warning messages and losing spins
  
  • **Green - \033[1;32;m** for confirmation messages and x3 winning spins
  
  • **Yellow - \033[1;33;m** for informative text & messages

  • **Blue - \033[1;34;m** for the main logo, 'structural' elements (lines & boxes) and instructive messages

  • **Cyan - \033[1;36;m** for confirmation of x2 winning spins, to slightly differentiate from x3 winning spins

  The value of 1 in the examples above denote bold styling; variations of this value were utilised to achieve different text styles, specifically 3 for italics, 4 for underlines and 0 for resetting (normal-ising) text.


----


# TECHNOLOGIES

During the course of this project I have utilised the following technologies:


## Languages

- [**Python**](https://www.javascript.com/) was used to build the application


## Tools

- [**Git**](https://git-scm.com/) was used for version control (commit to Git and push to GitHub)

- [**Gitpod**](https://www.gitpod.io/) was used to write the code; an online IDE linked to the GitHub repository

- [**GitHub**](https://github.com/) was used to create the repository and store the project's code after being pushed from Git

- [**LucidChart**](https://) used to generate project flowchart

- [**Google Cloud Platform**](https://) used to connect & configure the APIs used in the project; specifically for Google Drive and Google Sheets integration, including generation of the required creds.json file

- [**amiresponsive**](http://ami.responsivedesign.is/) used to check how responsive the application is on different devices

- [**PEP8**](https://), [**Python Validator**](https://validator.w3.org/) used to validate all Python source code

- [**Heroku**](https://) used to configure and deploy the final project


----


# FEATURES


## Background info & Introduction

![Intro Header](readme_media/)

![Intro Copy](readme_media/)

![Intro Footer](readme_media/)

  - 
      
      • 
  
  - 

      • 


## Game Loop

![Image](readme_media/)

![Image](readme_media/)

![Image](readme_media/)

  - 
      
      • 
  
  - 

      • 


## Game Loop

![Image](readme_media/)

![Image](readme_media/)

![Image](readme_media/)

  - 
      
      • 
  
  - 

      • 


## Game Loop

![Image](readme_media/)

![Image](readme_media/)

![Image](readme_media/)

  - 
      
      • 
  
  - 

      • 


## Game Loop

![Image](readme_media/)

![Image](readme_media/)

![Image](readme_media/)

  - 
      
      • 
  
  - 

      • 


## *Features to Implement*

- 

----


# VERSION CONTROL

Managed within **GitHub** and **Gitpod** via regular commits pushed to GitHub remote servers:


## Gitpod Workspaces
1. Starting from GitHub, clone the Code Institute template by clicking Use This Template and copying to my repo. Launch Workspace by clicking GitPod button - this action is only performed once and the workspace is subsequently reopened through GitPod.

2. Start the Gitpod Workspace which opens an online IDE editor window.
    
    - Update GitHub by committing from GitPod

3. During editing save the code regularly, using git add ., git commit -m "commit message here" and git push Bash commands to push changes to the GitHub repository.

4. Meaningful commit messages allow easy roll-back of any changes to earlier versions.


# TESTING 

## Testing External User Goals & Stories


## Aut TESTING


## PEP8 Validator Testing 

- Python
  - No errors were returned when passing through the [PEP8 validator](https://)

![PEP8](readme_media/)


## Response Testing

In order to test responsiveness to all device sizes, I used [amiresponsive](http://ami.responsivedesign.is/)

![amiresponsive](readme_media/)


## MANUAL TESTING


| FEATURE | OUTCOME | EXAMPLE | PASS/FAIL |
|---|---|:---:|:---:|
| Name Input | Validate value is | ![image](readme_media/) | PASS |
| Name Input | Validate value is | ![image](readme_media/) | PASS |
| Name Input | Validate value is | ![image](readme_media/) | PASS |
| Name Input | Validate value is | ![image](readme_media/) | PASS |
| Name Input | Validate value is | ![image](readme_media/) | PASS |
| Name Input | Validate value is | ![image](readme_media/) | PASS |
| Name Input | Validate value is | ![image](readme_media/) | PASS |
| Name Input | Validate value is | ![image](readme_media/) | PASS |


## BUGS and FIXES


### **Bug:** title
  
  • *Issue:* 
  
  • *Fixed:* 


### **Bug:** title
  
  • *Issue:* 
  
  • *Fixed:* 


### **Bug:** title
  
  • *Issue:* 
  
  • *Fixed:* 


# DEPLOYMENT

**Heroku** was used to deploy the final application by following these steps:

• Create requirements.txt file using pip3 freeze > requirements.txt in console
• Commit changes; push to GitHub
• Go to Heroku website
• Click "Create new app" on Heroku dashboard
• Enter app name; choose region (Europe); create app
• Settings tab: "Reveal Config Vars"; add KEY: CREDS; paste contents of creds.json as VALUE
• Add Config Var KEY: PORT with VALUE: 8000.
• Under "Buildpacks" section select Python; save changes
• Add NodeJS buildpack using the process above
• Deploy tab: "Deployment method", select GitHub; connect
• Search the repository to be deployed (portfolio-project-three); connect
• Enable Automatic Deploys; initial Manual Deploy of application


The live link can be found here - https:// 


# CREDITS


## Content

• **Google Cloud Platform** process for activating APIs and obtaing creds.json was achieved by re-referencing & revisiting the Love Sandwiches project

• **Example** sourced from: https://

• **Example** sourced from: https://

• **Example** sourced from: https://

• **Example** sourced from: https://

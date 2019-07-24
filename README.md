# Scripts
A collection of all the Scripts I make for myself, descriptions below:

1. KillApplications.sh
  (Uses: Bash)

  - Contains a list of applications that should all be closed
  - Checks if the application has any processes that are currently running
  - if there are applications open kill them
  - if there is no instances open display a message to terminal
  - Tell the terminal when the process is complete
  - (this is a simple modular for a larger project)

2. Auto_Login.py
  (Uses: Python and Selenium)

  - Contains a script to get terminal arugements for username, password, and url of a website
  - opens google chrome and goes to that URL
  - looks in the URL's html code for a input form with the id "username" and enters the given arugement (working on making it look for more then just ID if this fails)
  - looks in the URL's html code for a input form with the id "password" and enters the given arugement (working on making it look for more then just ID if this fails)
  - hits the login button

3. Steam_Top_Selling_Scraper.py
  (Uses: Python and Selenium)

  - Contains a script that grabs the list of top selling games from steam.com and saves it to a local text file
  - opens google chrome and goes to https://store.steampowered.com
  - looks for the Top Selling (For all game categories) tab on the home page
  - Clicks the tab to open up the table
  - copies a list of game names and prices saves these lists to a text file
  - navagates to the Action and Advenure games tabs to do the same for those categories specifically

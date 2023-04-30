# PokemonUI
GUI that runs pokemon scripts that I made.
It dynamically pulls them down from their own repos so if I change the scripts, I don't have to recompile the EXE file to update the changes.

# WARNING
Windows Security will flag this as a trojan as it runs scripts that control your keyboard and mouse input to play the game for you


# Game Configuration:
* Make battle log as minimized as possible and lock the chat.
* Set window size: 1280x720 in Settings.
* Turn off, 'Show Overworld in Battle' and 'Show Battle Background' in Settings/Video.
* Controls are default
* Extract the 'black_battle_options.zip' and add it as a custom Pokemmo theme (search up how to add custom themes to the game).

# Path Correction/Item Farming Setup:
* Sometimes the script will overshoot/undershoot the path the player takes. Setting this up will help the script 
correct any path it misses (currently working for Ditto Farm and Amulet Farming).
* For Item finding, it will make sure to read the latest battle log only and not read older battle logs by knowing where your game is on your screen.

## Setup:
* Find the game folder (could be in Program Files, Program Files x86, etc).
* Run the add_game_path.exe file and paste the directory path (only needs to be ran once).

## Delete:
* To delete, just look for the corresponding .dat file


# Gmail Notification:
## This is optional
Emails you when game encounters a shiny (the script will end itself when it encounters one automatically) 
or when the script has finished running.

## Setup:
* Generate google app password for account
* Run add_gmail.exe and input email address and correlated app password (only needs to be ran once)

## Delete:
* To delete, just look for the corresponding .dat file

# Jump to specific Script:
* [Farming Everstones](#farming-everstones)
* [Farming Amulet Coins](#farming-amulet-coins)
* [Plant or Water](#plant-or-water)
* [Level Farming](#level-farming)
* [Ditto Farm](#ditto-farm)

# Farming Everstones 
## Sinnoh

## Where to start running the code:
* Make sure your character is running and not walking.
* Start at the nurse in the pokecenter at Canalave City.
* 2.30 is the amount of hours.minutes, so the program will run for 2 hours and 30 minutes.
* sweet scent costs 5pp per use, so if you have 32pp then enter: 6
    * if you have 20pp then enter: 4
    * etc
* As soon as you hit start, make sure you click on the game.

## Pokemon Team Composition:
* First pokemon has frisk ability.
* Second pokemon (Quagsire) has thief.
* Pokemon with Sweet Scent must be in your party.
* Pokemon with Teleport must be in your party.
* Pokemon with Dig must be in your party.

## Key Slots:
* Bike in 1st key slot.
* Sweet scent in 4th key slot.
* Teleport in 5th key slot.
* Dig in the 6th key slot.

# Farming Amulet Coins
## Kanto

## Where to start running the code:
* Make sure your character is running and not walking.
* Start at the nurse in the pokecenter at Cerulean City.
* Must have HM Cut
* 2.30 is the amount of hours.minutes, so the program will run for 2 hours and 30 minutes.
* sweet scent costs 5pp per use, so if you have 32pp then enter: 6
    * if you have 20pp then enter: 4
    * etc
* As soon as you hit start, make sure you click on the game.

## Pokemon Team Composition:
* First pokemon (Banette) has frisk ability and thief.
* Pokemon with Sweet Scent must be in your party.
* Pokemon with Teleport must be in your party.

## Key Slots:
* Bike in 1st key slot.
* Sweet scent in 4th key slot.
* Teleport in 5th key slot.

# Plant or Water
## Unova

## Where to start running the code:
* Mistralton:
    * Make sure your character is on the bike.
    * Start by facing up at the most bottom left soil.
* Abundant Shrine:
    * Make sure your character is on the bike.
    * Make sure bike is in key slot #1
    * Start by facing up at the bottom left soil of the patch to the right of the house
    * Activate a Max Repel once you are in position
    * you need a pokemon with surf on your team

## Start script:
* As soon as you press start, make sure you click on the game.
    * If you choose plant, the first plant it will make you choose the seeds manually, you have 10 seconds before the script goes to the next plant and it will do those and the rest automatically.
    
# Level Farming
## Unova

## Python Configuration:
* Tested with Python 3.11.2
* run: pip install -r requirements.txt

## Where to start running the code:
* Make sure your character is running and not walking.
* Start at the nurse in the pokecenter at Lacunosa Town.
* Sweet scent uses 5pp per usage. So if you have 32pp then enter: 6
    * If you have 20pp, then enter: 4
* As soon as you hit start, make sure you click on the game.

## Pokemon Team Composition:
* First pokemon has Surf and is strong enough to kill lvl40s Rapidash.
* Pokemon with Sweet Scent must be in your party.
* Pokemon with Teleport must be in your party.

## Key Slots:
* Bike in 1st key slot.
* Sweet scent in 4th key slot.
* Teleport in 5th key slot.

# Ditto Farm
## Hoenn

## Where to start running the code:
* Make sure your character is running and not walking.
* Start at the nurse in the pokecenter at Fallarbor Town.
* Enter the total amount of duskballs the user currently has
* As soon as you hit start, make sure you click on the game.

## Pokemon Team Composition:
* First pokemon is Smeargle.
   * Has Payday, False Swipe, Assist and SweetScent 
   * Ability is Technician
   * Holding LeftOvers
* Second pokemon is Parasect.
    * Has Counter, Dig, Spore, Endure

## Key Slots:
* Bike in 1st key slot.
* Teleport Ocarina in 5th key slot.
* Dig Ocarina in the 6th key slot.


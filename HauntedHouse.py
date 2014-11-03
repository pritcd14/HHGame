#############################################################################################################
# ASSERTION                                                                                                 #
#############################################################################################################

import random
import winsound
import bot
import time
from data import *

#############################################################################################################
# HELPER FUNCTIONS                                                                                          #
#############################################################################################################

def isMultiwordStatement(value):
    return value.find(" ") != -1


def isItemAvailableAtLocation(ItemID, LocationID):
    return PositionOfItems[ItemID] == LocationID


def isItemInInventory(name):
    return isItemAvailableAtLocation(GetItemID(name), -1)


def changePositionOfItem(ItemID, newLocationID):
    PositionOfItems[ItemID] = newLocationID


#############################################################################################
# GAME LOGIC                                                                                #
#############################################################################################

def GetVerbFromSentence(sentence):
    if not isMultiwordStatement(sentence):
        return sentence
    return sentence[:sentence.find(" ")]


def GetNounFromSentence(sentence):
    if not isMultiwordStatement(sentence):
        return ""
    return sentence[sentence.find(" ") + 1:]


def GetItemID(item):
    for ItemID in range(0, len(ItemList), 1):
        if item == ItemList[ItemID]:
            return ItemID
    return -1


def isMovementAvailable(directioncharacter, LocationID):
    return DirectionsArray[LocationID].find(directioncharacter) >= 0


def isMovementVerb(verb, noun):
    return verb == 'N' or verb == 'S' or verb == 'E' or verb == 'W' or verb == 'U' or verb == 'D' or verb == 'GO'


def GetMovementDirection(statement):
    verb = GetVerbFromSentence(statement)
    noun = GetNounFromSentence(statement)
    if len(verb) == 1:
        return verb
    if verb == 'GO':
        return noun[:1]
    return ''

def GetScore():
    score = 0
    for i in range(0, len(PositionOfItems), 1):
        if isItemAvailableAtLocation(i, -1):
            score += 1

    return score


#############################################################################################
# END GAME LOGIC                                                                            #
#############################################################################################

#############################################################################################
# BEGIN PRESENTATION LOGIC                                                                  #
#############################################################################################

def DisplayGameName():
    print("\n\n╔═══════════════╗\n"
          "║ {} ║\n"
          "╚═══════════════╝".format("Haunted House"))


def DisplayPosition():
    print("Location:", LocationsArray[LocationID].capitalize())


def DisplayItemsAtPosition():
    if ItemsAvailableAtPosition():
        print("You can see these items in your area:", ListItemsAtPosition())

def DisplayVisibleExitsAtPosition():
    exits = ""
    if "N" in DirectionsArray[LocationID]: # See if 'north (N)' is in the list of valid directions
        exits += "North and "
    if "S" in DirectionsArray[LocationID]: # See if 'south (S)' is in the list of valid directions
        exits += "South and "
    if "E" in DirectionsArray[LocationID]: # See if 'east (E)' is in the list of valid directions
        exits += "East and "
    if "W" in DirectionsArray[LocationID]: # See if 'west (W)' is in the list of valid directions
        exits += "West and "

    print("Visible exits:", exits[:-4])

def DisplayGetItemMessage(successful, noun):
    if successful:
        print("You are now carrying:", Carrying())
    else:
        print("You cannot take that!")


def DisplayInventory(strInventory):
    if len(strInventory) == 0:
        strInventory = " Nothing"
    print("You are carrying:" + strInventory)


def DisplayScore(score):
    print("Your current score is:", score)


def DisplayDropMessage(dropped, item):
    if dropped:
        print("You have dropped your ", item)
    else:
        print("You can't drop what you don't have!")

def DisplayAttemptOpenDoor(opened):
    if opened:
        print("The door is now open! Revealing a new exit!")
    else:
        print("The door is locked!")


def ExamineCoat():
    if LocationID == 32 and isItemAvailableAtLocation(GetItemID("Key"), 100):
        PositionOfItems[GetItemID("KEY")] = 32
        return 1
    elif LocationID == 32 and not isItemAvailableAtLocation(GetItemID("Key"), 100):
        return 2
    return 99


def ExamineDrawer():
    if LocationID == 43 and isItemInInventory("KEY"):
        return 3
    elif LocationID == 43 and not isItemInInventory("KEY"):
        return 4
    return 99


def ExamineRubbish():
    if LocationID == 3:
        return 5
    return 99


def ExamineWall():
    global Events
    if LocationID == 43:
        Events[0] = 1
        LocationsArray[LocationID] = "STUDY WITH DESK"
        DirectionsArray[LocationID] = "NW"
        return 6
    return 7


def ExamineDoor():
    if LocationID == 28 and isItemInInventory("KEY"):
        DirectionsArray[LocationID] = "SEW"
        return 8
    elif LocationID == 28 and not isItemInInventory("KEY"):
        return 9
    return 88


def DoExamine(noun):
    if noun == "COAT":
        return ExamineCoat()
    if noun == "DRAWER":
        return ExamineDrawer()
    if noun == "RUBBISH":
        return ExamineRubbish()
    if noun == "WALL":
        return ExamineWall()
    if noun == "DOOR":
        return ExamineDoor()

    return 99


def DisplayExamineMessage(MessageID, noun):
    if MessageID == 1:
        print("You examine the coat and find a dusty key in the pocket")
    elif MessageID == 2:
        print("It\'s a dirty old coat")
    elif MessageID == 3:
        print("You unlock the drawer and find is empty")
    elif MessageID == 4:
        print("The drawer is locked")
    elif MessageID == 5:
        print("The rubbish is filthy, what were you expecting to find?")
    elif MessageID == 6:
        print("You inspect the wall and find it is a fake wall, a new exit is revealed!")
    elif MessageID == 7:
        print("No interesting walls here")
    elif MessageID == 8:
        print("You unlock the door and discover a new location!")
    elif MessageID == 9:
        print("The door is locked")

    elif MessageID == 88:
        print("No interesting " + noun + " here...")
    elif MessageID == 99:
        print("What " + noun + "?")

def RoomInfo(value):
    if value == LocationID:
        return " ☺"
    if value in PositionOfProps:
        return " ▪"
    if value in PositionOfItems:
        return " ▫"
    else:
        return "  "


def DisplayMap():
    Line1 = ""
    Line2 = ""
    Line3 = ""

    for Index in range(0, 64, 1):
        currentValues = DirectionsArray[Index]

        if Index in VisitedPlaces:
            if "N" in currentValues:
                Line1 += '░  ░'
            else:
                Line1 += "░░░░"

            if "W" in currentValues:
                Line2 += (" ") + RoomInfo(Index)
            else:
                Line2 += ("░") + RoomInfo(Index)

            if "E" in currentValues:
                Line2 += (" ")
            else:
                Line2 += ("░")

            if "S" in currentValues:
                Line3 += "░  ░"
            else:
                Line3 += "░░░░"

        else:
            Line1 += "    "
            Line2 += "    "
            Line3 += "    "

        if (Index + 1) % 8 == 0:
            if Line1.find("░") != -1:
                print(Line1)
                print(Line2)
                print(Line3)
            Line1 = ""
            Line2 = ""
            Line3 = ""

    print("\n╔════════════════════════════════════════╗\n"
          "║{:^40s}║\n"
          "║{:40s}║\n"
          "╚════════════════════════════════════════╝".format("Map Key: ", " ○ = You   ▫ = Object found   ▪ = Prop "))


#############################################################################################
# END PRESENTATION LOGIC                                                                    #
#############################################################################################



def Carrying():
    strItems = ""
    for i in range(0, len(PositionOfItems), 1):
        if PositionOfItems[i] == -1:
            strItems = strItems + " " + ItemList[i].capitalize()
    return strItems

def ListItemsAtPosition():
    strItems = ""
    for i in range(0, len(PositionOfItems), 1):
        if PositionOfItems[i] == LocationID:
            strItems = strItems + " " + ItemList[i].capitalize()
    return strItems


def ItemsAvailableAtPosition():
    for i in range(0, len(PositionOfItems), 1):
        if PositionOfItems[i] == LocationID:
            return True
    return False

def Go(statement):
    global LocationID
    directioncharacter = GetMovementDirection(statement)

    if LocationID == WINNING_ROOM and Events[2] == 1 and directioncharacter == "S":
        SaveGame()
        InitEnd(1)

    else:
        if isMovementAvailable(directioncharacter, LocationID):
            if directioncharacter == 'N':
                LocationID -= 8
            elif directioncharacter == 'S':
                LocationID += 8
            elif directioncharacter == 'W':
                LocationID -= 1
            elif directioncharacter == 'E':
                LocationID += 1

def GetItem(ItemID, LocationID):
    if isItemAvailableAtLocation(ItemID, LocationID):
        changePositionOfItem(ItemID, -1)
        return True
    return False


def DropItem(ItemID):
    if isItemAvailableAtLocation(ItemID, -1):
        changePositionOfItem(ItemID, LocationID)
        return True
    return False


def OpenDoor():
    global Events
    if LocationID == 28 and isItemInInventory("KEY"):
        Events[1] = 1
        DirectionsArray[LocationID] = "SEW"
        return True
    return False


def ToggleMap():
    global MapEnabled
    if MapEnabled is False:
        MapEnabled = True
    else:
        MapEnabled = False

def ProcessStatement(statement):
    verb = GetVerbFromSentence(statement)
    noun = GetNounFromSentence(statement)

    if verb in ["HELP", "COMMANDS", "VERBS", "OBJECTIVE"]:
        DungeonMaster()

    if verb in ["SCORE", "SC"]:
        DisplayScore(GetScore())

    if verb in ["CARRYING", "INVENTORY", "INV", "ITEMS"]:
        DisplayInventory(Carrying())

    if verb in ["GET", "TAKE"]:
        DisplayGetItemMessage(GetItem(GetItemID(noun), LocationID), noun)

    if verb in ["MAP", "M"]:
        ToggleMap()

    if verb in ["QUIT", "EXIT"]:
        OnGameExit("NO")

    if verb == "SAVE":
        SaveGame()

    if verb == "LOAD":
        LoadGame()

    if verb == "TALK" and LocationID == 24:
        StartConversation()
        
    elif ((verb == "OPEN" or verb == "UNLOCK") and noun == "DOOR") or (verb == "USE" and noun == "KEY"):
        DisplayAttemptOpenDoor(OpenDoor())

    elif verb == "DROP":
        DisplayDropMessage(DropItem(GetItemID(noun)), noun)

    elif verb == "EXAMINE":
        DisplayExamineMessage(DoExamine(noun), noun)
        
    elif verb == "HACK" and noun == "MAP":
        global VisitedPlaces
        VisitedPlaces = [i for i in range(0, 64)]

    elif verb == "HACK" and noun == "ITEMS":
        global PositionOfItems
        for idx in range(0, len(PositionOfItems)):
            PositionOfItems[idx] = -1

        
    elif isMovementVerb(verb, noun):
        Go(statement)


def StartConversation():
    """ StartConversation will talk to Cleverbot

    """
    cb = bot.Session()
    question = ""
    print("Type 'end' to finish conversation")
    while True:
        question = input("You: ")
        if question == "end":
            print("You: Bye")
            answer = cb.Ask("Goodbye")
            print("Shady Figure:", answer)
            time.sleep(2)
            break
        answer = cb.Ask(question)
        print("Shady Figure:", answer)

def DungeonMaster():
    print("╔══════════════════════════════╗\n"
          "║ {} ║\n"
          "╚══════════════════════════════╝".format("Welcome to the Haunted House"))
    print("\nTo win the game, you must have a score of", WINNING_SCORE, "and be at the:", LocationsArray[WINNING_ROOM].capitalize())
    print("\nHere is a full list of the commands, and what each of them do:")
    print("{:40s}{:40s}".format("Command", "Explanation"))
    for key, value in DVerbList.items():
        print("{:40s}{:40s}".format(key, value))


def getStatementYN(input):
    if input in ["y", "Y", "yes", "YES", ""]:
        return YES
    elif input in ["n", "N", "no", "NO"]:
        return NO
    else:
        return INVALID

def SaveGame():
    print("Saving...")
    with open(fileName, "w") as f:
        f.write("Location={}\n".format(LocationID))

        addStr = "ItemPos="
        addStr += ",".join(str(i) for i in PositionOfItems)
        addStr += "\nVisited="
        addStr += ",".join(str(i) for i in VisitedPlaces)
        addStr += "\nEvents="
        addStr += ",".join(str(i) for i in Events)
        addStr += "\nPlaying={}".format(PLAYING)

        f.write(addStr)
    print("Saving successful.")

def LoadGame():
    print("Loading...")
    with open(fileName, "r") as f:
        global LocationID, PositionOfItems, VisitedPlaces, Events, PLAYING

        #LocationID (line1)
        data = f.readline().split("=")
        LocationID = int(data[1])

        #PositionOfItems (line2)
        PositionOfItems = []
        data = f.readline().split("=")
        newdata = data[1].split(",")
        for item in newdata:
            PositionOfItems.append(int(item))

        #VisitedPlaces (line3)
        VisitedPlaces = []
        data = f.readline().split("=")
        newdata = data[1].split(",")
        for item in newdata:
            VisitedPlaces.append(int(item))

        #Events (line4)
        Events = []
        data = f.readline().split("=")
        newdata = data[1].split(",")
        for item in newdata:
            Events.append(int(item))
        UpdateEvents()

        PLAYING = -1
        data = f.readline().split("=")
        PLAYING = int(data[1])
        if PLAYING != -1:
            if PLAYING == 0:
                winsound.PlaySound("sounds/rain.wav", winsound.SND_LOOP | winsound.SND_ASYNC)
            elif PLAYING == 1:
                winsound.PlaySound("sounds/bg.wav", winsound.SND_LOOP | winsound.SND_ASYNC)


    print("Loading successful.")

def UpdateEvents():
    global DirectionsArray
    if Events[0] == 1:
        DirectionsArray[43] = "NW"
    if Events[1] == 1:
        DirectionsArray[28] = "SEW"
    if Events[2] == 1:
        DirectionsArray[57] = "NSWE"

def SoundManager():
    global PLAYING
    
    if LocationID == 0:
        if PLAYING != SND_RAIN:
            winsound.PlaySound("sounds/rain.wav", winsound.SND_LOOP | winsound.SND_ASYNC)
            PLAYING = SND_RAIN

    if LocationID in [3, 14, 49]:
        if PLAYING != SND_RAIN:
            winsound.PlaySound("sounds/door.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            winsound.PlaySound("sounds/rain.wav", winsound.SND_LOOP | winsound.SND_ASYNC)
            PLAYING = SND_RAIN

    elif LocationID in [11, 22, 41]:
        if PLAYING != SND_BG:
            winsound.PlaySound("sounds/door.wav", winsound.SND_ASYNC)
            time.sleep(0.5)
            winsound.PlaySound("sounds/bg.wav", winsound.SND_LOOP | winsound.SND_ASYNC)
            PLAYING = SND_BG


def OnGameInit():  # When the game first initializes
    printASCII("TITLE")
    winsound.PlaySound("sounds/title.wav", winsound.SND_LOOP | winsound.SND_ASYNC)

def OnGameExit(win):
    global QUIT
    if win == "YES":
        QUIT = True
        pass

    else:
        while True:
            statement = input("Are you sure you want to quit? (Y/n) ").upper()
            if getStatementYN(statement) != INVALID:
                break
        
        if getStatementYN(statement) == YES:
            while True:
                saveGame = input("Do you want to save the game? (Y/n) ").upper()
                if getStatementYN(saveGame) != INVALID:
                    break

            if getStatementYN(saveGame) == YES:
                SaveGame()
                exitString = "Saving the game...\nExiting..."
                
            if getStatementYN(saveGame) == NO:
                exitString = "Exiting without saving..."
            
            QUIT = True
            print("Thank you for playing the Haunted House game")
            print(exitString)
            winsound.PlaySound(None, winsound.SND_NODEFAULT)

        if getStatementYN(statement) == NO:
            print("You chose not to quit")
            return

def printASCII(statement):
    if statement == "WIZARD":
        print("""
        o
                   O       /`-.__
                          /  \\·'^|
             o           T    l  *
                        _|-..-|_
                 O    (^ '----' `)
                       `\\-....-/^
             O       o  ) "/ " (
                       _( (-)  )_
                   O  /\\ )    (  /\\
                     /  \\(    ) |  \\
                 o  o    \\)  ( /    \\
                   /     |(  )|      \\
                  /    o \\ \\( /       \\
            __.--'   O    \\_ /   .._   \\
           //|)\\      ,   (_)   /(((\\^)'\\
              |       | O         )  `  |
              |      / o___      /      /
             /  _.-''^^__O_^^''-._     /
           .'  /  -''^^    ^^''-  \\--'^
         .'   .`.  `'''----'''^  .`. \\
       .'    /   `'--..____..--'^   \\ \\
      /  _.-/                        \\ \\
  .::'_/^   |                        |  `.
         .-'|                        |    `-.
   _.--'`   \\                        /       `-.
  /          \\                      /           `-._
  `'---..__   `.                  .´_.._   __       \\
           ``'''`.              .'gnv   `'^  `''---'^
                  `-..______..-'""")


    if statement == "GAME OVER":
        print ("""
   ______                        ____
  / ____/___ _____ ___  ___     / __ \\_   _____  _____
 / / __/ __ `/ __ `__ \\/ _ \\   / / / / | / / _ \\/ ___/
/ /_/ / /_/ / / / / / /  __/  / /_/ /| |/ /  __/ /
\\____/\\__,_/_/ /_/ /_/\\___/   \\____/ |___/\\___/_/\n\n
        """)

    if statement == "YOU WIN":
        print("""
 __     __                    _
 \\ \\   / /                   (_)
  \\ \\_/ /__  _   _  __      ___ _ __
   \\   / _ \\| | | | \\ \\ /\\ / / | '_ \\
    | | (_) | |_| |  \\ V  V /| | | | |
    |_|\\___/ \\__,_|   \\_/\\_/ |_|_| |_|
    """)

    if statement == "CREDITS":
        print("""
   _____              _ _ _
  / ____|            | (_) |
 | |     _ __ ___  __| |_| |_ ___
 | |    | '__/ _ \\/ _` | | __/ __|
 | |____| | |  __/ (_| | | |_\\__ \\
  \\_____|_|  \\___|\\__,_|_|\\__|___/

    > Initial Source by David McCurdy, Tony Kuo and Lei Song

    > This source code was edited by Dion Pritchard

    > 'bot' module source code from EvanDotPro on GitHub

    > ASCII Art found at http://ascii.co.uk/art/magician

    > Sound effects from FF7 OST, RPGMaker VXACE soundpack and http://www.soundjay.com/door-sounds-1.html

© 2014, Unitec New Zealand "ISCG5420 Programming Fundamentals"


Thanks for playing!
- Dion""")
        printASCII("DOGE")

    if statement == "DOGE":
        print("""
░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░
░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░
░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░
░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░
░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░
░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░ much game
░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░
░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░
░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░
░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░    such mark?
▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░
▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░
░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░
░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░very wow
░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░
░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░
░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░10/10
░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░
    """)

    if statement == "TITLE":
        print("""
    __  __                  __           __   __  __
   / / / /___ ___  ______  / /____  ____/ /  / / / /___  __  __________
  / /_/ / __ `/ / / / __ \\/ __/ _ \\/ __  /  / /_/ / __ \\/ / / / ___/ _ \\
 / __  / /_/ / /_/ / / / / /_/  __/ /_/ /  / __  / /_/ / /_/ (__  )  __/
/_/ /_/\\__,_/\\__,_/_/ /_/\\__/\\___/\\__,_/  /_/ /_/\\____/\\__,_/____/\\___/
        """)
        printASCII("TITLE2")

    if statement == "TITLE2":
        print("""
                              .-----.
                            .'       `.
                           :           :
                           :           :
                           '           '
            |~        www   `.       .'
           /.\\       /#^^\\_   `-/\\--'
          /#  \\     /#%    \\   /# \\
         /#%   \\   /#%______\\ /#%__\\
        /#%     \\   |= I I ||  |- |
        ~~|~~~|~~   |_=_-__|'  |[]|
          |[] |_______\\__|/_ _ |= |`.                  1. New Game
   ^V^    |-  /= __   __    /-\\|= | :;                 2. Load Game
          |= /- /\\/  /\\/   /=- \\.-' :;
          | /_.=========._/_.-._\\  .:'
          |= |-.'.- .'.- |  /|\\ |.:'
          \\  |=|:|= |:| =| |~|~||'|
           |~|-|:| -|:|  |-|~|~||=|      ^V^
           |=|=|:|- |:|- | |~|~|| |
           | |-_~__=_~__=|_^^^^^|/___
           |-(=-=-=-=-=-(|=====/=_-=/\\
           | |=_-= _=- _=| -_=/=_-_/__\\
           | |- _ =_-  _-|=_- |]#| I II
           |=|_/ \\_-_= - |- = |]#| I II
           | /  _/ \\. -_=| =__|]!!!I_II!!
          _|/-'/  ` \\_/ \\|/' _ ^^^^`.==_^.
        _/  _/`-./`-; `-.\\_ / \\_'\\`. `. ===`.
       / .-'  __/_   `.   _/.' .-' `-. ; ====;\\
      /.   `./    \\ `. \\ / -  /  .-'.' ====='  >
     /  \\  /  .-' `--.  / .' /  `-.' ======.' /
        """)


def InitEnd(value):
    if value == 1: # Boss Fight
        winsound.PlaySound("sounds/battle.wav", winsound.SND_LOOP | winsound.SND_ASYNC)

        printASCII("WIZARD")
        print("\nYou encounter an evil wizard at the end of the bridge!")
        print("He won't let you pass, you must fight him!")
        playerHealth = 150
        enemyHealth = 120
        attack = 0
        defense = 0
        FightOver = False
        while FightOver is False:
            defense = 0
            if PositionOfItems[1] == -2: # If the player is wearing the Ring, then improve their stats
                defense = 3
                attack = 4

            if playerHealth <= 0: # If the player dies...
                printASCII("GAME OVER")

                print("Loading from last auto-save (before the fight against the wizard)")
                LoadGame()
                break

            if enemyHealth <= 0: # If the wizard dies...
                InitEnd(2)
                break

            print("\n╔═════════════════════════════════════════╗\n"
                  "║ {:20s}{:20s}║\n"
                  "║ {:20s}{:20s}║\n"
                  "║ Health: {:<10d} Enemy Health: {:<7d}║\n"
                  "╚═════════════════════════════════════════╝".format("1. Attack ", "2. Defend", "3. Use Item", "4. Throw Item", playerHealth, enemyHealth))

            while True:
                statement = input("What do you want to do? (1-4) ")
                if statement in ["1", "2", "3", "4"]:
                    break

            if statement == "1":
                rand = random.randint(0, 4)
                if rand == 0:
                    print("Attack missed !")
                else:
                    print("You attacked the evil wizard dealing {} damage".format(rand))
                    enemyHealth -= rand

            elif statement == "2":
                defense += random.randint(1, 4)
                print("Defending, blocking {} damage".format(defense))

            elif statement in ["3", "4"]:
                for idx, item in enumerate(ItemList):
                    if PositionOfItems[idx] == -1:
                        print("{}. {}".format(idx, item))

                while True:
                    itemidx = input("Which item do you want to use? (0-16) ")
                    try:
                        itemidx = int(itemidx)
                        if PositionOfItems[itemidx] != -1:
                            print("You do not have that item anymore! You cannot use it!")
                        else:
                            break

                    except:
                        print("That is not a valid index (0-16)")

                if statement == "3":
                    dmg = UseItem(itemidx)

                elif statement == "4":
                    dmg = ThrowItem(itemidx)

                dmg += attack
                enemyHealth -= dmg
                print("You deal {} damage to the evil wizard".format(dmg))

            rand = random.randint(0, len(EnemyAttacks)-1)
            enemydmg = list(EnemyAttacks)[rand]
            enemydmg -= defense
            print("The evil wizard {} and takes off {} health".format(list(EnemyAttacks.values())[rand], enemydmg))
            playerHealth -= enemydmg


    elif value == 2: # Boss Fight over
        print("You defeated the evil wizard, you can now leave this Haunted House!")

        InitEnd(3)

    else: # Show credits
        printASCII("YOU WIN")
        printASCII("CREDITS")
        OnGameExit("YES")

def UseItem(index):
    global ItemList, PositionOfItems

    itemDmg = 0
    if PositionOfItems[index] == -1:
        if index == 0: # PAINTING
             print("You hold up the painting and show it to the wizard!")

        elif index == 1: # RING
            PositionOfItems[index] = -2
            print("You put the ring on your finger, you feel stronger!")

        elif index == 2: # MAGIC SPELLS
            PositionOfItems[index] = -2
            print("You chant out the only pronounceable words you see: SATOR AREPO TENET OPERA ROTAS")
            itemDmg = random.randint(20, 25)

        elif index == 3: # GOBLET
            print("You inspect the goblet, nothing happens!")

        elif index == 4: # SCROLL
            print("You open the scroll and read the statement: ABRACADABRA, this healing spell heals the evil wizard")
            itemDmg = -10

        elif index == 5: # COINS
            result = random.choice("HT")
            if result == "H":
                result = "Heads"
            else:
                result = "Tails"
            print("You flip a coin, lands on", result)

        elif index == 6: # STATUE
            print("You inspect the statue, and wonder how you managed to carry it around")

        elif index == 7: # CANDLESTICK
            print("Just an ordinary candle stick...")

        elif index == 8: # MATCHES
            PositionOfItems[index] = -2
            print("You light your only match and throw it at the evil wizard")
            itemDmg = 10

        elif index == 9: # VACUUM
            print("A great vacuum cleaner, in fair condition")

        elif index == 10: # BATTERIES
            print("Just ordinary double A batteries...")

        elif index == 11: # SHOVEL
            print("You run toward the evil wizard and hit him with your shovel")
            itemDmg = random.randint(3, 6)

        elif index == 12: # AXE
            print("You run toward the evil wizard and hit him with your axe")
            itemDmg = random.randint(6, 8)

        elif index == 13: # ROPE
            print( "You don't know how to Lasso, nothing happens!")

        elif index == 14: # BOAT
            print("There is no water to place to boat in... how'd you manage to carry this anyway?")

        elif index == 15: # AEROSOL
            print("You spray the evil wizard with your can of Aerosol!")
            itemDmg = random.randint(1, 2)

        elif index == 16: # KEY
            print("Just an ordinary key...")

        return itemDmg

    else:
        print("Error has occurred (error code 201)")

def ThrowItem(index):
    global ItemList, PositionOfItems

    itemDmg = 1
    if PositionOfItems[index] == -1:
        PositionOfItems[index] = -2
        if index in [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 15, 16]:
            print("You throw your {} at the evil wizard!".format(ItemList[index]))

        elif index == 6: # STATUE
            print("You throw a huge statue at the evil wizard... how'd you manage to carry this anyway?")
            itemDmg = random.randint(6, 10)

        elif index == [11, 12]: # SHOVEL
            print("You throw your {} at the evil wizard!".format(ItemList[index]))
            itemDmg = random.randint(6, 10)

        elif index == 13: # ROPE
            print("You do not know how to throw a Lasso, you cannot throw your rope")
            PositionOfItems[13] = -1 # This is to make sure the player always has 1 item at least to throw, otherwise they would get stuck in a while loop
            itemDmg = 0
        elif index == 14: # BOAT
            print("You throw a huge boat at the evil wizard... how'd you manage to carry this anyway?")
            itemDmg = random.randint(10, 15)


        return itemDmg

    else:
        print("Error has occurred (error code 202)")


def Game():
    '''main game functionality
        all

    '''
    global VisitedPlaces, Events
    OnGameInit()

    while True:
        statement = input("What do you want to do? ")
        if statement == "1":
            winsound.PlaySound("sounds/select1.wav", winsound.SND_ASYNC)
            time.sleep(0.7)
            break
        if statement == "2":
            winsound.PlaySound("sounds/select2.wav", winsound.SND_ASYNC)
            LoadGame()
            time.sleep(0.7)
            break


    DungeonMaster()
    while True:
        if LocationID not in VisitedPlaces:
            VisitedPlaces.append(LocationID)
        DisplayGameName()
        if MapEnabled is True:
            DisplayMap()
        SoundManager()
        DisplayPosition()
        DisplayItemsAtPosition()
        DisplayVisibleExitsAtPosition()
        if LocationID == 24:
            print("Type 'talk' to try start a conversation")
        statement = input("What do you want to do next? ")
        ProcessStatement(statement.upper())

        if GetScore() == 17 and DirectionsArray[57] == "NWE":
            print("The ground begins to shake, an exit has opened up")
            Events[2] = 1
            UpdateEvents()


        if QUIT == True:
            break

# TestGame()
Game()

#############################################################################################################
# ASSERTION                                                                                                 #
#############################################################################################################

import random
from data import *
# from tests import *

#############################################################################################################
# HELPER FUNCTIONS                                                                                          #
#############################################################################################################

def contains(validValues, values):
    validCount = 0
    lengthValues = len(values)
    for letter in validValues:
        for character in values:
            if letter == character:
                validCount = validCount + 1
    return validCount == lengthValues


def isValidName(value):
    alphabeticCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ &-"
    return contains(alphabeticCharacters, value)

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


def isEndOfGame(score, locationID):
    return score == WINNING_SCORE and locationID == WINNING_ROOM


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
          "║ %s ║\n"
          "╚═══════════════╝" %"Haunted House")


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
        strInventory = "Nothing"
    print("You are carrying:" + strInventory)


def DisplayScore(score):
    print("Your current score is:", score)


def DisplayTheDoorIsLockedMessage():
    print("THE DOOR IS LOCKED")


def DisplayOpenDoorMessage():
    print("THE DOOR IS NOW OPEN! REVEALING A NEW EXIT!")


def DisplayDigAroundTheBars():
    print("YOU DIG AROUND! THE BARS IN THE WINDOW BECOME LOOSE! REVEALING A NEW EXIT!")


def DisplayYouDugAHole():
    print("YOU DIG A HOLE")


def DisplayWhatWith():
    print("YOU HAVE NOTHING TO DIG WITH")


def DisplayDropMessage(dropped, item):
    if dropped:
        print("YOU HAVE DROPPED THE ", item)
    else:
        print("YOU CANNOT DROP THAT WHICH YOU DO NOT POSSESS")


def DisplayDigAttempt(DigMessageType):
    if DigMessageType == 1:
        print("YOU DIG AROUND THE ROOM. THE BARS BECOME LOOSE. A NEW EXIT!")
    elif DigMessageType == 2:
        print("YOU DIG A LITTLE HOLE.")
    else:
        print("WHAT WITH?")


def DisplayAttemptOpenDoor(opened):
    if opened:
        DisplayOpenDoorMessage()

    else:
        DisplayTheDoorIsLockedMessage()


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
    if LocationID == 43:
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
        print("YOU EXAMINE THE COAT AND FIND A KEY IN THE POCKET")
    elif MessageID == 2:
        print("IT\'S A DIRTY OLD COAT")
    elif MessageID == 3:
        print("YOU UNLOCK THE DRAWER AND FIND IT IS EMPTY")
    elif MessageID == 4:
        print("UNFORTUNATELY THE DRAWER IS LOCKED")
    elif MessageID == 5:
        print("The rubbish is filthy, what were you expecting to find?")
    elif MessageID == 6:
        print("YOU LOOK AT THE WALL AND DISCOVER IT IS FALSE!\nYOU DISCOVER A NEW EXIT")
    elif MessageID == 7:
        print("NO INTERESTING WALLS HERE")
    elif MessageID == 8:
        print("YOU UNLOCK THE DOOR AND DISCOVER A NEW LOCATION!")
    elif MessageID == 9:
        print("UNFORTUNATELY THE DOOR IS LOCKED")

    elif MessageID == 88:
        print("NO INTERESTING " + noun + "HERE...")
    elif MessageID == 99:
        print("WHAT " + noun + "?")

def RoomInfo(value):
    if value == LocationID:
        return " ○"
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
                Line1 += "░  ░"
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
          "║%-40s║\n"
          "║%-40s║\n"
          "╚════════════════════════════════════════╝"
          %("                 Map Key: ", " ○ = You   ▫ = Object found   ▪ = Prop "))


#############################################################################################
# END PRESENTATION LOGIC                                                                    #
#############################################################################################



def Carrying():
    strItems = ""
    for i in range(0, len(PositionOfItems), 1):
        if PositionOfItems[i] == -1:
            strItems = strItems + " " + ItemList[i]
    return strItems.capitalize()


def Dig():
    if LocationID == 30 and isItemInInventory("SHOVEL"):
        DirectionsArray[LocationID] = "SEW"
        LocationsArray[30] = 'HOLE IN WALL'
        return 1
    elif isItemInInventory("SHOVEL"):
        return 2
    return 3


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
    directioncharacter = GetMovementDirection(statement)
    global LocationID
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
    if LocationID == 28 and isItemInInventory("KEY"):
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
        OnGameExit()

    elif ((verb == "OPEN" or verb == "UNLOCK") and noun == "DOOR") or (verb == "USE" and noun == "KEY"):
        DisplayAttemptOpenDoor(OpenDoor())

    elif verb == "DIG" or (verb == "USE" and noun == "SHOVEL"):
        DisplayDigAttempt(Dig())

    elif verb == "DROP":
        DisplayDropMessage(DropItem(GetItemID(noun)), noun)

    elif verb == "EXAMINE":
        DisplayExamineMessage(DoExamine(noun), noun)

    elif isMovementVerb(verb, noun):
        Go(statement)

def DungeonMaster():
    print("╔══════════════════════════════╗\n"
          "║ %s ║\n"
          "╚══════════════════════════════╝" %"Welcome to the Haunted House")
    print("\nTo win the game, you must have a score of", WINNING_SCORE, "and be at the:", LocationsArray[WINNING_ROOM].capitalize())
    print("\nHere is a full list of the commands, and what each of them do:")
    print("%-40s%-40s" %("Command", "Explanation"))
    for key, value in DVerbList.items():
        print("%-40s%-40s" %(key, value))


def getStatementYN(input):
    if input in ["y", "Y", "yes", "YES", ""]:
        return YES
    elif input in ["n", "N", "no", "NO"]:
        return NO
    else:
        return INVALID

def SaveGame():
    print("SAVING")
    print("SAVING")
    print("SAVING")

def OnGameInit():  # When the game first initializes
    DungeonMaster()

def OnGameExit():
    statement = INVALID
    while getStatementYN(statement) == INVALID:
        statement = input("Are you sure you want to quit? (Y/n) ").upper()

    if getStatementYN(statement) == YES:
        saveGame = INVALID
        while getStatementYN(saveGame) == INVALID:
            saveGame = input("Do you want to save the game? (Y/n) ").upper()

        if getStatementYN(saveGame) == YES:
            SaveGame()
            exitString = "Saving the game...\nExiting..."
        if getStatementYN(saveGame) == NO:
            exitString = "Exiting without saving..."

        global QUIT
        QUIT = True
        print("Thank you for playing the Haunted House game")
        print(exitString)
        return

    if getStatementYN(statement) == NO:
        print("You chose not to quit")
        return


def Game():
    global VisitedPlaces
    OnGameInit()
    while not isEndOfGame(LocationID, GetScore()) and not QUIT == True:
        if LocationID not in VisitedPlaces:
            VisitedPlaces.append(LocationID)
        DisplayGameName()
        if MapEnabled is True:
            DisplayMap()
        DisplayPosition()
        DisplayItemsAtPosition()
        DisplayVisibleExitsAtPosition()
        statement = input("What do you want to do next? ")
        ProcessStatement(statement.upper())

# TestGame()
Game()


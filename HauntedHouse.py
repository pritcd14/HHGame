#############################################################################################################
# ASSERTION                                                                                                 #
#############################################################################################################

import random


#############################################################################################################
# ASSERTION                                                                                                 #
#############################################################################################################

def ASSERT(condition, message):
    if not condition:
        raise AssertionError(message+ ":False")

def ASSERT_FALSE(condition, message):
    if not condition:
        raise AssertionError(message+ ":True Failure")

def ASSERT_TRUE(condition, message):
    if not condition:
        raise AssertionError(message+ ":False")

#############################################################################################################
# GAME DATA                                                                                                 #
#############################################################################################################

DirectionsArray = ['SE', 'WE',  'WE',  'SWE', 'WE',   'WE',  'SWE',  'WS',
                   'NS', 'SE',  'WE',  'NW',  'SE',   'W',   'NE',   'NSW',
                   'NS', 'NS',  'SE',  'WE',  'NWUD', 'SE',  'WSUD', 'NS',
                   'N',  'NS',  'NSE',  'WE',  'WE',   'NSW', 'NS',   'NS',
                   'S',  'NSE', 'NSW', 'S',   'NSUD', 'N',   'N',    'NS',
                   'NE', 'NW',  'NE',  'W',   'NSE',  'WE',  'W',    'NS',
                   'SE', 'NSW', 'E',   'WE',  'NW',   'S',   'SW',   'NW',
                   'NE', 'NWE', 'WE',  'WE',  'WE',   'NWE', 'NWE',  'W']

LocationsArray = \
[ 'DARK CORNER',                  'OVERGROWN GARDEN',       'BY LARGE WOODPILE',         'YARD BY RUBBISH',
  'WEEDPATCH',                    'FOREST',                 'THICK FOREST',              'BLASTED TREE',
  'CORNER OF HOUSE',              'ENTRANCE TO KITCHEN',    'KITCHEN & GRIMY COOKER',    'SCULLERY DOOR',
  'ROOM WITH INCHES OF DUST',     'REAR TURRET ROOM',       'CLEARING BY HOUSE',         'PATH',
  'SIDE OF HOUSE',                'BACK OF HALLWAY',        'DARK ALCOVE',               'SHALL DARK ROOM',
  'BOTTOM OF SPIRAL STAIRCASE',   'WIDE PASSAGE',           'SLIPPERY STEPS',            'CLIFFTOP',
  'NEAR CRUMBLING WALL',          'GLOOMY PASSAGE',         'POOL OF LIGHT',             'IMPRESSIVE VAULTED HALLWAY',
  'HALL BY THICK WOODEN DOOR',    'TROPHY ROOM',            'CELLAR WITH BARRED WINDOW', 'CLIFF PATH',
  'CUPBOARD WITH HANGING COAT',   'FRONT HALL',             'SITTING ROOM',              'SECRET ROOM',
  'STEEP MARBLE STAIRS',          'DINING ROOM',            'DEEP CELLAR WITH COFFIN',   'CLIFF PATH',
  'CLOSET',                       'FRONT LOBBY',            'LIBRARY OF EVIL BOOKS',   'STUDY WITH DESK & HOLE IN WALL',
  'WEIRD COBWEBBY ROOM',          'VERY COLD CHAMBER',      'SPOOKY ROOM',               'CLIFF PATH BY MARSH',
  'RUBBLE-STREWN VERANDAH',       'FRONT PORCH',            'FRONT TOWER',               'SLOPING CORRIDOR',
  'UPPER GALLERY',                'MARSH BY WALL',          'MARSH',                     'SOGGY PATH',
  'BY TWISTED RAILING',           'PATH THROUGH IRON GATE', 'BY RAILINGS',               'BENEATH FRONT TOWER',
  'DEBRIS FROM CRUMBLING FACADE', 'LARGE FALLEN BRICKWORK', 'ROTTING STONE ARCH',        'CRUMBLING CLIFFTOP']

VerbList = ['HELP', 'CARRYING?', 'GO',    'N',       'S',       'W',     'E',   'U',      'D',
            'GET',  'TAKE',      'OPEN',  'EXAMINE', 'READ',    'SAY',
            'DIG',  'SWING',     'CLIMB', 'LIGHT',   'UNLIGHT', 'SPRAY', 'USE', 'UNLOCK', 'DROP', 'SCORE']

NounList = ['NORTH',   'SOUTH',  'WEST',   'EAST',    'UP',   'DOWN',
            'DOOR',    'BATS',   'GHOSTS', 'X2ANFAR', 'SPELLS', 'WALL']

PropList = ['DRAWER',  'DESK', 'COAT', 'RUBBISH', 'COFFIN', 'BOOKS']

PositionOfProps = [43, 43, 32, 3, 38, 35]

ItemList = ['PAINTING', 'RING',      'MAGIC SPELLS', 'GOBLET', 'SCROLL', 'COINS', 'STATUE',  'CANDLESTICK', 'MATCHES',
            'VACUUM',   'BATTERIES', 'SHOVEL',       'AXE',    'ROPE',   'BOAT',  'AEROSOL', 'CANDLE',      'KEY']

PositionOfItems = [46, 38, 35, 50, 13, 18, 28, 42, 10, 25, 26, 4, 2, 7, 47, 60, 100, 100]

#############################################################################################################
# TEST FUNCTONS                                                                                             #
#############################################################################################################

def TestDirectionsArray():
    lengthOfDirectionsArray=len(DirectionsArray)
    validvalues='NSEWUD'
    ASSERT(lengthOfDirectionsArray == 64, "The array length is correct?")
    for i in range(0, lengthOfDirectionsArray, 1):
        values = DirectionsArray[i]
        if not contains(validvalues, values):
            ASSERT(False, "The array contains invalid values"+values)
            return

def TestLocationsArray():
    lengthOfLocationsArray = len(LocationsArray)
    ASSERT(lengthOfLocationsArray == 64, "The total number of locations expected was correct")
    for i in range(0, lengthOfLocationsArray, 1):
        value=LocationsArray[i]
        if not isValidName(value):
            print (False, "The value is not alphabetic:"+value)
            return

def TestVerbsArray():
    lengthOfVerbList = len(VerbList)
    ASSERT (lengthOfVerbList == 25, "The size of the verb dictionary is incorrect")

def TestNounsArray():
    lengthOfNounsArray = len(NounList)
    ASSERT (lengthOfNounsArray == 12, "The size of the nouns dictionary is incorrect")
        
def TestItemsArray():
    lengthOfItemsArray = len(ItemList)
    ASSERT (lengthOfItemsArray == 18, "The size of the items dictionary is incorrect")

def TestParse():
    sentence = "GO NORTH"
    ASSERT(isMultiwordStatement(sentence), "Multiword?")
    verb = GetVerbFromSentence(sentence)
    noun = GetNounFromSentence(sentence)
    sentence="SCORE"
    ASSERT (not isMultiwordStatement(sentence), "Multiword wrongly detected")

def TestChangeDirectionCharacter():
    ExpectedRoomsWithDirectionChanges = 3
    ActualRoomsWithDirectionChanges = 0
    lengthOfDirectionsArray=len(DirectionsArray)
    validvalues='NSEW'
    for i in range(0, lengthOfDirectionsArray, 1):
        values = DirectionsArray[i]
        if not contains(validvalues, values):
            ActualRoomsWithDirectionChanges += 1
    ASSERT (ExpectedRoomsWithDirectionChanges == ActualRoomsWithDirectionChanges, "Total Directions Changed Was Correct?")
    newDirection=changeDirectionCharacter("U", 20)
    ASSERT (newDirection == "N", "Changed Incorrectly")
    newDirection=changeDirectionCharacter("D", 20)
    ASSERT (newDirection == "W", "Changed Incorrectly")
    newDirection=changeDirectionCharacter("U", 22)
    ASSERT (newDirection == "W", "Changed Incorrectly")
    newDirection=changeDirectionCharacter("D", 22)
    ASSERT (newDirection == "S", "Changed Incorrectly")
    newDirection=changeDirectionCharacter("U", 36)
    ASSERT (newDirection == "S", "Changed Incorrectly")
    newDirection=changeDirectionCharacter("D", 36)
    ASSERT (newDirection == "N", "Changed Incorrectly")

def TestGo():
    newLocationID = Go("S", 0)
    ASSERT (newLocationID == 8, "Moved to Location Correctly")
    newLocationID = Go("S", newLocationID)
    ASSERT (newLocationID == 16, "Moved to Location Correctly")
    newLocationID = Go("W", newLocationID)
    ASSERT (newLocationID == 16, "Stayed in Location Correctly")
    newLocationID = Go("E", newLocationID)
    ASSERT (newLocationID == 16, "Stayed in Location Correctly")
    newLocationID = Go("S", newLocationID)
    ASSERT (newLocationID == 24, "Moved to Location Correctly")
    newLocationID = Go("N", newLocationID)
    ASSERT (newLocationID == 16, "Moved to Location Correctly")
    newLocationID = Go("N", newLocationID)
    ASSERT (newLocationID == 8, "Stayed in Location Correctly")
    newLocationID = Go("W", newLocationID)
    ASSERT (newLocationID == 8, "Stayed in Location Correctly")
    newLocationID = Go("E", newLocationID)
    ASSERT (newLocationID == 8, "Stayed in Location Correctly")
    newLocationID = Go("N", newLocationID)
    ASSERT (newLocationID == 0, "Moved to Location Correctly")
    newLocationID = Go("N", newLocationID)
    ASSERT (newLocationID == 0, "Stayed in Location Correctly")
    newLocationID = Go("W", newLocationID)
    ASSERT (newLocationID == 0, "Stayed in Location Correctly")
    newLocationID = Go("E", newLocationID)
    ASSERT (newLocationID == 1, "Moved to Location Correctly")
    newLocationID = Go("E", newLocationID)
    ASSERT (newLocationID == 2, "Moved to Location Correctly")
    newLocationID = Go("W", newLocationID)
    ASSERT (newLocationID == 1, "Moved to Location Correctly")

def TestBoundaryOfMap():
    for i in range (0, 7, 1):
        ASSERT(contains("SEW", DirectionsArray[i]), "North Most Extends")
        ASSERT(contains("NEW", DirectionsArray[i+57]), "South Most Extends")

    ASSERT(contains("SE", DirectionsArray[0]), "North West Corner")
    ASSERT(contains("SW", DirectionsArray[7]), "North East Corner")
    ASSERT(contains("NE", DirectionsArray[56]), "South West Corner")
    ASSERT(contains("NW", DirectionsArray[63]), "North East Corner")

    for i in range (8, 48, 8):
        ASSERT(contains("NSE", DirectionsArray[i]), "West Most Extends")
        ASSERT(contains("NSW", DirectionsArray[i+7]), "East Most Extends")        

def TestGoLonger():
    newLocationID = Go("GO SOUTH", 0)
    ASSERT (newLocationID == 8, "Moved to Location Correctly")
    newLocationID = Go("GO SOUTH", newLocationID)
    ASSERT (newLocationID == 16, "Moved to Location Correctly")
    newLocationID = Go("GO WEST", newLocationID)
    ASSERT (newLocationID == 16, "Stayed in Location Correctly")
    newLocationID = Go("GO EAST", newLocationID)
    ASSERT (newLocationID == 16, "Stayed in Location Correctly")
    newLocationID = Go("GO SOUTH", newLocationID)
    ASSERT (newLocationID == 24, "Moved to Location Correctly")
    newLocationID = Go("GO NORTH", newLocationID)
    ASSERT (newLocationID == 16, "Moved to Location Correctly")
    newLocationID = Go("GO NORTH", newLocationID)
    ASSERT (newLocationID == 8, "Stayed in Location Correctly")
    newLocationID = Go("GO WEST", newLocationID)
    ASSERT (newLocationID == 8, "Stayed in Location Correctly")
    newLocationID = Go("GO EAST", newLocationID)
    ASSERT (newLocationID == 8, "Stayed in Location Correctly")
    newLocationID = Go("GO NORTH", newLocationID)
    ASSERT (newLocationID == 0, "Moved to Location Correctly")
    newLocationID = Go("GO NORTH", newLocationID)
    ASSERT (newLocationID == 0, "Stayed in Location Correctly")
    newLocationID = Go("GO WEST", newLocationID)
    ASSERT (newLocationID == 0, "Stayed in Location Correctly")
    newLocationID = Go("GO EAST", newLocationID)
    ASSERT (newLocationID == 1, "Moved to Location Correctly")
    newLocationID = Go("GO EAST", newLocationID)
    ASSERT (newLocationID == 2, "Moved to Location Correctly")
    newLocationID = Go("GO WEST", newLocationID)
    ASSERT (newLocationID == 1, "Moved to Location Correctly")

def TestItemPositions():
    LengthOfItemsPositionArray=len(PositionOfItems)
    LengthOfItemsArray=len(ItemList)
    ASSERT(LengthOfItemsPositionArray==LengthOfItemsArray, "Item List And Item Position Lengths Match?")

def TestIsItemAvailableAtLocation():
    ASSERT(isItemAvailableAtLocation(0, 46) == True, "Item is supposed to be at this location")
    ASSERT(isItemAvailableAtLocation(0, 47) == False, "Item is not supposed to be at this location")
    ASSERT(isItemAvailableAtLocation(17, 100) == True, "Item is supposed to be at this location")
    ASSERT(isItemAvailableAtLocation(17, 33) == False, "Item is not supposed to be at this location")

def TestCarryingNothing():
    itemList = ""
    itemList = Carrying()
    ASSERT(len(itemList) == 0, "Item list is supposed to be empty")

def TestGetItem():
    ASSERT(isItemAvailableAtLocation(17, 100) == True, "Item is supposed to be in this location")
    GetItem(17, 100)
    ASSERT(isItemAvailableAtLocation(17, 32) == False, "Item is no longer in this location")
    strItemList = ""
    strItemList = Carrying()
    ASSERT(len(strItemList) != 0, "Items are now carried")
    DropItem(17, 32)
    strItemList = Carrying()
    ASSERT(len(strItemList) == 0, "Item dropped so now it is supposed to be empty again")

def TestGetScore():
    score = GetScore()
    ASSERT(score == 0, "The score is zero")
    for i in range(0, len(ItemList), 1):
        GetItem(i, PositionOfItems[i])
    ASSERT(GetScore() == 18, "The score is maximum")

def TestEndGame():
    expectedWinConditions = 1
    expectedNonWinConditions = (18 * 64) - 1
    actualWinConditions = 0
    actualNonWinConditions = 0
    for score in range(0, 18, 1):
        for location in range(0, 64, 1):
            if isEndOfGame(score, location):
                actualWinConditions += 1
            else:
                actualNonWinConditions += 1
    ASSERT(actualWinConditions == expectedWinConditions, "Total win conditions check")
    ASSERT(actualNonWinConditions == expectedNonWinConditions, "Total non-win conditions check")

def TestGame():
    TestDirectionsArray()
    TestLocationsArray()
    TestBoundaryOfMap()
    TestVerbsArray()
    TestNounsArray()
    TestItemsArray()
    TestParse()
    TestChangeDirectionCharacter()
    TestGo()
    TestGoLonger()
    TestItemPositions()
    TestIsItemAvailableAtLocation()
    TestCarryingNothing()
    TestGetItem()
    TestGetScore()
    TestEndGame()


#############################################################################################################
# END TESTS                                                                                                 #
#############################################################################################################


#############################################################################################################
# HELPER FUNCTIONS                                                                                          #
#############################################################################################################

def contains(validValues, values):
    validCount = 0
    lengthValues = len(values)
    for letter in validValues:
        for character in values:
           if letter == character:
                validCount=validCount+1
    return validCount == lengthValues

def containsLetter(letter, values):
    for character in values:
        if letter == character:
            return True
    return False

def isAlphabetic(value):
    alphabeticCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return contains(alphabeticCharacters, value)

def isValidName(value):
    alphabeticCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ &-"
    return contains(alphabeticCharacters, value)

def isItemInList(value, list):
    for item in list:
        if item == value:
            return true
    return false

def isValidVerb(value):
    return isItemInList(value, VerbList)

def isValidNoun(value):
    return isItemInList(value, NounList)

def isValidItem(value):
    return isItemInList(value, ItemList)

def isMultiwordStatement(value):
    return value.find(" ") != -1

def isItemAvailableAtLocation(ItemID, LocationID):
    return PositionOfItems[ItemID] == LocationID

def isItemInInventory(name):
    return isItemAvailableAtLocation(GetItemID(name), -1)

def changePositionOfItem(ItemID, newLocationID):
    PositionOfItems[ItemID]=newLocationID

#############################################################################################
# GAME LOGIC                                                                                #
#############################################################################################

def GetVerbFromSentence(sentence):
    if not isMultiwordStatement(sentence):
        return sentence
    locationOfSpace=sentence.find(" ")
    return sentence[:locationOfSpace]

def GetNounFromSentence(sentence):
    if not isMultiwordStatement(sentence):
        return ""
    locationOfSpace=sentence.find(" ") + 1
    return sentence[locationOfSpace:]

def GetItemID(item):
    for ItemID in range(0, len(ItemList), 1):
        if item == ItemList[ItemID]:
            return ItemID
    return -1

def changeDirectionCharacter(directioncharacter, locationID):
    if locationID == 20 and directioncharacter == 'U':
        directioncharacter = 'N'
    elif locationID == 20 and directioncharacter == 'D':
        directioncharacter = 'W'
    elif locationID == 22 and directioncharacter == 'U':
        directioncharacter = 'W'
    elif locationID == 22 and directioncharacter == 'D':
        directioncharacter = 'S'
    elif locationID == 36 and directioncharacter == 'U':
        directioncharacter = 'S'
    elif locationID == 36 and directioncharacter == 'D':
        directioncharacter = 'N'
    return directioncharacter

def isMovementAvailable(directioncharacter, LocationID):
    return DirectionsArray[LocationID].find(directioncharacter) >= 0

def isMovementVerb(verb, noun):
    return verb == 'N' or verb == 'S' or verb == 'E' or verb == 'W' or verb == 'U' or verb == 'D' or verb == 'GO'

def GetMovementDirection(statement):
    verb=GetVerbFromSentence(statement)
    noun=GetNounFromSentence(statement)
    if len(verb)==1:
        return verb
    if verb == 'GO':
        return noun[:1]
    return ''

def isEndOfGame(score, locationID):
    return score == 17 and locationID == 57

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
    print("========Haunted House=========")
    
def DisplayPosition(LocationID):
    print("YOU ARE LOCATED IN A ", LocationsArray[LocationID])

def DisplayItemsAtPosition(LocationID):
    if ItemsAvailableAtPosition(LocationID):
        print("YOU CAN SEE THE FOLLOWING ITEMS AT THIS LOCATION: ", ListItemsAtPosition(LocationID))

def DisplayVisibleExitsAtPosition(LocationID):
    print("VISIBLE EXISTS: ", DirectionsArray[LocationID])

def DisplayListOfVerbs():
    print(VerbsArray)

def DisplayHelpMessage():
    print("I UNDERSTAND THE FOLLOWING WORDS:")
    DisplayListOfVerbs()

def DisplayMoveFromTo(LocationID, newLocationID):
    if LocationID != newLocationID:
        print("YOU MOVED FROM " + LocationsArray[LocationID] + " TO " + LocationsArray[newLocationID])
    else:
        print("YOU ARE UNABLE TO MOVE IN THAT DIRECTION")

def DisplayGetItemMessage(successful, noun):
    if successful:
        print("YOU ARE NOW CARRYING A ", noun)
    else:
        print("SORRY YOU CANNOT TAKE A ", noun)

def DisplayInventory(strInventory):
    if len(strInventory) == 0:
        strInventory = "NOTHING"
    print("YOU ARE CARRYING:" + strInventory)
    
def DisplayScore(score):
    print("YOUR CURRENT SCORE IS:", score)

def DisplayTheDoorIsLockedMessage():
    print("THE DOOR IS LOCKED")

def DisplayOpenDoorMessage():
    print("THE DOOR IS NOW OPEN! REVEALLING A NEW EXIT!")

def DisplayDigAroundTheBars():
    print("YOU DIG AROUND! THE BARS IN THE WINDOW BECOME LOOSE! REVEALLING A NEW EXIT!")

def DisplayYouDugAHole():
    print("YOU DIG A HOLE")

def DisplayWhatWith():
    print("YOU HAVE NOTHING TO DIG WITH")

def GetActionStatement():
    return input("WHAT DO YOU WANT TO DO NEXT?")

def DisplayDropMessage(dropped, item):
    if dropped:
        print("YOU HAVE DROPPED THE ", item)
    else:
        print("YOU CANNOT DROP THAT WHICH YOU DO NOT POSSESS")

def DisplayDigAttempt(DigMessageType):
    if DigMessageType == 1:
        print ("YOU DIG AROUND THE ROOM. THE BARS BECOME LOOSE. A NEW EXIT!")
    elif DigMessageType == 2:
        print ("YOU DIG A LITTLE HOLE.")
    else:
        print ("WHAT WITH?")
    
def DisplayAttemptOpenDoor(opened, LocationID):
    if opened:
        DisplayOpenDoorMessage()
        
    else:
        DisplayTheDoorIsLockedMessage()

def ExamineCoat(LocationID):
    if LocationID == 32 and isItemAvailableAtLocation(GetItemID("Key"), 100):
        PositionOfItems[GetItemID("KEY")] = 32
        return 1
    elif LocationID == 32 and not isItemAvailableAtLocation(GetItemID("Key"), 100):
        return 2
    return 99

def ExamineDrawer(LocationID):
    if LocationID == 43 and isItemInInventory("KEY") :
        return 3
    elif LocationID == 43 and not isItemInInventory("KEY") :
        return 4
    return 99

def ExamineRubbish(LocationID):
    if LocationID == 3:
        return 5
    return 99

def ExamineWall(LocationID):
    if LocationID == 43:
        LocationsArray[LocationID] = "STUDY WITH DESK"
        DirectionsArray[LocationID]="NW"
        return 6
    return 7

def ExamineDoor(LocationID):
    if LocationID == 28 and  isItemInInventory("KEY"):
        DirectionsArray[LocationID]="SEW"
        return 8
    elif LocationID == 28 and  not isItemInInventory("KEY"):
        return 9
    return 88

def DoExamine(LocationID, noun) :
    if noun == "COAT":
        return ExamineCoat(LocationID)
    if noun == "DRAWER":
        return ExamineDrawer(LocationID)
    if noun == "RUBBISH":
        return ExamineRubbish(LocationID)
    if noun == "WALL":
        return ExamineWall(LocationID)
    if noun == "DOOR":
        return ExamineDoor(LocationID)

    return 99
          
def DisplayExamineMessage(MessageID, noun) :
    if MessageID == 1:
        print ("YOU EXAMINE THE COAT AND FIND A KEY IN THE POCKET")
    elif MessageID == 2:
        print ("IT\'S A DIRTY OLD COAT")
    elif MessageID == 3:
        print ("YOU UNLOCK THE DRAWER AND FIND IT IS EMPTY")
    elif MessageID == 4:
        print ("UNFORTUNATELY THE DRAWER IS LOCKED")
    elif MessageID == 5:
        print ("THE RUBBISH IS FILTHY")
    elif MessageID == 6:
        print ("YOU LOOK AT THE WALL AND DISCOVER IT IS FALSE!\nYOU DISCOVER A NEW EXIT")
    elif MessageID == 7:
        print ("NO INTERESTING WALLS HERE")
    elif MessageID == 8:
        print ("YOU UNLOCK THE DOOR AND DISCOVER A NEW LOCATION!")
    elif MessageID == 9:
        print ("UNFORTUNATELY THE DOOR IS LOCKED")

    elif MessageID == 88:
        print ("NO INTERESTING " + noun + "HERE...")
    elif MessageID == 99:
        print ("WHAT " + noun + "?")

'DRAWER',  'DESK', 'COAT', 'RUBBISH', 'COFFIN', 'BOOKS', 'WALL'


def DisplayMagicMessage(LocationID, newLocationID) :
    print ("YOU UTTER WORDS OF DARK MAGIC... X2ANFAR!")
    print ("YOU DISAPPEAR AND REAPPEAR IN ANOTHER LOCATION...")
    print ("YOU WERE IN " + LocationsArray[LocationID])
    print ("YOU ARE NOW IN " + LocationsArray[newLocationID])


def PrintableInts(value):
    if(value<10):
        return " "+str(value)
    return str(value)

def DisplayMap():
        Line1 = ""
        Line2 = ""
        Line3 = ""
        
        for Index in range (0, 64, 1):
            DirectionsArray    
            currentValues=DirectionsArray[Index]
    
            if containsLetter("N", currentValues):
                Line1 += "+  +"
            else:
                Line1 += "+--+"
                
            if containsLetter("W", currentValues):
                Line2 += (" ") + PrintableInts(Index)
            else:
                Line2 += ("|") + PrintableInts(Index)
                
            if containsLetter("E", currentValues):
                Line2 += (" ")
            else:
                Line2 += ("|")

            if containsLetter("S", currentValues):
                Line3 += "+  +"
            else:
                Line3 += "+--+"
    
            if (Index + 1) % 8 == 0:
                print (Line1)
                print (Line2)
                print (Line3)
                Line1 = ""
                Line2 = ""
                Line3 = "" 
                                
#############################################################################################
# END PRESENTATION LOGIC                                                                    #
#############################################################################################



def Carrying():
    strItems=""
    for i in range(0, len(PositionOfItems), 1):
        if PositionOfItems[i] == -1:
            strItems = strItems + " "+ ItemList[i]
    return strItems

def Dig(LocationID):
        if LocationID == 30 and isItemInInventory("SHOVEL"):
            DirectionsArray[LocationID]="SEW"
            LocationsArray[30] = 'HOLE IN WALL'
            return 1
        elif isItemInInventory("SHOVEL"):
            return 2 
        return 3


def ListItemsAtPosition(LocationID):
    strItems=""
    for i in range(0, len(PositionOfItems), 1):
        if PositionOfItems[i] == LocationID:
            strItems = strItems + " "+ ItemList[i]
    return strItems

def ItemsAvailableAtPosition(LocationID):
    for i in range(0, len(PositionOfItems), 1):
        if PositionOfItems[i] == LocationID:
            return True
    return False

def GoMagic(LocationID):
    newLocationID=LocationID
    while(newLocationID == LocationID):
           newLocationID = random.randint(0,63)

    return newLocationID;

def Go(statement, LocationID):
    directioncharacter=GetMovementDirection(statement)
    if isMovementAvailable(directioncharacter, LocationID):
        directioncharacter = changeDirectionCharacter(directioncharacter, LocationID)
        if directioncharacter == 'N':
            LocationID -= 8
        elif directioncharacter == 'S':
            LocationID += 8
        elif directioncharacter == 'W':
            LocationID -= 1
        elif directioncharacter == 'E':
            LocationID += 1
    return LocationID

def GetItem(ItemID, LocationID):
    if isItemAvailableAtLocation(ItemID, LocationID):
        changePositionOfItem(ItemID, -1)
        return True
    return False

def DropItem(ItemID, LocationID):
    if isItemAvailableAtLocation(ItemID, -1):
        changePositionOfItem(ItemID, LocationID)
        return True
    return False

def OpenDoor(LocationID):
    if LocationID == 28 and isItemInInventory("KEY"):
        DirectionsArray[LocationID]="SEW"
        return True
    return False

def ProcessStatement(statement, LocationID):
    verb=GetVerbFromSentence(statement)
    noun=GetNounFromSentence(statement)    

    if verb== "HELP":
        DisplayHelpMessage()

    elif verb == "SCORE":
        DisplayScore(GetScore())

    elif verb == "CARRYING" or verb == "CARRYING?" or verb == "INVENTORY" or verb == "INV":
        DisplayInventory(Carrying())

    elif verb == "GET" or verb == "TAKE":
        DisplayGetItemMessage(GetItem(GetItemID(noun), LocationID), noun)

    elif ((verb == "OPEN" or verb == "UNLOCK") and noun == "DOOR") or (verb =="USE" and noun == "KEY"):
        DisplayAttemptOpenDoor(OpenDoor(LocationID), LocationID)

    elif verb == "DIG" or (verb =="USE" and noun=="SHOVEL"):
        DisplayDigAttempt(Dig(LocationID))

    elif verb == "DROP":
        DisplayDropMessage(DropItem(GetItemID(noun), LocationID), noun)

    elif verb == "EXAMINE":
        DisplayExamineMessage(DoExamine(LocationID, noun), noun)

    elif verb == "SAY" and noun == "X2ANFAR":
        newLocationID = GoMagic(LocationID)
        DisplayMagicMessage(LocationID, newLocationID)
        LocationID = newLocationID

    elif verb == "SHOW" and noun == "MAP":
        DisplayMap()
           
    elif isMovementVerb(verb, noun):  
        newLocationID = Go(statement, LocationID)
        DisplayMoveFromTo(LocationID, newLocationID)
        LocationID = newLocationID

    print ("LocationID=", LocationID)

    return LocationID

def Game():
    locationID = 0
    while not isEndOfGame(locationID, GetScore()):
        DisplayGameName()
        DisplayPosition(locationID)
        DisplayItemsAtPosition(locationID)
        DisplayVisibleExitsAtPosition(locationID)
        statement = GetActionStatement()
        locationID = ProcessStatement(statement, locationID)

#TestGame()
Game()


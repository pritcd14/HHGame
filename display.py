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


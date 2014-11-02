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

def isItemInList(value, list):
	return value in list


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
	if LocationID == 43 and isItemInInventory("KEY"):
		return 3
	elif LocationID == 43 and not isItemInInventory("KEY"):
		return 4
	return 99


def ExamineRubbish(LocationID):
	if LocationID == 3:
		return 5
	return 99


def ExamineWall(LocationID):
	if LocationID == 43:
		LocationsArray[LocationID] = "STUDY WITH DESK"
		DirectionsArray[LocationID] = "NW"
		return 6
	return 7


def ExamineDoor(LocationID):
	if LocationID == 28 and isItemInInventory("KEY"):
		DirectionsArray[LocationID] = "SEW"
		return 8
	elif LocationID == 28 and not isItemInInventory("KEY"):
		return 9
	return 88


def DoExamine(LocationID, noun):
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
		print("THE RUBBISH IS FILTHY")
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

def DisplayMagicMessage(LocationID, newLocationID):
	print("YOU UTTER WORDS OF DARK MAGIC... X2ANFAR!")
	print("YOU DISAPPEAR AND REAPPEAR IN ANOTHER LOCATION...")
	print("YOU WERE IN " + LocationsArray[LocationID])
	print("YOU ARE NOW IN " + LocationsArray[newLocationID])


def PrintableInts(value):
	if (value < 10):
		return " " + str(value)
	return str(value)


def DisplayMap():
	Line1 = ""
	Line2 = ""
	Line3 = ""

	for Index in range(0, 64, 1):
		DirectionsArray
		currentValues = DirectionsArray[Index]
		if "N" in currentValues:
			Line1 += "+  +"
		else:
			Line1 += "+--+"

		if "W" in currentValues:
			Line2 += (" ") + PrintableInts(Index)
		else:
			Line2 += ("|") + PrintableInts(Index)

		if "E" in currentValues:
			Line2 += (" ")
		else:
			Line2 += ("|")

		if "S" in currentValues:
			Line3 += "+  +"
		else:
			Line3 += "+--+"

		if (Index + 1) % 8 == 0:
			print(Line1)
			print(Line2)
			print(Line3)
			Line1 = ""
			Line2 = ""
			Line3 = ""

#############################################################################################
# END PRESENTATION LOGIC                                                                    #
#############################################################################################



def Carrying():
	strItems = ""
	for i in range(0, len(PositionOfItems), 1):
		if PositionOfItems[i] == -1:
			strItems = strItems + " " + ItemList[i]
	return strItems


def Dig(LocationID):
	if LocationID == 30 and isItemInInventory("SHOVEL"):
		DirectionsArray[LocationID] = "SEW"
		LocationsArray[30] = 'HOLE IN WALL'
		return 1
	elif isItemInInventory("SHOVEL"):
		return 2
	return 3


def ListItemsAtPosition(LocationID):
	strItems = ""
	for i in range(0, len(PositionOfItems), 1):
		if PositionOfItems[i] == LocationID:
			strItems = strItems + " " + ItemList[i]
	return strItems


def ItemsAvailableAtPosition(LocationID):
	for i in range(0, len(PositionOfItems), 1):
		if PositionOfItems[i] == LocationID:
			return True
	return False


def GoMagic(LocationID):
	newLocationID = LocationID
	while (newLocationID == LocationID):
		newLocationID = random.randint(0, 63)

	return newLocationID


def Go(statement, LocationID):
	directioncharacter = GetMovementDirection(statement)
	if isMovementAvailable(directioncharacter, LocationID):
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
		DirectionsArray[LocationID] = "SEW"
		return True
	return False


def ProcessStatement(statement, LocationID):
	verb = GetVerbFromSentence(statement)
	noun = GetNounFromSentence(statement)

	if verb in ["HELP", "COMMANDS", "VERBS"]:
		print("I understand these words:\n" + VerbList)

	if verb in ["SCORE", "SC"]:
		DisplayScore(GetScore())

	if verb in ["CARRYING", "CARRYING?", "INVENTORY", "INV"]:
		DisplayInventory(Carrying())

	if verb in ["GET", "TAKE"]:
		DisplayGetItemMessage(GetItem(GetItemID(noun), LocationID), noun)

	elif ((verb == "OPEN" or verb == "UNLOCK") and noun == "DOOR") or (verb == "USE" and noun == "KEY"):
		DisplayAttemptOpenDoor(OpenDoor(LocationID), LocationID)

	elif verb == "DIG" or (verb == "USE" and noun == "SHOVEL"):
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

	print("LocationID=", LocationID)

	return LocationID


def Game():
	locationID = 0
	while not isEndOfGame(locationID, GetScore()):
		DisplayGameName()
		DisplayPosition(locationID)
		DisplayItemsAtPosition(locationID)
		DisplayVisibleExitsAtPosition(locationID)
		statement = input("What do you want to do next? ")
		locationID = ProcessStatement(statement.upper(), locationID)

#TestGame()
Game()


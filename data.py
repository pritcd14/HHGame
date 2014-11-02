#############################################################################################################
# GAME DATA                                                                                                 #
#############################################################################################################

DirectionsArray = \
['SE',  'WE',   'WE',   'SWE',  'WE',   'WE',   'SWE',  'SW',
'NS',   'SE',   'WE',   'NW',   'SE',   'W',    'NSE',   'NSW',
'NS',   'NS',   'SE',   'WE',   'NSW',  'SE',   'NSW',  'NS',
'N',    'NS',   'NSE',  'WE',   'NSWE', 'NSW',  'NS',   'NS',
'S',    'NSE',  'NSW',  'S',    'NS',   'N',    'N',    'NS',
'NE',   'NSW',  'NE',   'NW',   'NSE',  'WE',   'W',    'NS',
'SE',   'NSW',  'E',    'WE',   'NW',   'SE',   'SWE',  'NW',
'NE',   'NWE',  'WE',   'WE',   'WE',   'NWE',  'NWE',  'W']

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

DVerbList = {"HELP, COMMANDS, VERBS, OBJECTIVES": "Display the objective and all commands",
             "CARRYING, INVENTORY, INV, ITEMS": "Display the items you are carrying",
             "GO": "Move in a specified direction",
             "N": "Specify you want to move North",
             "S": "Specify you want to move South",
             "W": "Specify you want to move West",
             "E": "Specify you want to move East",
             "GET, TAKE": "Take an item from the room",
             "USE": "Use an item",
             "OPEN": "Open a door",
             "UNLOCK": "Unlock a door/prop",
             "EXAMINE": "Examine your surroundings (info about room)",
             "DIG": "Dig a hole",
             "SCORE, SC": "Display your score",
             "DROP": "Drop an item",
             "MAP, M": "Show/Hide the map"}

NounList = ['NORTH',   'SOUTH',  'WEST',   'EAST',    'UP',   'DOWN',
            'DOOR',    'BATS',   'GHOSTS', 'X2ANFAR', 'SPELLS', 'WALL']

PropList = ['DRAWER',  'DESK', 'COAT', 'RUBBISH', 'COFFIN', 'BOOKS']

PositionOfProps = [43, 43, 32, 3, 38, 35]

ItemList = ['PAINTING', 'RING',      'MAGIC SPELLS', 'GOBLET', 'SCROLL', 'COINS', 'STATUE',  'CANDLESTICK', 'MATCHES',
            'VACUUM',   'BATTERIES', 'SHOVEL',       'AXE',    'ROPE',   'BOAT',  'AEROSOL', 'CANDLE',      'KEY']

PositionOfItems = [46, 38, 35, 50, 13, 18, 28, 42, 10, 25, 26, 4, 2, 7, 47, 60, 100, 100]

MapEnabled = True
QUIT = False
LocationID = 0
YES = "1"
NO = "0"
INVALID = "-1"
WINNING_SCORE = 17
WINNING_ROOM = 57

VisitedPlaces = []
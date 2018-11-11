'''
This contains multiple dictionaries of different enemies, weapons, and so on
'''
from random import choice
from monster import Monster
from player import Player
import colorama as C

# Damage to be used for skills usually equals to player's current dmg
INITIAL_DMG = 0

# Constants
# This is the list of tags to be displayed in inventory
INVENTORY_TAGS = ['food', 'weapon', 'armor']

# Text constants
BULLET = '  > '
SEP = ' ● '
# The color used to highlight name with which the user can interact
HIGHLIGHT_COLOR = C.Fore.MAGENTA
# General color constants
CYAN = C.Fore.CYAN
WHITE = C.Fore.WHITE
BRIGHT = C.Style.BRIGHT
DIM = C.Style.NORMAL

# Weapon dict keys
FIST = 'fist'
DAGGER = 'dagger'
SWORD = 'sword'
BOW = 'bow'
# Rooms/items dict keys
NAME = 'name'
USERDESC = 'userdesc'
DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
DIRECTIONS = [NORTH, SOUTH, EAST, WEST, UP, DOWN]
# Item specific dict keys
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
PICKABLE = 'pickable'
PRICE = 'price'
EDIBLE = 'edible'
WEAPON = 'weapon'
TAG = 'tag' # Tags can be food, weapon, random, decor

# DATA DICTIONARIES
MONSTER_VARIATION = ['Ruthless', 'Ferocious', 'Demonic',
                     'Brutal', 'Bloody', 'Violent', 'Wild', 'Spooky',
                     'Murderous', 'Fierce', 'Savage', 'Monsterous',
                     'Hideous', 'Grotesque',
                    ]

'''Stores specie names and its equivalent stats
in a dictionary, 2 word names must be separated
with a "dash (-)"
'''
MONSTER_SPECIES = {
    #Specie         |  NAME  | HP |  DMG  |  ACTION |
    'chicken':      ['Chicken', 1, 1,      'pinched'],
    'archer':       ['Archer', 1, 2,          'shot'],
    'spider':       ['Spider', 2, 1,           'hit'],
    'scorpion':     ['Scorpion', 1, 3,       'stung'],
    'guard':        ['Guard', 2, 2,        'punched'],
    'wolf':         ['Wolf', 3, 1,            'bit'],
    'werewolf':     ['Werewolf', 3, 2,        'bit'],
    'alligator':    ['Alligator', 3, 3,       'bit'],
    'bear':         ['Bear', 4, 2,      'slashed at'],
    'ogre':         ['Ogre', 5, 3,         'slammed'],
    'pbag':         ['Punching-Bag', 10, 0,       ''],
    'spbag':        ['Super-Punching-Bag', 999, 0,''],
}

'''
Stores of weapons and their equivalent dmg, weapon names
start with a capital letter
'''
WEAPONS = {
    #           NAME --> DMG --> VERB
    FIST   :  ['Fist',   1,   'punched'],
    DAGGER :  ['Dagger', 2,   'stabbed'],
    SWORD  :  ['Sword',  3, 'sliced at'],
    BOW    :  ['Bow',    1,   'shot at'],
}

'''
Stores player skills
'''
SKILLS = {
    'NONE': {
        'name'    : 'None',},
    'DOUBLE_TROUBLE': {
        'name'    : 'Double Trouble',
        'function': Player.double_trouble,
        'message' : 'twice in quick succession',
        'dmg'     : None,
        'ismulti' : False,
        },
    'ARROW_STORM': {
        'name'    : 'Arrow Storm',
        'function': Player.arrow_storm,
        'message' : 'You throw deadly arrows on all enemies',
        'dmg'     : 2,
        'ismulti' : True,
        },
    }

ROOMS = {
    'town_square': {
        NAME: 'Town Square',
        USERDESC: '''You are in the middle of the square, with streets
                     surrounding you from all directions''',
        DESC: 'There is many people around, they all seem busy',
        NORTH: None,
        SOUTH: 'butchery',
        EAST: 'bakery',
        WEST: 'house_63',
        UP: None,
        DOWN: None,
        GROUND: ['fountain', 'apple', 'bread', 'coin'],
        SHOP: [],
    },
    'house_63': {
        NAME: 'House 63 (Ground)',
        USERDESC: 'You are inside an old, deserted house. You see a dark staircase upwards',
        DESC: 'This house looks like it is going to collapse',
        NORTH: None,
        SOUTH: None,
        EAST: 'town_square',
        WEST: None,
        UP: 'house_63_1',
        DOWN: None,
        GROUND: ['coin', 'coin'],
        SHOP: [],
    },
    'house_63_1': {
        NAME: 'House 63 (Attic)',
        USERDESC: 'You are in a dark, gloomy attic, There is a staircase downwards',
        DESC: 'Everything is untouched, covered in dust.',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: 'house_63',
        GROUND: ['dagger'],
        SHOP: [],
    },
    'bakery': {
        NAME: 'Bakery',
        USERDESC: 'You are looking at various kinds of delicious pastry, making your stomach growl',
        DESC: 'The air smells of warm, tasty bread',
        NORTH: None,
        SOUTH: None,
        WEST: 'town_square',
        EAST: None,
        UP: None,
        DOWN: None,
        GROUND: [],
        SHOP: ['bread', 'cake'],
    },
    'butchery': {
        NAME: 'Butchery',
        USERDESC: '''You are at the Butchery's entrance, You observe an old man
                     as he sharpens his knife''',
        DESC: 'The air smells of meat and blood, It is unclean and stinky',
        NORTH: 'town_square',
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: None,
        GROUND: [],
        SHOP: ['beef'],
    },
}

# coin items and their prices (Must use the exact name as their counterpart in ITEMS)
# A sack contains 10x items, its value depend on the contained item's value
COIN_VALUE = {
    'coin': 1,
    'gold coin': 7,
    'coins sack': 10,
    'gold coins sack': 70,
}

# GROUNDDESC is splitted into two, because later the item will be
# colored and insered between them
ITEMS = {
    'apple': {
        NAME: 'Apple',
        GROUNDDESC: ['An', 'lies in the dirt'],
        SHORTDESC: 'a red, shiny apple',
        LONGDESC: 'This is a delicious, edible fruit. Perhaps you can eat it.',
        PICKABLE: True,
        EDIBLE: True,
        TAG: 'food',
    },
    'cake': {
        NAME: 'Cake',
        GROUNDDESC: ['A lovely vanilla', 'is inside a box placed on ground'],
        SHORTDESC: 'a tasty vanilla cake',
        LONGDESC: '''This delicious treat was baked with lover at the Grand
                     Bakery, made from authentic vanilla and chocochips''',
        PICKABLE: True,
        PRICE: 20,
        EDIBLE: True,
        TAG: 'food',
    },
    'bread': {
        NAME: 'Bread',
        GROUNDDESC: ['A loaf of', 'lies on ground'],
        SHORTDESC: 'a warm bread loaf',
        LONGDESC: 'This bread is full of carbohydrates it can easily satisfy your hunger',
        PICKABLE: True,
        PRICE: 5,
        EDIBLE: True,
        TAG: 'food',
    },
    'fountain': {
        NAME: 'Fountain',
        GROUNDDESC: ['A white', 'is streaming water'],
        SHORTDESC: 'a fabulous, marble fountain',
        LONGDESC: 'This beautiful sculpture is emanating water, attracting various kinds of birds.',
        PICKABLE: False,
        EDIBLE: False,
        TAG: 'decor',
    },
    'dagger': {
        NAME: 'Dagger',
        GROUNDDESC: ['A rusty', 'is thrown on the ground'],
        SHORTDESC: 'a rusty, old dagger',
        LONGDESC: '''This dagger, ancient and rusty as it is, is still sharp enough
                     to be used as a weapon.''',
        PICKABLE: True,
        EDIBLE: False,
        WEAPON: WEAPONS[DAGGER],
        TAG: 'weapon',
    },
    'coin': {
        NAME: 'Coin',
        GROUNDDESC: ['A bronze', 'is dropped on the ground'],
        SHORTDESC: 'a bronze coin',
        LONGDESC: '''This is a bronze coin, You can spend it at any shop in exchange
                     for useful goods''',
        PICKABLE: True,
        EDIBLE: False,
        TAG: 'coins',
    },
    'sword': {
        NAME: 'Sword',
        GROUNDDESC: ['An old', 'is laying on the ground'],
        SHORTDESC: 'An old battered Sword',
        LONGDESC: 'This sword is old and battered but is still better than a dagger',
        PICKABLE: True,
        EDIBLE: False,
        WEAPON: WEAPONS[SWORD],
        TAG: 'weapon',
    },
    'meat': {
        NAME: 'Meat',
        GROUNDDESC: ['Some', 'on the ground'],
        SHORTDESC: 'Dried Meat',
        LONGDESC: 'Dried Meat of some unknown animal',
        PICKABLE: True,
        EDIBLE: True,
        PRICE: 8,
        TAG: 'food',
    },
    'bow': {
        NAME: 'Long Bow',
        GROUNDDESC: ['A nice', 'is layingon the ground'],
        SHORTDESC: 'A long bow',
        LONGDESC: 'A durable handmade long bow',
        PICKABLE: True,
        EDIBLE: False,
        PRICE: 10,
        WEAPON: WEAPONS[BOW],
        TAG: 'weapon',
    }
}

def set_skills_dmg():
    SKILLS['DOUBLE_TROUBLE']['dmg'] = INITIAL_DMG * 2
    SKILLS['ARROW_STORM']['dmg'] = 2

# ASCII FUNCTIONS
# Displays a nice looking banner, multi-lines are supported
def banner(text, corner='+', border='-'):
    max_length = 0
    _text = text.split('\n')
    # Checks max line length
    for line in _text:
        if len(line) > max_length:
            max_length = len(line)
    sides = corner + border * max_length + corner
    final_text = [sides]
    for line in _text:
        dif = 0
        if len(line) != max_length:
            dif = max_length - len(line)
        final_text.append('|{}{}|'.format(line, ' ' * dif))
    final_text.append(sides)
    return '\n'.join(final_text)

# True if text start with vowel and vice versa
def use_an(text):
    if text[0] in 'aeiou':
        return True
    else:
        return False

# EXTRACTOR FUNCTIONS
def give_monster(specie, use_special_name=False):
    my_specie_stats = MONSTER_SPECIES[specie]
    x = Monster(my_specie_stats[0], my_specie_stats[1], my_specie_stats[2], my_specie_stats[3])
    if use_special_name:
        # Generating a name using MONSTER_VARIATION
        adjective = choice(MONSTER_VARIATION)
        MONSTER_VARIATION.remove(adjective)
        x.name = '{} {}'.format(adjective, x.name)
    return x

# Returns rooms exits as a dictionary of {DIRECTION: DESTINATION, ...}
def get_room_exits(room):
    exits = {}
    for direct in DIRECTIONS:
        if room[direct]:
            exits[direct] = ROOMS[room[direct]][NAME]
        else:
            pass
            # exits[dir] = str(None)
    return exits

# Returns items GROUNDDESC as bullet points
def get_items_grounddesc(room, item_look=None):
    text = ''
    for item_name in room[GROUND]:
        item = ITEMS[item_name]
        # Add item GROUNDDESC to be displayed
        text += '{} {} {}'.format(BULLET + item[GROUNDDESC][0],
                                  HIGHLIGHT_COLOR + item[NAME].lower() + WHITE,
                                  item[GROUNDDESC][1] + '\n')
    return text

# Returns items SHORTDESC as bullet points
def get_items_shortdesc(item_names):
    text = ''
    for item_name in item_names:
        item = ITEMS[item_name]
        # Add item SHORTDESC to be displayed
        text += BULLET + item[SHORTDESC] + '\n'
    return text

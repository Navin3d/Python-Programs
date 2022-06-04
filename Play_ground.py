import os, random
from termcolor import colored
from time import sleep
from config import *

# Importing module specified in the config file
art = _import_(f'arts.{artFile}', globals(), locals(), ['*'])

def replaceMuliple(mainString, toBeReplace, newString):
    """[Replace a set of multiple sub strings with a new string]

    Args:
         mainString ([string]): [String in which the replacement will be done]
         toBeReplace ([list]): [A list which elements will be replaced by a newString]
         newString ([string]): [A string which will be replaced in place of elements of toBeReplace]

    Returns:
        [string]: [Rtrun the main string where the element of toBeReplace is replaced by newString]
    """

    # Iterate over the list to be replaced
    for elem in toBeReplace :
        # Check if the element is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)

    return mainString

def pprint(art,time ):
    color_used = [random.choice(color)]
    colorAttribute = []
    for i in range(len(art)):
        if art[i] in colorCodes:
                # Color atrr set to blink if 9
            if art[i] == '9':
                colorAttribute = [colorCodes[art[i]]]
            # color attr none if 10
            elif art[i] == '10':
                colorAttribute = []
            # Random colour if R
            elif art[i] == 'R':
                color_used = color
            else:
                color_used = [colorCodes[art[i]]]
        print(colored(replaceMuliple(art[i],colorCodes,''),random.choice(color_used),attrs=colorAttribute),sep='', end='',flush= True);sleep(time)

        def pcode():
            # Print the code before wishing
            if codePrint:
                for i in range(len(art.code)):
                    print(art.code[i], sep='', end='', flush= True);sleep(codingSpeed)
                input('\n\n' +colored('python3','blue')+colored( 'PyBirthdaywish.py','yellow'))
                os.system( 'cls' if os.name == 'nt' else 'clear')
            else:
                input()

 # Clearing terminal
os.system( 'cls' if os.name == 'nt' else 'clear')
pcode()
pprint (art.mainArt, speed)
input()
python3 PyBirthdayWish.py

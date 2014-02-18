'''
Created on Feb 11, 2014

@author: chemla
'''

from fonction import *
import sys

def main():
    pendu = GameManager()
    pendu2 = GameManager()
    print (range(2,3))
    while pendu.__lose__() == False and pendu.__victory__()==False:
        pendu.__putLetter__(pendu.__askLetter__())
        pendu.__print__()

    print ("Fin du jeu !")
    return 0

if __name__ == '__main__':
    main()

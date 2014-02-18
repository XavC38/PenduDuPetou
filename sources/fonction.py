'''
Created on Feb 11, 2014

@author: chemla
'''
import random
import sys

class Player:
    def __init__(self,l=8):
        self.l = l 
        
    def __str__(self):
        if self.l==1:
            return "ENCORE UN COUP COMME CA ET TU ES MORT !!"
        elif self.l == 3:
            return "ATTENTION : plus que trois chances"
        else:
            return "Il vous reste " + str(self.l) + " vies"

class Biblio:
    myWords = {}
    
    def __init__(self, myWayToBiblio):
        myBiblio = open(myWayToBiblio, "r")
        i = 0
        for line in myBiblio:
            self.myWords[i] = line[0:len(line)-1]
            i+=1
        myBiblio.close()
    
class Word:
    
    def __init__(self):
        #getting the Biblio
        myBiblio = Biblio("biblio.txt")
        rand = random.randint(0,len(myBiblio.myWords)-1)
        self.theWord = myBiblio.myWords[rand]
        
        #construction of the Hidden Word
        self.goodLetter = self.theWord[0] + self.theWord[-1]
        
    
    def __right__(self):
        for car in self.theWord:
            if car not in self.goodLetter:
                print("*"),
            else:
                print(car),
        print("")
    
    def __str__(self):
        self.__right__()
        return ""
    

def singleton(class_define):
    instances = {}
    def get_instance():
        if class_define not in instances:
            instances[class_define]=class_define()
        return instances[class_define]
    return get_instance

@singleton
class GameManager:
    def __init__ (self):
        self.myWord = Word()
        self.player = Player()
        print ("Le jeux commence : ")
        print (self.myWord)
        
    def __victory__(self):
        for car in self.myWord.theWord:
            if car not in self.myWord.goodLetter:
                return False
        print("VICTOIRE !!")
        return True

            
    def __lose__(self):
        if self.player.l == 0:
            print ("YOU LOOSE :(")
            return True
        else:
            return False
    
    def __askLetter__(self):
        myLetter = raw_input("Entrer une lettre :")   
        while (len(myLetter)!=1 or myLetter in self.myWord.goodLetter):
            if len(myLetter)!=1:
                print("Vous ne devez entrer qu'une lettre")
                myLetter = raw_input("Entrer une lettre")
            if (myLetter in self.myWord.goodLetter):
                print("Vous avez deja entree cette lettre")
                myLetter = raw_input("Entrer une lettre")
        return myLetter
    
    def __putLetter__(self, aLetter):
        if aLetter in self.myWord.theWord :
            self.myWord.goodLetter += aLetter
        else : 
            self.player.l -= 1
    
    def __print__(self):
        print (self.myWord)
        
    

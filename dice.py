#Importing 'random' 
import random


#function to show dice
def show_dice(no):
  if(no == 1):
    print(" - - - ")
    print(" - + - ")
    print(" - - - ")
  if(no ==2):
    print(" - - + ")
    print(" - - - ")
    print(" + - - ")
  if(no == 3):
    print(" - - + ")
    print(" - + - ")
    print(" + - - ")
  if(no ==4):
    print(" + - + ")
    print(" - - - ")
    print(" + - + ")
  if(no == 5):
    print(" + - + ")
    print(" - + - ")
    print(" + - + ")
  if(no ==6):
    print(" + - + ")
    print(" + - + ")
    print(" + - + ")


#input variable
q = input("Roll Dice(y/n) >> ")


if(q == 'y'):  

    #random number
    no = random.randint(1,6)

    #showing output
    show_dice(no)

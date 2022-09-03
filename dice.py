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
response = input("Roll Dice(y/n) ? >> ")


while response == 'y' :

    #random number
    no = random.randint(1,6)

    #showing output
    show_dice(no)
    response = input("Reroll dice(y/n) ? >> ")

if(response == 'n'):
    print('...Thank you for rolling...')
 

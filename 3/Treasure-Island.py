from tkinter.constants import RIGHT

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road.'Where do you want to go?")
way = input('Type "left" or "right"\n') #Option
if way == 'right'and 'left':
    print("You fell into hole. Game Over!") # for right
else:
    print("You've welcome to lake. There is an Island in the middle of lake.") #for left
    forward= input("Type 'wait' to wait a boat. Type 'swim' to swim across.\n") # Option
    if forward == 'swim'and 'wait':
        print("You get attacked by an angry throat. Game Over!") #for swim
    else:
        print("You arrive at the Island unharmed. There is a house 3 doors.") #for wait
        doors= input("one yellow, one red, and one blue. Which color do you choose.\n") # Option
        if doors== 'red' and 'yellow':
            print("It is room full of fire. Game Over!") #for red
        elif doors== 'blue' and 'yellow':
            print("You enter a room of beasts. Game Over!") #for blue
        else:
            print("You found the treasure! You Win!") # for yellowror
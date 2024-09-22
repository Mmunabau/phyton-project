# treasure_island_GAME
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`." . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
start1 = input(" your at a crossroad, where do to go ? Type left or right ?").lower()
if start1 == " left":
    start2 = input("you come to a lake.There is an island in the middle of the lake. Type \"wait\" to wait ffor a boat.Type \"swim\" to swim across. ").lower()
    if start2 == "wait":
        start3 = input("You arrived on the island unharemed.There is a house with 3 doors. one red,one yellow and one blue. Which colour do you choose?").lower()
        if start3 == "red":
            print("it's a room full of fire.GAME OVER")
        elif start3 == "yellow":
            print("you found the treasure. You win!")
        elif start3 == "blue":
            print("you enter a room of beasts.Game Over")
        else:
            print("you choose a door that doesn't exist.GAME OVER")
    else:
       print("you got attacked by an angry trout.Game over")
else:
    print("you fell into a hole. Game over.")

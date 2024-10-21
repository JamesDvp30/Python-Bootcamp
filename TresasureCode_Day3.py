print('''-------------------------------------------------------------------------
   |               .--.          .--.          /
  \|/      O  /\   |--.|  .-.   /    \        /
 --*--    ( ) \/\--|__|+./  |  /      `-- -- '
  /|\    (__.) \___      \  `-'
   |    (__ _.)   |     X |  - In space,
        |XXxx)    /Oooo/\/     no one
        |XXX/    /     \/      can eat
        |XX/    /  .|  |       ice cream
        |X/     \  \|  |
       
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print(("You are at a crossroad. Where do you want to go? Type 'left' or 'right'\n"))
input1 = input()
if input1 == "right":
          print("You fell into a hole. Game Over.")
elif input1 == "left":
          print("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
          input2 = input()
          if input2 == "wait":
                    print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow")
                    input3 = input()
                    if input3 == "red":
                              print("Burned by fire. Game Over.")
                    elif input3 == "blue":
                              print("Eaten by beasts. Game Over.")
                    elif input3 == "yellow":
                              print( "You Win!")
                    else: 
                              print("Game Over.")
                              
          else: 
                    print("Attacked by trout. Game Over.")
                            
else:
          print("Game Over")
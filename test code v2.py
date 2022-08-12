
"""This code is a type of game.  The operators that are in the code are from another game called tom clancy's rainbow six siege.  The operators are different people with different abilities.  They use them to take out the opponents. The person will hopefully get to choose the ability when I code it."""   
import random

# initialising variables and constants
ATTACKERS_R6 = ["ash","hibana","zofia","sledge","iq"]
DEFFENDERS_R6 = ["smoke","azami","tachanka","frost","kapkan"]
SISTER_RIVALY = ["zofia won ella lost this round","ela won zofia sadly lost a round"]
VALID_MENU_CHOICE = ["1","2","3","4","5"]
user_choice = ""

# print a menu and get user choice, validate their choice.
"""Welcome to operator picker, please pick 1,2,3,4,5 or 6, oparators are in a game called Tom Clancys rainbow six siege.  It a 5v5 gamemode.
the game has diffrent oparators to choose from, but this time the computer will choose for you :) 

    1. ATTACKERS_R6, 5 oparators for the computer to choose on attack.  All the attackers have diffrent abilies but im not gonna be able to code it in.

    2. DEFFENDERS_R6, 5 oparatoers for the computer.  The deffenders have diffrent abilities with frost having a human bear trap, smoke having a gas grenade that kills people that stand or go though the posiones smoke.choose on deffence 

    3. Both sides, = 10 oparators over all for the computer to randomly genarate choose

    4. Exit

    5. Zofia and Ela are sister rivals, they both hate each becuase Zofia was the favorite child other Sisters fight, if you choose 5 one will win and one will lose the battle"""

user_choice = input("Please enter you can only choose 5 numbers")
print("remember you can press 4 at anytime to end the code and stop the code from running")




while user_choice != "4":
   le 

hoice in VALID_MENU_CHOICE

user_choice = input("choose a number bettwen 1 - 5 please")
    elif user_choice == "1":
        print(random.choice(ATTACKERS_R6))
        print(random.choice(DEFFENDERS_R6))
        user_choice = input("please enter")
        print("If you want to leave just press 4")
    if user_choice == "2":
        print(random.choice(ATTACKERS_R6))
        print(random.choice(DEFFENDERS_R6))
        user_choice = input("please enter anyother number than 5 and over")
        print("If you want to leave just press 4")
    if user_choice == "3":
        print(random.choice(ATTACKERS_R6))
        print(random.choice(DEFFENDERS_R6))
        user_choice = input("please any other numbers")
    if user_choice == "5":
        print(random.choice(SISTER_RIVALY))
        user_choice = input("please enter another number")
    
   
    

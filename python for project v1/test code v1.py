   
import random

# initialising variables and constants
ATTACKERS_R6 = ["ash","hibana","zofia","sledge","iq"]
DEFFENDERS_R6 = ["smoke","azami","tachanka","frost","kapkan"]
SISTER_RIVALY = ["zofia won ella lost this round","ela won zofia sadly lost a round"]
THE_SECRET_NUMBER = ["6"]
VALID_MENU_CHOICE = ["1","2","3","4","5","6"]
user_choice = ""

# print a menu and get user choice, validate their choice.

print("""Welcome to operator picker, please pick 1,2,3,4,5 or 6
    1. ATTACKERS_R6, 5 oparators for the computer to choose on attack
    2. DEFFENDERS_R6, 5 oparatoers for the computer to
    choose on deffence 
    3. Both sides, = 10 oparators over all for the computer to randomly genarate choose
    4. Exit""")
user_choice = input("Please enter you can only choose 5 numbers")
print("remember you can press 4 at anytime to end the code and stop the code from running")

while user_choice != "4":

    
    while not user_choice in VALID_MENU_CHOICE:
        user_choice = input("choose a number bettwen 1 - 5 please")

    if user_choice == "1":
        print(random.choice(ATTACKERS_R6))
        print(random.choice(DEFFENDERS_R6))
        user_choice = input("please enter")
        print("If you want to leave just press 4")
        user_choice = input("please any other numbers")
    if user_choice == "5":
        print(random.choice(SISTER_RIVALY))
        user_choice = input("please enter another number")
 
   
    

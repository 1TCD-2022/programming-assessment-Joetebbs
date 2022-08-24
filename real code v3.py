 #this game is a random choice oparator, you choose a number and the game chooses for you    
import random

# initialising variables and constants
Revived_attackers = ["ash came back to life"," Hibana came back to life"," Zofia came back to life"," sledge came back to life"] 
ATTACKERS_R6 = ["ash rushed in and died, smokes gas grande","hibana fell in frosts bear trap","zofia was backstabbed by ella","sledge got a kill and survived","iq died to kapkans entery denile device ","iq survied"]
DEFFENDERS_R6 = ["smoke killed ash with his smoke grenade ","azami","Ella backstabbed Zofia","frost killed Hibana with her human bear trap","kapkan killed iq"]
SISTER_RIVALY = ["zofia won ella lost this round","ela won zofia sadly lost a round"]
THE_SECRET_NUMBER = ["6"]
VALID_MENU_CHOICE = ["1","2","3","4","5","6","y","n"]
user_choice = ""


# print a menu and get user choice, validate their choice.

print("""Welcome to operator picker, please pick 1,2,3,4,5 or 6, oparators are in a game called Tom Clancys rainbow six siege.  It a 5v5 gamemode.
the game has diffrent oparators to choose from, but this time the computer will choose for you :) 

    1. ATTACKERS_R6, 5 oparators for the computer to choose on attack.  All the attackers have diffrent abilies but im not gonna be able to code it in.

    2. DEFFENDERS_R6, 5 oparatoers for the computer.  The deffenders have diffrent abilities with frost having a human bear trap, smoke having a gas grenade that kills people that stand or go though the posiones smoke.choose on deffence 

    3. Both sides, = 10 oparators over all for the computer to randomly genarate choose

    4. Exit

    5. Zofia and Ela are sister rivals, they both hate each becuase Zofia was the favorite child other Sisters fight, if you choose 5 one will win and one will lose the battle""")

user_choice = input("Please enter you can only choose 5 numbers")
print("remember you can press 4 at anytime to end the code and stop the code from running")

while user_choice != "4":


    
    while not user_choice in VALID_MENU_CHOICE:
        user_choice = input("choose a number bettwen 1 - 5 please")

    if user_choice == "1":
        print(random.choice(DEFFENDERS_R6))
        print(random.choice(DEFFENDERS_R6))
        print(random.choice(Revived_attackers)) 
        user_choice = input("please enter")
        print("If you want to leave just press 4")
        print(DEFFENDERS_R6)
        print("this is all the options you could have gotten") 



    if user_choice == "2": 
        print(random.choice(ATTACKERS_R6))
        print(random.choice(ATTACKERS_R6))
        user_choice = input("please enter anyother number than 5 and over")
        print("this is all the options you could have gotten")
        print(ATTACKERS_R6)
        
        
        print("If you want to leave just press 4")
    if user_choice == "3":
        print(random.choice(ATTACKERS_R6))
        print(random.choice(DEFFENDERS_R6))
        user_choice = input("please any other numbers")
    if user_choice == "5":
        print(random.choice(SISTER_RIVALY))
        user_choice = input("please enter another number")
    
    import random
MY_NUMBER = random.randint(1,100)

user_guess = int(input("guess my number bettwen 1 and 100 "))

while user_guess != MY_NUMBER :
    if user_guess < MY_NUMBER :
       user_guess = int(input("your too low try again: "))
    else:
        user_guess = int(input("your too high try again: "))

print("yay you got it looks like you will survie")   


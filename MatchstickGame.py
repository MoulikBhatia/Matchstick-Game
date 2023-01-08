#Matchstick Game
from random import *
ms=21
U1=True
U2=True
U3=True
while True:
    print("""
        ----------------------------------------------------------
        |                      MAIN MENU                         |
        ----------------------------------------------------------
        |                                                        |
        |                                                        |
        |                 [1] Play Game                          |
        |                 [2] How to play?                       |
        |                 [3] Credits                            |
        |                                                        |
        |    Enter the respective number to select an option     |
        |                                                        |
        ----------------------------------------------------------
        """)
    C1=int(input("Enter Your choice:  "))
    if C1==1:
        print("Game Start\n")
        while ms>2:
            print("Current number of matchsticks:",ms)
            while U1:
                try:
                    a=int(input("Enter the amount of matchsticks you would like to remove:"))
                except ValueError:
                    print("Please print numbers from 1 to 3 only")
                    if a==1 or a==2 or a==3:
                        U1=False
                    else:
                        print("Please choose numbers from 1 to 3")
            ms-=a
            b=randrange(1,4)
            print("The AI takes ",b,"number of matchsticks from the pile")
            ms-=b 
        while ms==2:
            print("Current number of matchsticks:",ms)
            while U2:
                try:
                    a=int(input("Enter the amount of matchsticks you would like to remove:"))
                except ValueError:
                    print("Please print numbers from 1 to 3 only")
                    if a==1 or a==2:
                        U2=False
                    else:
                        print("Please choose numbers from 1 to 2")
            ms-=a
            if ms==0:
                break
            b=randrange(1,3)
            print("The AI takes ",b,"number of matchsticks from the pile")
            ms-=b
        while ms==1:
            print("Current number of matchsticks:",ms)
            while U3:
                try:
                    a=int(input("Enter the amount of matchsticks you would like to remove:"))
                except ValueError:
                    print("Please print numbers from 1 to 3 only")
                    if a==1:
                        U3=False
                    else:
                        print("Please choose numbers from 1 to 2")
            ms-=a
            if ms==0:
                break
            b=randrange(1,2)
            print("The AI takes ",b,"number of matchsticks from the pile")
            ms-=b
        if (ms+a)-a==0:
            print("Sorry you lost the game! Try again?")
        elif (ms+b)-b==0:
            print("Hooray! You won!")
    if C1==2:
            print('''
            ----------------------------------------------------------
                                   HOW TO PLAY
            ----------------------------------------------------------
                How to play:
                    1. The game will ask for inputs in this pattern:''')
            ext1=input()
            if ext1==ext1:
                pass       
                
    if C1==3:
        print('''
        ----------------------------------------------------------
        |                       CREDITS                          |
        ----------------------------------------------------------
        |                                                        |
        |   1. Moulik Bhatia                                     |
        |   2. Khanak Jindal                                     |
        |                                                        |
        |   XI - A and C                                         |
        |   Source code available at:                            |
        |   https://github.com/MoulikBhatia/Matchstick-Game      |
        |                                                        |
        |   LICENSED UNDER THE MIT LICENSE                       |
        |                                                        |
        ----------------------------------------------------------
        |              PRESS ANY KEY TO GO BACK                  |
        ----------------------------------------------------------''')
        ext1=input()
        if ext1==ext1:
                pass
    else:
        print("""
INVALID INPUT!
        """)
        pass

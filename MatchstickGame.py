#Matchstick Game
from random import *
from time import *
ms = 21
U1 = True
U2 = True
U3 = True
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
    if C1 == 1:
        sleep(1)
        print("Game Start\n")
        while ms > 2 :
            sleep(1)
            print("\nCurrent number of matchsticks:",ms)
            inp_str = input("\nEnter the amount of matchsticks you would like to remove:")
            
            try :
                inp_int = int(inp_str)
            except :
                print('\nPlease enter a numeric value between 1 and 3')
                break

               
            while U1 == True:  
                sleep(1)
                if inp_int == 1 or inp_int == 2 or inp_int == 3:
                    ms = ms - inp_int
                    b = randrange(1,4)
                    sleep(1)
                    print("\nThe AI takes ",b,"number of matchsticks from the pile")
                    ms = ms - b
                    break
                else :
                    sleep(0.61)
                    print("\nPlease choose numbers from 1 to 3")
                    break
                    
            if ms > 2 :
                continue
            else :
                break
                
                    
        while ms==4:
            sleep(1)
            print("\nCurrent number of matchsticks:",ms)
            inp_str2 = input("\n\nEnter the amount of matchsticks you would like to remove:")
                
            try :
                inp_int2 = int(inp_str2)
            except :
                print("\nPlease print numbers from 1 to 3 now")
                continue
            if inp_int2 == 3:
                ms = 1
                sleep(1)
                print('\nThe AI takes 1 matchsticks from the pile')
                print('\nSorry you lost the game! Try again?')
                break
        while ms==3:
            print("\nCurrent number of matchsticks:",ms)
            inp_str2 = input("\n\nEnter the amount of matchsticks you would like to remove:")
                
            try :
                inp_int2 = int(inp_str2)
            except :
                print("\nPlease print numbers from 1 to 3 now")
                continue
            if inp_int2 == 3:
                print('\nHooray! You won!')
                sleep(1)
                break           
            
        while ms == 2:
            print("\nCurrent number of matchsticks:",ms)
            inp_str2 = input("\n\nEnter the amount of matchsticks you would like to remove:")
                
            try :
                inp_int2 = int(inp_str2)
            except :
                print("\nPlease print numbers from 1 to 2 now")
                continue
                        
            if inp_int2 == 1:
                ms = 1
                print('\nThe AI takes 1 matchsticks from the pile')
                print('\nSorry you lost the game! Try again?')
            elif inp_int2 == 2:
                print('\nHooray! You won!')
                sleep(1)
                break
            else :
                print("\nPlease choose numbers from 1 to 2 now")
                break
                
                
                
        while ms == 1:
            print("\nCurrent number of matchsticks:",ms)
            inp_str3 = input('\n\nEnter the amount of matchsticks you would like to remove:')
            
            try:
                inp_int3 = int(inp_str3)
            except :
                print("\nPlease choose numbers from 1 to 3 only")
                continue
            
            if inp_int3 == 1:
                print('\nHooray! You won!')
                sleep(1)
                break
            else :
                print('\nYou moron cannot even pick out 1 on 1 matchstick! Throw away your PC!')
                
    if C1==2:
            sleep(1)
            print('''
        ----------------------------------------------------------
        |                  HOW TO PLAY                           |
        ----------------------------------------------------------
        | How to play:                                           |
        |                                                        |
        |1. The game will ask for number of matchsticks to add.  |
        |                                                        |
        |                                                        |
        |2. Enter your desired amount of matchsticks from 1 to   |
        |   3 and continue until you reach zero.                 |
        |                                                        |
        |                                                        |
        |3.AI or user, the first one to reach zero wins.         |
        ----------------------------------------------------------
        |                  PRESS ANY KEY TO GO BACK              |
        
        ----------------------------------------------------------''')
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
    

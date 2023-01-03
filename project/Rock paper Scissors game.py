# Rock Paper and Scissors game
import random


cn=["rock","paper","scissor"]
'''
rock.vs.paper->.paper.wins
rock.vs.scissor->.rock.wins
paper.vs.scissor->.scissor.wins
'''

while True:
    Ccount=0
    ucount=0
    uc=int(input('''
    Game Start.....
    1 Yes
    2 No | Exit

    '''))

    if uc==1:
        for a in range(1,6):
            userinput= int(input('''
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==3:
                uchoice="paper"
            Cchoice=random.choice(cn)
            if Cchoice==uchoice:
                print("Computer Value",Cchoice)
                print("User Value", uchoice)    
                print("Game Draw")
                ucount=ucount+1
                Ccount=Ccount+1
            elif (uchoice=="rock"and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer Value",Cchoice)
                print("User Value", uchoice)
                print("you win")
                ucount=ucount+1
            else:
                print("Computer Value",Cchoice)
                print("User Value", uchoice)
                print("Computer win")
                Ccount=Ccount+1
        if ucount==Ccount:
            print("Final Game Draw....")
            print("user Score",ucount)
            print("Computer Score",Ccount)
        elif ucount>Ccount:
            print("Final you win the Game....")
            print("user Score",ucount)
            print("Computer Score",Ccount)
        else:
            print("Final Computer win the Game....")
            print("user Score",ucount)
            print("Computer Score",Ccount)


    else:
        break
import random
def tictac():
    count=0 # A count that will record the amount of turns taken within the game.
    win= False #Win has been set to false as no one has won the game
    userselection=[]
    computerselection= [] #The list where the Computer choices will be stored
    winningoutcomes = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[7,5,3],[1,5,9]] #This list contains the winning list combinations
    print("User is X")
    while count !=9: #While the count does not equal 9, as that is the maximum number of turns in tic-tac-tie.
        print("X will begin")
        userchoice = int(input("Enter a number between 1 and 9: ")) #User can select a choice between 1 and 9
        if userselection not in winningoutcomes: #If the user's choice is not in winning outcomes
            if computerselection not in winningoutcomes: # and If the computer choice is not in user outcomes
                if userchoice not in userselection or userchoice not in computerselection: #If the user choice is not included within their own choices or user choices
                    userselection.append(userchoice) #Will add the user choice into the list
                    count = count + 1
                    print("You placed your X in position",userchoice) #Will identify to the user where they placed their placeholder
                    computerchoice = random.randint(1,9) #The computer will randomly select a number
                    if computerchoice not in userselection or computerchoice not in computerselection: #If the computer selection is not included within the user or current user chocie
                        computerselection.append(computerchoice)#Will add it to the list of Computer choices
                        print("Computer placed their O in position",computerchoice)
                        count = count + 1
                    else:
                        computerchoice = random.randint(1,9) #if the choice is in user solection - then will re-select a number.
                else:
                    print("This poisition has already been filled")
                    userchoice= int(input("Enter a number between 1 and 9: ")) #If User enters a number already used, then they will have to re-enter it
            else:
                print("Player O, the computer, has won!") #If the computer has a winning combination, then they will win.
        else:
tictac() #Calls the Function to begin the game


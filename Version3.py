import random
board_setup = [1,2,3,4,5,6,7,8,9] #A list containing the positions on the board
winningoutcomes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]#A 2-D array that will contain the winning combinations on the board
players = ["X","O"] # A list containing the different players that can be selected within the game
def tictac(): #The first function that will be called to initate the game
    play = True
    amountofplayers = int(input("How Many Players(Max 2)? ")) #The user is able to select the amount of players - Deciding if the user will play against another user, or the computer
    if amountofplayers == 1: # If the User selects 1 player, then they will play against the computer
        playernum = random.randint(0, 1) # This will randomly select a position in the list between 0 and 1, to choose a player for the user
        if playernum == 0: #if the selection is in the first position on the list (Position 0)
            player1 = players[0] # The User will be X (Position "0")
            print("Player is", player1)
            x = "User" #X will be assigned to the user
            computer = players[1] #The computer will be O, (Position "1)
            print("computer is", computer)
            o = "Computer" #O will be assigned to the computer
        else: #If the random selection is in position 1, it will assign the opposite
            player1 = players[1]
            print("Player is", player1)
            o = "User"
            computer = players[0]
            print("Computer is", computer)
            x = "Computer"
    else: #If the user selects 2 players, they will play against another user
        player1 = players[0] #Player 1 will be assigned to X
        print("Player 1 is X")
        x = "User 1"
        player2 = players[1] #Player 2 will be assigned to O
        print("Player 2 is O")
        o = "User 2"
    def board():
        print("|",board_setup[0],"|",board_setup[1],"|",board_setup[2],"|") # This will display the board in a table format, displaying the contents of the list based upon the position
        print("|",board_setup[3],"|",board_setup[4],"|",board_setup[5],"|") # For example, if board_setup[0] would display "1" to the user.
        print("|",board_setup[6],"|",board_setup[7],"|",board_setup[8],"|")
    def playernumber():
        while play == True: #While the game is in process
            userselection = int(input("Enter a Number Between 1 and 9: ")) #The user can enter a number between 1 and 9, based upon the position on the board
            userselection = userselection - 1 #Due to the list starting from position 0, we subtract 1 from the number selected to correspond correctly with the board
            if userselection >= 0 and userselection <=9: #If the number is in range
                return userselection
            else:
                print("Incorrect; Input out of range. Enter again.")
                continue #If the number is out of range, then the loop will restart
    def computernumber():
            computerselection = random.randint(0,8)
            return computerselection # The program will select a random number between 0 and 8, based upon the corresponding position on the board
    def player1go():
        print("Player 1's Go")
        player1choice = playernumber() # The ouput of the Playernumber function would be stored in a variable to be used
        if board_setup[player1choice] == "X" or board_setup[player1choice] == "O": # If the position is filled in the table
            print("Space already filled by an", board_setup[player1choice])
            player1go() #Identify the user that the space is filled, then re-iterate the execution of the function
        else:
            board_setup[player1choice] = str(player1) #Fill the position the user selected with the player1 character choice
    def player2go():
        print("Player 2's go")
        player2choice = playernumber() #The output of the playernumber() function will be stored in the Player 2 Choice varuable
        if board_setup[player2choice] == "X" or board_setup[player2choice] == "O":
            print("Space already filled by an", board_setup[player2choice])
            player2go()
        else:
            board_setup[player2choice] = str(player2) #The selection of player 2 will be filled with the player2 character choice
        
    def computergo():
        computerchoice = computernumber()
        if board_setup[computerchoice] == "X" or board_setup[computerchoice] == "O":
            computergo() #If the computer choice is filled by either character, it will re-iterate the function to make another random selection
        else:
            print("Computer Selected",computerchoice + 1)
            board_setup[computerchoice] = str(computer)
    def playerwin():
        count = 0 #The count selection will begin at 0 from the start of the game.
        for win1,win2, win3 in winningoutcomes: #For 3 individual items in each 1-D array within the 2-D array of Winning outcomes
            if board_setup[win1] == board_setup[win2] == board_setup[win3] == "X": #If any 3 Win combinations are filled with an X
                print("Player X,",x,",Wins")
                playagain = input("Do you wish to play again? ").lower()
                if playagain == "yes" or playagain == "y": #If the user wants to play again
                    tictac()
                else:
                    exit() # The player, X, has won the game and the user does not want to play again. The game will finish with the program stopping execution
            if board_setup[win1] == board_setup[win2] == board_setup[win3] == "O": #If any 3 Win Combinations are filled with an O
                print("Player O,",o,",Wins")
                playagain = input("Do you wish to play again? ").lower()
                if playagain == "yes" or playagain == "y": #If the user wants to play again
                    tictac() #Will Restart the game
                else:
                    exit()  # The player, O, has won the game and the user does not want to play again. The game will finish with the program stopping execution
        for game in range(0,9): # As there are 9 selections on the board, if this is reached, then  the game should end
            if count < 9: # If the maximum number of goes is not reached
                if board_setup[game] == "X" or board_setup[game] == "O": #If any position on the board is filled
                    count += 1 #One will be added to the count for each go
            else: #If the maximum number of goes is reached
                print("It is a Tie!")
                playagain = input("Do you wish to play again? ").lower()
                if playagain == "yes" or playagain == "y": #If the user wants to play again
                    tictac() #Will Restart the game
                else:
                    exit()  # No one has won and the user does not want to play again. The game will finish with the program stopping execution
    while play != False: #While the Game is still in play, as play = True, the game will continue.
        board() # In each Go, the board will be displayed.
        if amountofplayers == 1: #If the user selected one player, the functions with the player and computer will be called.
            playerwin() #Will check the board before each go
            player1go() #Will allow the user to make a selection
            computergo() #Will make a selection for the computer
            playerwin() #WIll do a final check of the board
        else: #If the user selected 2 players, the functions with player 1 and player 2 will be called.
            player1go() #Will allow the first user to make a selection
            playerwin() #Will do the first check before users make a decision
            player2go() #Will allow the second user to make a selection
            playerwin() #Will do the second check after users make a decision
tictac()


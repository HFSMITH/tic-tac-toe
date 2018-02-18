import random
board_setup = [1,2,3,4,5,6,7,8,9] #A list containing the positions on the board
winningoutcomes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]#A 2-D array that will contain the winning combinations on the board
players = ["X","O"] # A list containing the different players that can be selected within the game
def tictac():
    count = 0
    play = True
    playernum = random.randint(0,1)  # This will randomly select a position in the list between 0 and 1, to choose a player for the user
    if playernum == 0:  # if the selection is in the first position on the list (Position 0)
        player1 = players[0]  # The User will be X (Position "0")
        print("Player is", player1)
        x = "User"  # X will be assigned to the user
        computer = players[1]  # The computer will be O, (Position "1)
        print("computer is", computer)
        o = "Computer"  # O will be assigned to the computer
    else:  # If the random selection is in position 1, it will assign the opposite
        player1 = players[1]
        print("Player is", player1)
        o = "User"
        computer = players[0]
        print("Computer is", computer)
        x = "Computer"
    def board():
        print("|",board_setup[0],"|",board_setup[1],"|",board_setup[2],"|") # This will display the board in a table format, displaying the contents of the list based upon the position
        print("|",board_setup[3],"|",board_setup[4],"|",board_setup[5],"|") # For example, if board_setup[0] would display "1" to the user.
        print("|",board_setup[6],"|",board_setup[7],"|",board_setup[8],"|")
    def playernumber():
        while play == True:  # While the game is in process
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
    def playergo():
        playerchoice = playernumber()  # The ouput of the Playernumber function would be stored in a variable to be used
        if board_setup[playe1choice] == "X" or board_setup[playerchoice] == "O":  # If the position is filled in the table
            print("Space already filled by an", board_setup[player1choice])
            player1go()  # Identify the user that the space is filled, then re-iterate the execution of the function
        else:
            board_setup[playerchoice] = str(player)  # Fill the position the user selected with the player1 character choice
            count += 1 #Will add one to the coutner during the game for each go
    def computergo():
        computerchoice = computernumber()
        if board_setup[computerchoice] == "X" or board_setup[computerchoice] == "O":
            computergo()  # If the computer choice is filled by either character, it will re-iterate the function to make another random selection
        else:
            print("Computer Selected", computerchoice + 1)
            board_setup[computerchoice] = str(computer)
            count += 1 # Will add one to the counter during the game for each go
    def playerwin():
        for win1,win2, win3 in winningoutcomes: #For 3 individual items in each 1-D array within the 2-D array of Winning outcomes
            if board_setup[win1] == board_setup[win2] == board_setup[win3] == "X": #If any 3 Win combinations are filled with an X
                print("Player X,",x,",Wins")
                exit() # The player, X, has won the game and it will be identified to the user. The game will finish with the program stopping execution
            if board_setup[win1] == board_setup[win2] == board_setup[win3] == "O": #If any 3 Win Combinations are filled with an O
                print("Player O,",o,",Wins")
                exit() #The Player, O, has won the game. The game will finish with the program stopping in execution.

    while play != False:  # While the Game is still in play, as play = True, the game will continue.
        if count < 9: #As long as the count is below 9
            board() #Display the board
            playerwin() #Check the board for winning combinations
            playergo() # Will call the function to allow the user to make a selection
            computergo() #WIll call the function for the program to make a selection
            playerwin() # Final check for winning combinations
        else: #Once the count reaches 9
            print("The Game is a tie!")
            exit() #The game is a tie, and the program will stop execution
tictac()
#SHAM (Stanley Huang and Abeera Mohyuddin)
#Friday, June 14th, 2013
#Course Summative - 21

#Define Inital Variables
playerContinue = True        #Loop for the player to continue
computerContinue = True      #Loop for the computer to continue
playAgain = True             #allows user to play again
cardCounter = 0              #Keeps track of the cards durring the hand
playerTotal = 0              #Keeps track of the user's number until 21
computerTotal = 0            #Keeps track of the computer's number until 21
playerScore = 0              #Keeps track of the player's score
computerScore = 0            #Keeps track of the computer's score
tieScore = 0                 #Keeps track of the number of ties


#Defining custom functions

#Define random card function
def randomSuit():
    import random                    #import random function
    number = random.randint(1,4)     #random number between 1 - 4 (the four different signs)
    if number == 1:                  #returning the suits
        return "♠"
    elif number == 2:
        return "♥"
    elif number == 3:
        return "♦"
    else:
        return "♣"

#Defining random card function (converts card value to A, J, Q, K)
def randomCard(card):
    if card == 1:                   #Output proper signs for user
        return "A"
    elif card == 11:
        return "J"
    elif card == 12:
        return "Q"
    elif card == 13:
        return "K"
    else:
        return card

#Defining random card value function
def cardValue():
    import random                      #import random function
    number = random.randint(1,13)      #recieve random number (from A - K = 13)
    return number                      #return number


#main code body
print("Welcome to SHAM21\nProduced by SHAM INC.\n")  #welcome to game

#while loop to give user option to play again
while playAgain:
    print("Enter the number of rounds you would like to play.")      #Ask user for number for round variable
    round = int(input())


    #loop body until the amount of rounds entered
    for i in range(0, round):
        print("\n------\nRound:"+ str(i + 1)+"\n------")      #print out amount of rounds


        #player draws cards loop
        while playerContinue:
            cardCounter = cardCounter + 1     #keeps track of the amount of cards drawn
            suit = randomSuit()               #defining suit; randomSuit's ouput 
            value = cardValue()               #defining value; value of card
            card = randomCard(value)          #defining card; randomCard's output
            cardOutput = str(card) + suit     #card output is the card number plus suit 

            #if the value of the card is J, Q or K
            if value > 10:
                value = 10                    #convert value to 10

            print("\nYou Drew:",cardOutput)   #outputs what user drew 
        
            #if the player drew an ace
            if value == 1:
                aceInput = True

                
                #keeps looping while they enter a correct value
                while aceInput == True:
                    print("\nWhat would you like your ace to value to be, Enter 1 or 11")
                    aceValue = int(input())

                    #if the user enters 1, value is 1, else it is 11
                    if aceValue==1:
                        value = 1
                        aceInput = False
                    elif aceValue ==11:
                        value = 11
                        aceInput = False
                    else:                #If user enters anything but 1 or 11, program gives error
                        print("\nInvalid Number")

                
            playerTotal=playerTotal+value   #Add card's value to player's total
            
            #output the card they are on and what there number is at
            print("Card:"+ str(cardCounter), "Your number is at", str(playerTotal),"("+str(value)+"+"+str(playerTotal-value)+")")

            #If the playerTotal is 21 or the player has drawn 5 card...
            if playerTotal == 21 or (cardCounter == 5 and playerTotal < 21):  
                playerTotal = 0.1                                       #Set playerTotal to win 
                cardCounter = 0                                         #Set cardCounter back to zero 
                playerContinue = False                                  #playerContinue and computerContinue is set to false 
                computerContinue = False
                break
            
            #if the playerTotal is more then 21, the computer wins the round 
            elif playerTotal > 21:
                computerTotal = 0.1
                cardCounter = 0
                playerContinue = False
                computerContinue = False
                break
        
            #Ask if user wants to continue
            print("Press enter to continue, otherwise press h to hold or press q to quit")
            userInput = input()
        
            #If user wants to quit, the game ends
            if userInput == "q":
                computerContinue = False
                cardCounter = 0
                break

            #if a user wants to hold then it skips to computer continue
            elif userInput == "h":
                cardCounter = 0
                break



        #Another loop for the computer to play 
        while computerContinue:
            cardCounter = cardCounter + 1   #Set cardCounter 
            suit = randomSuit()             #draw card 
            value = cardValue()
            card = randomCard(value)
            
            if value > 10:              #converts J, Q, K values to 10
                value = 10

            #Output what the computer drew 
            print("Computer Drew", str(card) + suit)
        
            if value == 1:                          #If the computer draw an Ace, if it does not go over 21 at the value 
                if (computerTotal + 11) > 21:       #of 11, then ace is set to 11, otherwise ace is set to 1 
                    value = 1
                else:
                    value = 11
                    
            computerTotal = computerTotal + value      #add to the number
            
            #print the card number and the computer's number
            print("Card:"+str(cardCounter), "Computer Number is at:"+ str(computerTotal),"("+str(value)+"+"+str(computerTotal-value)+")")


            #Ask if user wants to continue
            print("Press enter to continue, otherwise press q to quit")
            userInput = input()
        
            #if a user quits then the game ends
            if userInput == "q":
                computerContinue = False
                playerContinue = False
                cardCounter = 0
                break

            #If the computerTotal is more then or equal to 18, round finishes
            if computerTotal == 21 or (cardCounter == 5 and computerTotal < 21):
                computerTotal = 0.1
                cardCounter = 0
                playerContinue = False
                computerContinue = False

            #if computerTotal is more than 21 the round ends
            elif computerTotal > 21:
                playerTotal = 0.1
                cardCounter = 0
                computerContinue = False
                playerContinue = False

            #if the total is 18 or above then the computer will stop playing
            elif computerTotal >= 18:
                computerContinue = False
                playerContinue = False
                cardCounter = 0

        #if a user wants to quit this breaks the main loop
        if userInput == "q":
            break
    
        #Decide winner of the round 
        if (playerTotal == computerTotal):                  #If the computer and user has the same score, they tie and
            print("\n------\nYou Tied, No Points will be awarded\n------")    #no points are given 
            tieScore = tieScore + 1

        #player wins 
        elif playerTotal == 0.1:                                    #if the computer wins
            print("\n------\nPlayer wins this round\n------")
            playerScore = playerScore + 1                          #add to score

        #computer wins 
        elif computerTotal == 0.1:
            print("\n------\nComputer wins this round\n------")
            computerScore = computerScore + 1
        
        #player wins 
        elif  playerTotal>computerTotal:
            print("\n------\nPlayer wins this round\n------")
            playerScore = playerScore + 1

        #computer wins 
        else:
            print("\n------\nComputer wins this round\n------")
            computerScore = computerScore + 1

        #reset for next hand
        playerContinue = True
        computerContinue = True
        cardCounter = 0
        computerTotal = 0
        playerTotal = 0

        #Output if user won 
        print("\nScores for this hand\nPlayer:", str(playerScore)+"\nComputer:", str(computerScore)+"\nTies:", str(tieScore))

        #Ask if user wants to continue
        print("Press enter to continue, otherwise press q to quit")
        userInput = input()
    
        #if a user quits
        if userInput == "q":
            computerContinue = False
            playerContinue = False
            cardCounter = 0
            break
        if userInput == "q":
            break




    #Output if user won 
    print("\n------\nEnd of Game\n------\nScores\nPlayer:", str(playerScore)+"\nComputer:", str(computerScore)+"\nTies:", str(tieScore))

    #determines the winner of the round
    if playerScore > computerScore:     #If the player score is more then the computer's score, player wins 
        print("\n------\nYou Win\n------")

    #If user and computer have the same score, it is a tie 
    elif playerScore == computerScore:  
        print("\n------\nYou Tied\n------")

    #Otherwise, the computer score is higher, thus the user loses
    else:
        print("\n------\nYou Lost\n------")             

    #reset scores
    playerScore = 0
    computerScore = 0
    print("Play Again? (y/n)")         #Ask user if they want to play again
    
    #ends the game and rolls credit
    if input() == "n":
        playAgain = False
    
print("\n\n------\nThanks for playing!\n------\n")         #Copyright info
print("© 2013 SHAM INC.")
print("No part of this game or any of it's contents")
print("may be reproduced, copied, modified or adapted")
print("without the prior written consent of the programmers,")
print("unless a licence has been approved by Abeera Mohyuddin and Stanley Huang.")
print("Commercial use and distribution of the contents of the game is not allowed")
print("without express prior consent of the progammers")

# Euler Difficulty 10%


def pokerHands():
    pokerTXT  = open("EulerProblems/PokerHands.txt", "r") 
    handsData = pokerTXT.readlines()
    player1WinCount = 0

    for hand in handsData:
        player1Values = ""
        player2Values = ""
        player1SameSuit = True
        player2SameSuit = True

        #Getting Values of Hand
        for ii in range( 0 , 13 , 3):
            player1Values += hand[ii]
        for ii in range( 15 , 28 , 3):
            player2Values += hand[ii]

        #Testing Same Suit
        for ii in range( 4 , 14 , 3):
            if (hand[ii] != hand [1]): # if any Card is Wrong suit do this:
                player1SameSuit = False
                break
        for ii in range( 19 , 29 , 3):
            if (hand[ii] != hand [16]): # if any Card is Wrong suit do this:
                player2SameSuit = False
                break
        #Tests ToDo 
        #hard with  Letters Solution: J:=11 Q=12 ... 
        #Time intensive|not interesting
    return player1WinCount
               


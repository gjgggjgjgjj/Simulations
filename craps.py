import random

#this doesn't need parameters as a tuple will always return
def rollDice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1+die2
    return(die1,die2,total)

#this will a function to rollDice for a Game (until a seven gets rolled after the firstroll)
#this will update curWins so that wins and losses are together as a 
#curWins will use a list with the first index being wins and losses, then the third one being dollars
def crapRound(curWins, curBet):

    if len(curWins) != 3:
        print("ERR:The list into crapRound is greater than 3 or less than 3")
        return

    leRoll1 = rollDice()
    curNumPoint = None

    if (leRoll1[2] == 7) or (leRoll1[2] == 11):
        curWins[2] += curBet
        curWins[0] += 1
        return 
    elif (leRoll1[2] == 2) or (leRoll1[2] == 3) or (leRoll1[2] == 11):
        curWins[1] += 1  #losses increment
        curWins[2] -= curBet
        return
    else:
        curNumPoint = leRoll1[2]


    #game has started and we play towards the point
    looping = True
    while looping:
        looping = False
        pointRoll = rollDice()
        if pointRoll[2] == curNumPoint:
            curWins[0] += 1
            curWins[2] += curBet
        elif pointRoll[2] == 7:
            curWins[1] += 1
            curWins[2] -= curBet
        else:
            looping = True

    return


def loopLogic(budget, loserPullOut, winnerPullOut, betamount):

    winLossCash = [0,0,budget]
    highestDollar = budget

    while winLossCash[2] >= loserPullOut:

        if winLossCash[2] > highestDollar:
            highestDollar = winLossCash[2]

        #to pull out and win
        if highestDollar >= winnerPullOut:
            break

        print(winLossCash)
        crapRound(winLossCash, betamount)

    
    print("\n\n=========================================================================================================\nAt the end of everything the most you made was:", highestDollar)
    totalgames = winLossCash[0] + winLossCash[1]
    print("\n--------------------------------------------------\nYou played",totalgames,"total games with",winLossCash[0],"wins and ",winLossCash[1],"losses")
    print("You went in with ",budget,", and you left with ", winLossCash[2])



def userPlay():
    print("Hello! Welcome to craps!!!\n\nThe way this works is we are gonna try and play craps smartly.")
    print("I am going to ask you the amoutn of money you are bring in, then when you want to pullout from both profit and when you are losing too much past the budget")
    print("the last thing i'll ask is how much you want to bet each round")
    print("-------------------------------------------------------------------------------------------------------------")

    budget = int(input("Enter me how much money we are bringing in?  ------> "))
    loserPullOut = int(input("What's the lowest amount for when we need to cut our losses? ------> "))
    winnerPullOut = int(input("Okay how much over the amount of money we bring when should we leave the casino with profit? ------> "))
    betamount = int(input("Lastly how much are we betting each round??  ------> "))

    loopLogic(budget, loserPullOut, winnerPullOut, betamount)
    
    

def main():
    userPlay()


if __name__ == "__main__":
    main()


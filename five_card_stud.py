import random
import math

#here is a dictionary of the current wins
winDictionary = {
    "royal flush": 0,
    "straight flush": 0,
    "four of a kind": 0,
    "full house": 0,
    "flush": 0,
    "straight": 0,
    "three of a kind": 0,
    "two pair": 0,
    "pair": 0,
    "high card": 0,
}

#this just pulls random number from the deck of cards without repeats
def fiveDrawn():
    curHand = random.sample(range(52),5)
    print(curHand)
    return curHand

#here we need to define if the deck is a winning hand or just in general the ranking on it
def theCardRank(theHand, windic):
    #0-12 is spades
    #13-25 clubs
    #26-38 diamonds
    #39-51 hearts
    #suit = index //13
    #rank = index %13
    #index = suit * 13 + rank
    

    #hashmap of suites
    hashsuit = [0,0,0,0]
    #hashmap of rank
    hashrank = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    #bool of hands atm
    pair = 0
    threepair = False
    fourpair = False
    straight = False
    flush = False
    fullhouse = False
    straightflush = False 
    royalflush = False


    #this evaluates the rank and suit
    for i in theHand:
        
        cursuit = i // 13
        rank = i % 13
        hashsuit[cursuit] += 1
        hashrank[rank] += 1


    straightcnt = 0
    hasAce = False
    hasKing = False
    if hashrank[0] > 0: #to know if we have an ace
        hasAce = True
    if hashrank[12]:
        hasKing = True

    for i in range(len(hashrank)):
        if hashrank[i] == 0:
            straightcnt = 0
            continue
        if hashrank[i] > 1:
            if hashrank[i] == 2:
                pair += 1
            elif hashrank[i] == 3:
                threepair = True
            elif hashrank[i] == 4:
                fourpair = True
        #this else is evaluating a straight now
        else:
            straightcnt += 1
            if i >= 9:  #evaluating the weird straight with ace on top
                if straightcnt == 4 and hasAce:
                    straight = True
            if straightcnt == 5:
                straight = True

    # checking if we have a suit
    for i in hashsuit:
        if i == 5:
            flush = True


    ##lastly we append to the windic and need to see if we have straight flushes 
    #or if we have full houses
    if pair == 1 and threepair:
        windic["full house"] += 1
        return
    if flush and straight and hasAce and hasKing:
        windic["royal flush"] += 1
        return
    if flush and straight:
        windic["straight flush"] += 1
        return
    if straight:
        windic["straight"] += 1
        return
    if flush:
        windic["flush"] += 1
        return
    if fourpair:
        windic["four of a kind"] += 1
        return
    if threepair:
        windic["three of a kind"] += 1
        return
    if pair == 2:
        windic["two pair"] += 1
        return
    if pair == 1:
        windic["pair"] += 1
        return
    else:
        windic["high card"] += 1
        return

            
#easier to just get the percent
def mathPercentage(total,unitAmount):
    percent = (unitAmount / total) * 100
    return percent

#--------------------------------------
def printResults(totalHands):
    print("\n\n\n\n==========================================================================================")
    for i in winDictionary:
        print(i," : ",winDictionary[i])
    print("\n\n\n\n")
    print("The percentage likelyhood of the hands that came out from this experiment are as follows:")
    print("-------------------------------------------------------------------------------------------")
    for i in winDictionary:
        lePercent = mathPercentage(totalHands,winDictionary[i])
        print(i,"in this experiment occured:","%",lePercent,"amount of time\n")

#just asks user how many times they want to run the sim
def inputAmountRuns():
    amount = int(input("How many times do you wanna run the hands? : ---> "))
    for i in range(amount):
        leHand = fiveDrawn()
        theCardRank(leHand,winDictionary)

    printResults(amount)


def main():
    inputAmountRuns()


if __name__ == "__main__":
    main()

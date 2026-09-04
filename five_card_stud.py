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
def theCardRank(theHand, winDic):
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
    pair = False
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
        rank = % 13
        hashsuit.append(cursuit)
        hashrank.append(rank)


    straightcnt = 0
    hasAce = False
    if hashrank[0] > 0: #to know if we have an ace
        hasAce = True

    for i in range(hashrank):
        if hashrank[i] == 0:
            straightcnt = 0
            continue
        if hashrank[i] > 1:
            if hashrank[i] == 2:
                twopair = True
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

    # checking if we have a suit
    for i in hashsuit:
        if i == 4:
            flush = True


    ##lastly we append to the windic and need to see if we have straight flushes 
    #or if we have full houses
    if pair and twopair:
        windic["full house"] += 1
        return
    if flush and straight and hasAce:
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
        windic["three of a kind"]
        return
    if twopair:
        windic["two pair"] += 1
        return
    else:
        windic["high card"] += 1
        return

            

def printResults(resultsDic):




def inputAmountRuns():
    amount = input("How many times do you wanna ")
                    






def main():


if __name__ == "__main__":
    main()

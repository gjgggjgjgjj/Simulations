from five_card_stud import theCardRank, winDictionary, printResults, mathPercentage #don't know yet
from combinations import cr ,crTwo, cFive

#the combinations of this would be
# cr(6,3) * cr(6,2)
    # then with all those combinations we will see which ones Attacker wins and 
    # how much defender wins
solvedRiskStats = {
    "Attacker Percentage": 0.0,
    "Defender Percentage": 0.0, 
}

#remeber that to get the total cobinations of this its
# p(52,5)
solvedPokerStats = {
    "Royal Flush Percentage": 0.0,
    "Straight Flush Percentage": 0.0,
    "Four Of A Kind Percentage": 0.0,
    "Full House Percentage": 0.0,
    "Flush Percentage": 0.0,
    "Straight Percentage": 0.0,
    "Three Of A Kind Percentage": 0.0,
    "Two Pair Percentage": 0.0,
    "Pair Percentage": 0.0,
    "High Card Percentage": 0.0,
}


#changed this function just a little bit from the original riskSim so now we feed our die into it instead of people
def theAttack(atts, defs):      #attacker die list and def die list
    #making the list of attacker die and defender die
    atList = atts.copy()
    deList = defs.copy()
    atList.sort(reverse=True)   #makes the list sorted so we can compare the highes aggaint highest easily
    deList.sort(reverse=True)

    attpts = 0
    defpts = 0
    #only need to itereate through the defender rolls as the max people that can die are the amoutn of defender rolls
    for i in range(len(deList)):
        if deList[i] >= atList[i]:
            defpts += 1
        else:
            attpts += 1

    retList = [attpts, defpts]
    return retList #who won points


def totalCombRisk():
    #will need to create a list of lists first 
    attListCombos = cr(6)  #returns a list with all combos of cr(6,3)

    defListCombos = crTwo(6)  #returns same as above but with only 2 dice as r is two
    #now we will need to compare every single combinations of these to find our stats
    retTotalPts = [0,0]   #first index is attacker points, second is defender points
    totalPossibleCombinationInt = 0 #we will find this out soon enough

    for attacks in attListCombos:
        for defences in defListCombos:
            #these are dice rolled put into it
            resultPts = theAttack(attacks,defences)
            retTotalPts[0] += resultPts[0]
            retTotalPts[1] += resultPts[1]
            totalPossibleCombinationInt += 2   #because two points are given per round rolled

    attackPercentage = retTotalPts[0]/ totalPossibleCombinationInt
    defenderPercentage = retTotalPts[1]/ totalPossibleCombinationInt
    print("attacker percentage is :", attackPercentage)
    print("defender percentage is :", defenderPercentage)
    print("for testing here is totalPossibleCombinationInt:", totalPossibleCombinationInt)
    print("futher testing here is retTotalPts:", retTotalPts)
    return retTotalPts

#poker sections --------------------------------------------------------
def totalCombPoker():
    #here is total combinations then we'll just go through and test each variation
    totalPokerHands = cFive(52)
    for i in totalPokerHands:
        # print("here is the hand being passed (its a list lol) into theCardRank",i)
        theCardRank(i,winDictionary)

    printResults(len(totalPokerHands))



def main():
    selection = int(input("If you wan't the combo of risk stats press 1 otherwise press 2 for poker -->  "))
    if selection == 1:
        totalCombRisk()
    else:
        totalCombPoker()



if __name__ == "__main__":
    main()
    
        



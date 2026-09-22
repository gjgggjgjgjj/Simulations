import random


#dictionary so that we can know the stats at the end 
statsDic = {
    "Attacker points": 0,
    "Defender points": 0,
    "Number of total battles": 0,
    "Attacker percentage %": 0.0,
    "Defender percentage %": 0.0,
}



def diceRoll():
    #this will be just one dice
    die = random.randint(1,6)
    return die

#people is to determine how many dice the attackers get to have
def attackerRoll(people):
    dice = []
    if people > 3:
        amt = 3
    elif people == 3:
        amt = 2
    elif people == 2:
        amt = 1
    else:   #they can't attack with only one person
        return dice

    for i in range(amt):
        roll = diceRoll()
        dice.append(roll)
    return dice

def defenderRoll(people):
    dice = []
    if people > 1:
        amt = 2
    elif people == 1:
        amt = 1
    else:       #in this case all the defenders are dead and it should not get here
        raise Exception("zero people got passed into defenderRoll")
        return dice

    for i in range(amt):
        roll = diceRoll()
        dice.append(roll)
    return dice

def theAttack(atts, defs):      #takes amount of attackers and defenders and returns the result
    #making the list of attacker die and defender die
    atList = attackerRoll(atts)
    deList = defenderRoll(defs)
    atList.sort(reverse=True)   #makes the list sorted so we can compare the highes aggaint highest easily
    deList.sort(reverse=True)
    print("attacker rolled die ", atList)
    print("defender rolled die ", deList)

    attpts = 0
    defpts = 0
    #only need to itereate through the defender rolls as the max people that can die are the amoutn of defender rolls
    for i in range(len(deList)):
        if deList[i] >= atList[i]:
            defpts += 1
        else:
            attpts += 1

    retList = [attpts, defpts]
    return retList #returns new attacker people and defendder people



#here is the loop of perpetual battles until we find our answer
def tillDeath(runs, attackers, defenders, statsDic):

    for i in range(runs):
        #re init the people to do another run
        attackers = attackers
        defenders = defenders


        while (attackers > 0) and (defenders > 0):
            pointList = theAttack(attackers, defenders)

            statsDic["Attacker points"] += pointList[0]
            statsDic["Defender points"] += pointList[1]

            attackers -= pointList[1]  #for every defender point we lose attackers
            defenders -= pointList[0]  #same but for attackr pts we lose defenders

            statsDic["Number of total battles"] += 1

    totalPtsAwarded = statsDic["Number of total battles"] *2    #since two points are awarded each battle
    statsDic["Attacker percentage %"] = (statsDic["Attacker points"] / totalPtsAwarded) * 100
    statsDic["Defender percentage %"] = (statsDic["Defender points"] / totalPtsAwarded) * 100   #getting the percentages right
    return 


def main():
    
    attackers = int(input("how many attackers "))
    defenders = int(input("how many defenders "))
    ttlRuns = int(input("Tell me how many times should we battle until they all die (runs)?\n-->   "))
    tillDeath(ttlRuns, attackers, defenders, statsDic)
    
    #print all the stuff in the dic
    for i in statsDic:
        print(i,statsDic[i])
        print()




if __name__ == "__main__":
    main()


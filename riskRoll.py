from riskSim import theAttack, diceRoll, attackerRoll, defenderRoll
import random

def askUserCharacter():
    attPeople = int(input("How many attackers? "))
    defPeople = int(input("How many defenders? "))

    print("Okay press enter for a dice roll and people left will be printed")
    while True:
        input("press enter")
        print("-------------------------")

        peopleLeft = theAttack(attPeople,defPeople)
        attPeople -= peopleLeft[1]
        defPeople -= peopleLeft[0]
        print("Attackers left:", attPeople)
        print("Defenders left:", defPeople)
        print()
        
    


def main():
    askUserCharacter()



if __name__ == "__main__":
    main()

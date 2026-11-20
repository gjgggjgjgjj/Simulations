import math
import random 

def isPrimeStandard(num):
    leSqrRoot = math.sqrt(num)
    leSqrRoot = int(leSqrRoot)

    prime = True
    for i in range(2, leSqrRoot + 1):
        if (num % i == 0):
            prime = False

    if (prime):
        print("\n\n",num,":is PRIME")
    else:
        print("\n\n",num,":is COMPOSITE")
    return prime

#use miller-rabin
def isPrimeMonteCarlo(num):
    # small/even numbers so random selection doesn't crash
    if num < 2:
        print("\n\n", num, ":is COMPOSITE (MonteCarlo)")
        return False
    if num in (2, 3):
        print("\n\n", num, ":is PRIME (MonteCarlo)")
        return True
    if num % 2 == 0:
        print("\n\n", num, ":is COMPOSITE (MonteCarlo)")
        return False

    nMinOne = num - 1

    #divide by 2 until we have a base that is odd
    twoBase = 0   #init to 2^0
    divisedNum = nMinOne
    while (divisedNum % 2 == 0):
        divisedNum //= 2
        twoBase += 1

    print(divisedNum,":divisedNum")

    #we have our new base now
    k = 40    #change this to how accurate we want our test
    isPrime = True

    #k rounds with random bases
    for _ in range(k):
        testers = random.randint(2, num - 2)

        #doing first calc because if first one can be 1 or -1
        b0 = pow(testers, divisedNum, num)
        if (b0 == 1 or b0 == num-1):
            continue    #run the rest of the test to further accuracy of being prime

        bs = b0
        passed = False
        for _ in range(twoBase-1):
            # print("am stuck",bs)
            bs = pow(bs, 2, num)
            if (bs == num-1):
                passed = True
                break

        if not passed:
            isPrime = False
            print("\n\n",num,":is COMPOSITE (MonteCarlo)")
            return False

    print("\n\n",num,":is PRIME (MonteCarlo)")
    return isPrime

def main():
    looping = True
    while looping:
        choice = int(input("Hello! test prime numbers here!\n-----------------\nPress 1:isPrimeStandard\nPress 2:isPrimeMonteCarlo\nPress 3:For Both\n--> "))
        number = int(input("\n==============\nWhat number are we testing for primality??\n--> "))
        if (choice == 1):
            isPrimeStandard(number)
        elif (choice == 2):
            isPrimeMonteCarlo(number)
        elif (choice == 3):
            val1 = isPrimeMonteCarlo(number)
            print("\n- - - - - - - - - - - - - - - - -\n")
            print(" - - - - - - - - - - - - - - - - ")
            val2 = isPrimeStandard(number)


        input("...\n--> ")

if __name__=="__main__":
    main()

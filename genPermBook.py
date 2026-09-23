import math
import random

def lexiPerm(n):
    #this will be the list we reorder and print
    # n += 1
    leList = []
    leList = list(range(0,n))
    #keep going until we can't get a bigger number
    #so with 012
    #the highest number will be 210

    #while not false as false means we found the last item
    stillPermutating = True
    print(leList)
    while stillPermutating:
        keepGoing = next_permutations(leList)
        if keepGoing == False:
            stillPermutating = False
        else:
            leList = keepGoing
            print(leList)

def next_permutations(leList):

    #first find largest index j such that p[j] < p[j + 1]
    j = len(leList) - 2   #im starting from the second to last index
    while j >= 0 and leList[j] >= leList[j+1]:
        j -= 1

    #if nothing exists then we have the latgest number
    if j < 0:
        print(leList)
        return False

    #second find largest index k suck that p[j] < p[k]
    k = len(leList)-1
    while leList[j] >= leList[k]:
        k -= 1
 
    #now that we found it we must swap them
    leList[j], leList[k] = leList[k], leList[j]

    #reverse sund
    left = j + 1
    right = len(leList) - 1
    while left < right:
        leList[left], leList[right] = leList[right], leList[left]
        left += 1
        right -= 1

    return leList

def next_combination(c, n, r):
    """
    generates the next r-combination from {1, 2, ..., n in-place
    returns True if a next combination exists, or False if done
    """
    i = r - 1
    while i >= 0 and c[i] == n - r + i + 1:
        i -= 1

    
    if i < 0:
        return False

    #increment c[i]
    c[i] += 1

   #
    for j in range(i + 1, r):
        c[j] = c[j - 1] + 1

    return True

def lexiComb(n, r):
    # Initial combination 1, 2, ..., r
    c = list(range(1, r + 1))
    
    # the initial combination
    print(" ".join(map(str, c)))

    # generating and printing until no more
    while next_combination(c, n, r):
        print(" ".join(map(str, c)))

def main():
    print("IF you want permutations press 1")
    print("IF YOU want combinations press 2")
    choice = int(input("-->  "))

    if choice == 1:
        n = int(input("For this lexicographical sort, type how big you want it (1-9) --> "))
        lexiPerm(n)
    elif choice == 2:
        n = int(input("ENTER N: --> "))
        r = int(input("ENTER R: --> "))
        lexiComb(n,r)

    else:
        #may break but oh well
        print("DIDNt CHOOSE ONE OF THE ANSWERS")
        main()

if __name__ == "__main__":
    main()


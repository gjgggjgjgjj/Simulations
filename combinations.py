#this program generates c(n,r) and p(n,cr) and cr(n,r) and pr(n,r)
#only works for and r=3
#using nested for loops

def pr(n): #r must be 3 for algorithm to work
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range (1, n+1):
                print(i,j,k)

def p(n): #r must be 3 for algorithm to work
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range (1, n+1):
                if i != j and i!= k and j != k:
                    print(i,j,k)

                    """
def p(n): #r must be 3 for algorithm to work
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range (1, n+1):
                if i != j and i!= k and j != k:
                    print(i,j,k)
                    """

def c(n): #r must be 3 for algorithm to work
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range (j+1, n+1):
                print(i,j,k)

def cFive(n)  #r is five

                """
 def c(n): #r must be 3 for algorithm to work
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range (j+1, n+1):
                print(i,j,k)
                    """

def cr(n): #r must be 3 for algorithm to work
    #retlist of the values appended
    #list of lists
    retList = []
    for i in range(1, n+1):
        for j in range(i, n+1):
            for k in range (j, n+1):
                print(i,j,k)
                combo = [i,j,k]
                retList.append(combo)
    return retList

def crTwo(n):  #this results in r being 2
    retList = []
    for i in range(1, n+1):
        for j in range(i, n+1):
            print(i,j)
            combo = [i,j]
            retList.append(combo)
    return retList
 



def main():
    # pr(5)
    # p(5)
    #
    # c(5)
    n = int(input("what do you want n to be? [r with be 3 so cr{n,r}] --> "))
    cr(n)

if __name__=="__main__":
    main()

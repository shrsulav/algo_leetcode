import math

'''
arguments:
changeFor       - an integer for which change is to be made
denominations   - a list of change denonminations
'''
def changeMaker(changeFor, denominations):
    changeTable = {'0': 0}
    lastDenomTable = {'0': None}

    for i in range(1, changeFor+1):
        leastNum = math.inf
        for denom in denominations:
            if(denom <= i):
                a = changeTable[str(i-denom)] + 1
                if(a < leastNum):
                    leastNum = a
                    lastDenomTable[str(i)] = denom
        changeTable[str(i)] = leastNum
    n = changeFor
    changes = []
    while n != 0:
        changes.append(lastDenomTable[str(n)])
        n -= lastDenomTable[str(n)]
    
    return changeTable[str(changeFor)],changes 

if __name__=='__main__':
    leastNum, changes = changeMaker(6, [1,3])
    print(leastNum)
    print(changes)
#The getWays function of Hackerrank, finding the number of ways change can be made for an amount of n, given an array c of coins. Dynamic programming approach (tabulation) has been used
def getWays(n, c):    
    print("n=", n)              
    print("c=", c)
    table=[]
    temp=[]
    for i in range(0, n+1):
        if(i%c[0]==0):
            temp.append(1)
        else:
            temp.append(0)
    
    table.append(temp)
    print(table)
    for i in range(1, len(c)):
        temp=[]
        for j in range(0, n+1):
            if(j<c[i]):
                temp.append(table[i-1][j])
            else:
                print("i=", i, "\tj=", j , "j-c[i]=", j-c[i])
                temp.append((table[i-1][j]+temp[j-c[i]]))#Number of ways change can be done EXCLUDING the current coin + Number of ways change can be made INCLUDING the current coin
        table.append(temp)
    print(table)
    return table[len(c)-1][n]
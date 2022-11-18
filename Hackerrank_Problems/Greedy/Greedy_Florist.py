def getMinimumCost(k, c):
    '''
    Case 1: Numer of flowers == Numer of people just add everything in array
    Case 2: Numer of flowers > people. After n-k top priced flowers are taken, we take the next k top priced flower, then the next k top priced flower. Its greedy as everytime we try to take the most priced flower so that as the repeat purchase increases, we have to multiply with a lesser priced value only. Strong assumption: the array is sorted. Example 10 3
    [1,2,3,4,5,6,7,8,9,10]. Here, we first take 8,9,10. Rest 10-3 or 7 flowers left to take. We take 5,6,7 at repeat=1, then take 2,3,4 at repeat=2 and 1 at repeat=3. Each time, use list comprehension to update the values and make sure the indices(a and v) are valid. Final array is [4,6,9,12,10,12,14,8,9,10] then add up the array values.
    '''
    c.sort()
    print("c=",c,"k=",k)
    n = len(c)
    cost = 0
    if(n==k):
        for i in range(0, len(c)):
            cost = cost + c[i]
        print("Cost = ", cost)
        return cost
    else:
        repeat = 1
        left = n - k
        while(left>0):
            a = len(c)-(repeat*k)-1
            v = a - k + 1
            if(a)>=len(c):
                a=len(c)-1
            if(v<0):
                v=0
        
            c = [x*(repeat+1) if index >=v and index<=a else x for index,x in enumerate(c)]
            left = left - k
            repeat = repeat + 1
            print("Updated c=", c)
        for i in range(0, len(c)):
            cost = cost + c[i]
            print("Cost = ", cost)
    return cost
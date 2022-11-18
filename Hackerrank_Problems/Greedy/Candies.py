def candies(n, arr):
    '''
    First pass go left to right, if rank > rank on left child then increase the candies


    Second pass go right to left, if rank is greater than child on right ut candy count is lesser than that for child on right then increase the candy count for current child as child on right's candy count plus one. Look at sample input/output where input=10 arr=[2,4,2,6,1,7,8,9,2,1]
    '''
    
    candies = [1 for x in range(0, len(arr))]
    for i in range(0, len(arr)-1):
        if(arr[i+1]>arr[i]):
            candies[i+1]=candies[i]+1
    for i in range(len(arr)-1,0,-1):
        if(arr[i-1]>arr[i]) and candies[i-1]<=candies[i]:
            candies[i-1]=candies[i]+1
    answer = 0
    for i in range(0, len(candies)):
        answer = answer + candies[i]
    return answer
    
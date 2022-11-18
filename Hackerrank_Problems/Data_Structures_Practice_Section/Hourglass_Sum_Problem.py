def hourglassSum(arr):
    '''
    Input is always 6*6 array like this
    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 2 4 4 0
    0 0 0 2 0 0
    0 0 1 2 4 0
    Compute the hour glass sum and show the largest sum got
    Approach: Similar to convolving, start at center point, add that point, corresponding top layer and bottom layer to get each sum. Since size = 6 and this pattern involves top and bottom patterns, we need to go total_size - 2 times so total_size-1 in range as range goes from start value till end_value-2. Think like convolving 6*6 by 3*3 filter.
    '''
    total = -999 #Cant be 0 as test case 3 and 7 has negative inputs lol
    subpart_total = 0
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            subpart_total = arr[i][j] + arr[i-1][j] + arr[i-1][j-1] + arr[i-1][j+1] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j+1]
            #print(subpart_total)
            #print("adding ", arr[i][j], arr[i-1][j], arr[i-1][j-1],arr[i-1][j+1],arr[i+1][j],arr[i+1][j-1],arr[i+1][j-1])
            if(subpart_total > total):
                total = subpart_total
    #print(total)
    return total
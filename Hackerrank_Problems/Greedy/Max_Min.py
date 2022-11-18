def maxMin(k, arr):
    '''
    Sort the array
    Slide a window of length k over the array
    Find difference of largest and smallest element of the array elements within the sliding window. Largest element = last item in sliding window and smallest element = first item in sliding window. The lowest value thus got after sliding the window over the entire array is the answer.
    Example [1,2,3,4,5,6], k=4
    Sliding window 1 = [1,2,3,4] unfairness=3
    Sliding window 2 = [2,3,4,5] unfairness=3
    Sliding window 3 = [3,4,5,6] unfairness=3
    '''
    arr.sort()
    print(arr)
    answer = 9999999999999999
    i=0
    while(i+k-1<len(arr)):
        print(arr[i+k-1] , "\t ____ ", arr[i])
        unfairness = arr[i+k-1] - arr[i]
        if(unfairness < answer):
            answer = unfairness
        i = i + 1
        print(unfairness)
    return answer   
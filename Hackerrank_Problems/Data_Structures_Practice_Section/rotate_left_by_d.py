'''
Rotate arr to left by d amount
'''
def rotateLeft(d, arr):
    # Write your code here
    d = d % len(arr)
    ans = arr[d:len(arr)+1] + arr[0:d]
    #print(ans)
    return ans

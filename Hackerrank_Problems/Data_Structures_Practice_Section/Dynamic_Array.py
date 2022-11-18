#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#Just do the queries 1 and 2 as mentioned in question.

def dynamicArray(n, queries):
    # Write your code here
    seq = []
    last_answer = 0
    result = []
    for i in range(0, n):
        seq.append([])
    for x in queries:
        if(x[0]==1):
            seq[(x[1]^last_answer)%n].append(x[2])
        else:
            sub_seq = seq[(x[1]^last_answer)%n]
            size = len(sub_seq)
            last_answer = sub_seq[x[2]%size]
            print(last_answer)
            result.append(last_answer)
    return result
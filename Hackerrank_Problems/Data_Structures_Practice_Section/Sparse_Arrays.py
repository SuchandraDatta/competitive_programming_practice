'''
Input: 4
aba
baba
aba
xzxb
3
aba
xzxb
ab
Output: 2
1
0
How many times each term in queries is present in strings array ofc dont use for loops twice.
'''



# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    count = 0
    ans = []
    for term in queries:
        count = 0
        print(len(list(filter(lambda s: s==term, strings))))
        ans.append(len(list(filter(lambda s: s==term, strings))))
    return ans
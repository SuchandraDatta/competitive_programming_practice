s=input("")
s = [ x+"#" for x in s ]
s = "#" + "".join(s)

R = 0
C = 0
P = [0 for i in range(0, len(s))]
for i in range(0, len(s)):
    iprime = 2*C - i;
    #If i<R, initialize P[i] with the minimum of R-i and P[iprime] or mirror of i
    if(i<R):
        if((R-i)<P[iprime]):
            P[i]=R-i
        else:
            P[i]=P[iprime]
    
    flag=0
    #Keep expanding as far as possible with center as i
    while(flag==0):
                right = i+P[i]+1
                left = i-1-P[i]
                #print("left = ", left, "\tright= ", right)
                if((left>=0 and right>=0) and (left<len(s) and right<len(s))):
                    #print(s[left],"==",s[right])
                    if(s[left] == s[right]):
                        P[i]=P[i]+1
                        #print(P)
                    else:
                        flag=1
                else:
                    flag=1
    #If suitable, update R
    if(R<=i+P[i]):
            R=i+P[i]
            C=i
            

#Final P list, max in P is length of longest palindromic substring and index of that is the C of final answer. R is C+length of longest palindromic substring and the L value is mirror of R around C.          
C = 0
high = 0
for i in range(0,len(P)):
    if(high<=P[i]):
        high=P[i]
        C=i
        
'''print(C)
print(R)
print(P)'''
R = C+P[C]
s_ans = s[2*C-R:R+1]
s_ans = "".join([ x for x in s_ans if(x!='#') ])
print(s_ans)
#Passed 8 test cases of Hackerrank, 8th test case is a test where all inputs = a and so the answer = a for required length. Basically input = output which wasn't working as left > 0 was done at 23 by mistake.
#THIS WORKED ON HACKERRANK AND LEETCODE

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = [ x+"#" for x in s ]
        s = "#" + "".join(s)

        R = 0
        C = 0
        P = [0 for i in range(0, len(s))]
        for i in range(0, len(s)):
            iprime = 2*C - i;
            if(i<R):
                if((R-i)<P[iprime]):
                    P[i]=R-i
                else:
                    P[i]=P[iprime]
    
            flag=0
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
    
            if(R<=i+P[i]):
                R=i+P[i]
                C=i
            

    
        C = 0
        high = 0
        for i in range(0,len(P)):
            if(high<=P[i]):
                high=P[i]
                C=i
        
        R = C+P[C]
        s_ans = s[2*C-R:R+1]
        s_ans = "".join([ x for x in s_ans if(x!='#') ])
        print(s_ans)
        return s_ans
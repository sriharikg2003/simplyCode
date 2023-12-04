

def LCS(str1,str2,dp):
    if str1=="" or str2=="":
        return 0
    if str1==str2:
        dp[str1+','+str2]=len(str1)
        dp[str2+','+str1]=len(str1)

        return len(str1)
    
    try:
        return dp[str1+','+str2]
    except:
        try:
            return dp[str1+','+str2]
        except:
            if str1[-1]==str2[-1]:  
                dp[str1+','+str2]=1 + LCS(str1[:-1],str2[:-1],dp)
                dp[str2+','+str1]=dp[str1+','+str2]
                return  dp[str1+','+str2]
            else:
                dp[str1+','+str2] = max( LCS(str1[:],str2[:-1],dp) , LCS(str1[:-1],str2[:],dp))
                dp[str2+','+str1]=dp[str1+','+str2]
                return  dp[str1+','+str2]
    
dp = dict()
dp[","]=0



"""
USING HASH 
"""
class Solution(object):
    def LCS(self, str1, str2, dp):
        if str1 == "" or str2 == "":
            return 0

        # Use a hash function to generate a unique key for the memoization dictionary
        key = hash((str1, str2))

        if key in dp:
            return dp[key]

        if str1[-1] == str2[-1]:
            dp[key] = 1 + self.LCS(str1[:-1], str2[:-1], dp)
        else:
            dp[key] = max(self.LCS(str1, str2[:-1], dp), self.LCS(str1[:-1], str2, dp))

        return dp[key]

    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = {}
        return self.LCS(text1, text2, dp)


"""
USING DP
"""

def LCSv2(m,n,str1,str2,dp):
    if m==0 or n==0:
        return 0
    
    if dp[m][n]!=-1:
        return dp[m][n]
    if str1[-1]==str2[-1]:  
        dp[m][n]=1 + LCSv2(m-1,n-1,str1[:-1],str2[:-1],dp)
        return   dp[m][n]
    else:
        dp[m][n] = max( LCSv2(m,n-1,str1[:],str2[:-1],dp) , LCSv2(m-1,n,str1[:-1],str2[:],dp))
        return   dp[m][n]
    
text1 = "abcde"
text2 = "ace" 
dp =[ [-1 for i in range(len(text1)+1)] for k in range(1+len(text2))]
for i in range(len(text1)+1):
    dp[0][i]=0
for i in range(len(text2)+1):
    dp[i][0]=0
for i in dp:
    print(i)

LCSv2(len(text2),len(text1),text2,text1,dp)

for i in dp:
    print(i)

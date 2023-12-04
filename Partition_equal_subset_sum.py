# Partition Equal Subset Sum

def ispart(nums):
    s = sum(nums)
    if s%2!=0:
        return False
    s = int(s/2)
    dp = [[False for i in range(s+1)] for k in range(len(nums))]


    for row in range(len(nums)):
        for col in range(1,s+1):
            if dp[row][col]!= True:         
                if nums[row]==col:
                    for i in range(row,len(nums)):
                        dp[i][col]=True
                elif (row-1>=0) and (col-nums[row]>=0):
                    if dp[row-1][col-nums[row]]:                    
                        for i in range(row,len(nums)):
                            dp[i][col]=True

    return dp[-1][-1]


if __name__ == '__main__':
    nums = [1,2,3,8]
    print(ispart(nums)) 

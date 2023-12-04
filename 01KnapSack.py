

def PRINT(arr):
    for i in arr:
        print(i)



if __name__ == '__main__':

    capacity = 10
    weights = [1,3,4,6]
    value = [20,30,10,50]
    dp = [[0 for i in range(capacity+1)] for i in range(len(weights)+1)]


    for row in range(1,len(weights)+1):
        for col in range(1,capacity+1):
            if col< weights[row-1]:
                dp[row][col] = dp[row-1][col]
            else:
                dp[row][col] = max ( dp[row-1][col] , value[row-1] + dp[row-1][col-weights[row-1]])
    PRINT(dp)   

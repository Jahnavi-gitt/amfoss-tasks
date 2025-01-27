def countWays(X,N):
    dp=[0]*(X+1) 
    dp[0]=1
    powers=[]
    k=1
    while k**N<=X:
        powers.append(k**N)
        k+=1
    for power in powers:
        for x in range(X,power-1,-1):
            dp[x]+=dp[x-power]
    return dp[X]
X =int(input())
N =int(input())
print(countWays(X,N))
coins = [1, 2, 5]
amount = 11

print("Coins: ", coins)
print("Amount: ", amount)

def CoinChange(amount, coins):
    #in this variable the subanswer will be stored
    dp = [amount + 1] * (amount + 1)

    #debugging here 
    dp[0] = 0

        #looping through the amount 
    for i in range(1, amount + 1):
            #for each coin in the coins array
        for j in range(len(coins)):
            #if the coin is less than or equal to the amount
            if coins[j] <= i:
                #the subanswer is the minimum of the current subanswer or the current coin + the subanswer of the current amount - the current coin
                dp[i] = min(dp[i], 1 + dp[i - coins[j]])

#        dp[amount] has our answer. If we do not have an answer then dp[amount]
#        will be amount + 1 and hence dp[amount] > amount will be true. We then
#        return -1.
#  
#        Otherwise, dp[amount] holds the answer

        if dp[1] == amount + 1:
            return -1
        elif dp[amount] < amount:
            return dp[amount]

print(" ")
print("Answer: ", CoinChange(amount, coins))
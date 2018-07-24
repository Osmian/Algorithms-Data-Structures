# Problem: 121
def maxProfit(self, prices):
    #We just need to find the max difference between two numbers in the correct order
    minPrice = sys.maxsize
    maxProfit = 0
    for i in range(len(prices)):
        # If the current price is less than the previous minimum,
        # set the minimum to that price
        if(prices[i]<minPrice):
            minPrice = prices[i]
        # If the difference between the current price and the current min price
        # is greater than maxprofit it becomes the new               # maxprofit
        if ((prices[i]-minPrice)>maxProfit):
            maxProfit = prices[i]-minPrice
    return maxProfit

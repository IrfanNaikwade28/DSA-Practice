# def maxProfit(prices):
#         maxprofit = 0
#         maxprice = 0
#         tempprofit = 0

#         for i in range(0, len(prices)):
#             for j in range(i+1, len(prices)):
#                 if prices[i] < prices[j] and prices[j] > maxprice:
#                     maxprice = prices[j]
                
#             tempprofit = maxprice - prices[i]
#             maxprice = 0
#             if tempprofit > maxprofit:
#                 maxprofit = tempprofit
        
#         if maxprofit < 0:
#             return 0
#         return maxprofit


def maxProfit(prices):
        buyVal = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] < buyVal:
                buyVal = prices[i]
            else:
                 profit = prices[i] - buyVal
                 if profit > maxProfit:
                      maxProfit = profit
        return maxProfit
                        

print(maxProfit([2, 10, 1, 8]))
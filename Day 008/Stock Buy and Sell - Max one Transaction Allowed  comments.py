# Stock Buy and Sell - Max one Transaction Allowed

# Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell.

# Note: Stock must be bought before being sold.

# Examples:

"""
Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
Output: 8
Explanation: Buy for price 1 and sell for price 9. 

Input: prices[] = {7, 6, 4, 3, 1} 
Output: 0
Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

Input: prices[] = {1, 3, 6, 9, 11} 
Output: 10
Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]

"""

class Solution:
    def max_profit(self, prices):
        min_price = prices[0]  
        max_profit = 0        

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit

        return max_profit


if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    sol = Solution()
    print(sol.max_profit(prices))

# Approach:
# 1. Initialize min_price to the first price in the array and max_profit to 0.
# 2. Iterate through each price in the prices array.
# 3. For each price, check if it is less than min_price. If yes, update min_price.
# 4. Calculate the profit by subtracting min_price from the current price.
# 5. If the calculated profit is greater than max_profit, update max_profit.
# 6. Finally, return max_profit which contains the maximum profit possible with one transaction.
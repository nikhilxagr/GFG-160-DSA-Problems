# Stock Buy and Sell - Multiple Transaction Allowed.py

# Given an array prices[] representing stock prices, find the maximum total profit that can be earned by buying and selling the stock any number of times.

# Note: We can only sell a stock which we have bought earlier and we cannot hold multiple stocks on any day.

# Examples:
"""

Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
Output: 865
Explanation: Buy the stock on day 0 and sell it on day 3 = 310 - 100 = 210 and Buy the stock on day 4 and sell it on day 6 = 695 - 40 = 655 so the Maximum Profit  is = 210 + 655 = 865.

Input: prices[] = [4, 2, 2, 2, 4]
Output: 2
Explanation: Buy the stock on day 3 and sell it on day 4 => 4 – 2 = 2. Maximum Profit = 2.
"""

from typing import List

class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
    
# Approach:
# 1. Initialize a variable profit to 0.
# 2. Loop through the prices array starting from the second day.
# 3. If the price on the current day is greater than the previous day, add the difference to profit.
# 4. Finally, return the total profit.
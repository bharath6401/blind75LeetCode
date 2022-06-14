# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.


maxProfit=0
left=0
arr=[7,1,5,3,6,4]
right=1
while(right<len(arr)):
    currentProfit=arr[right]-arr[left]
    
    if(currentProfit>0):
        maxProfit=max(maxProfit,currentProfit)
    else:
        left=right
        
    right+=1
    
print(maxProfit)
    
#  method2

# This is a simple problem, if you just step backward in time:

# set the highest sale price to the last value in the array
# set the highest profit (sale price minus price of stock) to zero.
# now step backward through the array, and at each point:
# A. if the stock price is higher than the previously seen highest sale price, set the latter to the former;
# B. if the highest profit is less than the current highest sale price minus the current stock price, set the former to the latter.
# And when you've stepped back all the way to the beginning of the array, you'll have, as highest profit, the greatest difference between a stock price, and the highest price seen later than it in the array. So an O(n) solution.


        
    
        

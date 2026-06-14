# Day of the Week

# Given an array date[] = [d, m, y], where d denotes the day, m denotes the month, and y denotes the year, Write a program that calculates the day of the week for any particular date in the past or future.

# Examples:

# Input: date[] = [28, 12, 1995]
# Output: Thursday
# Explanation: 28 December 1995 was a Thursday.


# Input: date[] = [30, 8, 2010]
# Output: Monday
# Explanation: 30 August 2010 was a Monday.

# Your Task:
# Since this is a function problem, you don't need to worry about the testcases. Your task is to complete the function dayOfTheWeek() which takes an array date[] as input and returns the day of the week for the given date. The array date[] contains three integers where date[0] is the day, date[1] is the month and date[2] is the year.


from datetime import datetime

class Solution:
    def getDayOfWeek(self, date: list[int]) -> str:
        
        day, month, year = date
        
        date_obj = datetime(year, month, day)
        
        
        return date_obj.strftime("%A")
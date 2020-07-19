#Refer solution:no
#https://leetcode.com/problems/roman-to-integer/
#Arleigh Chang
'''
Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        answer = 0
        control=0
        for row in range(len(s)):
            if row != len(s)-1 and symbol[s[row]] < symbol[s[row+1]]:
                answer = answer + (symbol[s[row+1]]- symbol[s[row]])
                control+=1
            elif control!=0:
                control=0
                continue
            else:
                answer+=symbol[s[row]]
        return answer
'''
Runtime: 44 ms, faster than 86.69% of Python3 online submissions for Roman to Integer.
Memory Usage: 14 MB, less than 11.77% of Python3 online submissions for Roman to Integer.
'''
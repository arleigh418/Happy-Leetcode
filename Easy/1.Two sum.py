#Refer solution : yes
#https://leetcode.com/problems/two-sum/
#Arleigh Chang
'''
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
'''
class Solution(object):
    def twoSum(self,nums,target):
        for index,num in enumerate(nums):
            for x in range(index+1,len(nums)):
                if num + nums[x] == target:
                    return [index,x]
          
'''
Runtime: 3968 ms, faster than 26.57% of Python online submissions for Two Sum.
Memory Usage: 13.5 MB, less than 86.76% of Python online submissions for Two Sum.
'''        
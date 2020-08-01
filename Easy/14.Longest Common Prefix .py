#Refer solution:no
#https://leetcode.com/problems/longest-common-prefix/
#Arleigh Chang
'''
Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs:list) -> str:
        if len(strs) == 0 :return ""
        if len(strs) == 1 :return strs[0]
        compare_word = strs[0]
        strs = strs[1:]
        strs_lenght = len(strs)
        result = ""
        control = -1
        check_all_same = 0
        for main_word in compare_word:
            control+=1
            for each_word in strs:
                if control > len(each_word)-1: continue
                elif main_word == each_word[control]:
                    check_all_same+=1
            if check_all_same == strs_lenght:
                result+=main_word
                check_all_same=0
            else :return result
        return result



                    
            

x = Solution()
print(x.longestCommonPrefix(["c","c"]))
                

            
        
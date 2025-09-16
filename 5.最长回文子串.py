#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub_string = s[0]
        reverse_s = s[::-1]

        for i, subs in enumerate(reverse_s):
            start_index = 0
            
            while True:
                # 从左往右的第一个相同字母
                left = s.index(subs, start_index)
                start_index = left + 1
                # 右往左遍历时的当前index
                right = len(s) - 1 - i
                # 没有相同的字母
                if left >= right:
                    break
                else:
                    res = s[left: right+1:]
                    res_reverse = reverse_s[i:len(s)-left:]
    
                    if res == res_reverse and len(res) > len(sub_string):
                        print(res)
                        sub_string = res

        return sub_string
        
# @lc code=end

a = Solution()
# print(a.longestPalindrome('jcdcabacwicop'))
print(a.longestPalindrome('aa'))
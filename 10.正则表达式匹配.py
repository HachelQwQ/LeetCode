#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode.cn/problems/regular-expression-matching/description/
#
# algorithms
# Hard (30.97%)
# Likes:    4111
# Dislikes: 0
# Total Accepted:    475K
# Total Submissions: 1.5M
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# 
# 
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 
# 
# 所谓匹配，是要涵盖 整个 字符串 s 的，而不是部分字符串。
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s 只包含从 a-z 的小写字母。
# p 只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符
# 
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        left = 0
        right = len(p)
        
        for str in s:
            # pattern遍历完后，str还没遍历完
            if left >= right:
                return False
            
            print(left, str, p[left])

            # 如果pattern字符后接*并且，不匹配，则跳过当前字符和*
            while left < right -1 and p[left + 1] == '*':
                print('*')
                if not self.match(str, p[left]):
                    left += 2
                # 如果s字符和p的*后的字符匹配
                elif left < right - 2 and self.match(str, p[left + 2]):
                    left += 3
                    break
                # 如何和str匹配并且和pattern *后的字符不匹配
                else:
                    break
            # break则不执行
            else:
                if not self.match(str, p[left]):
                    return False
                left += 1

        while left < right - 1 and p[left + 1] == '*':
            left += 2

        # str遍历完后，pattern还没遍历完
        if not left >= right:
            return False

        return True
    
    def match(self, s: str, p: str) -> bool:
        if s == p or p == '.':
            return True
        else:
            return False

# @lc code=end

print(Solution().isMatch('mississippi', 'mis*is*ip*.'))
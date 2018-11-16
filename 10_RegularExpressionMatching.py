# coding=utf-8

# '.' 匹配单个的character
# '*' 可以匹配0个或者多个前面的元素， 例如'a*'代表着可以有0个a(没有a), 也可以有多个a
#
# The matching should cover the entire input string (not partial).

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true



class Solution(object):
    def isMatch(self, s, p):
        """
        Dynamic Programming
        dp[i][j] represents isMatch(p[0...i], s[0...j]), default is False;
            dp[i][-1] represents isMatch(p[0...i], "")
            dp[-1][j] represents isMatch("", s[0...j])
        """
        if not s:
            # .*.*.*.* Return True, others return False.
            if len(p) % 2 != 0:
                return False
            for k in range(1, len(p), 2):
                if p[k] != "*":
                    return False
            return True

        # dp = [[False] * (len(s)+1)] * (len(p)+1)
        dp = [[False for col in range(len(s) + 1)]
              for row in range(len(p) + 1)]
        dp[-1][-1] = True

        for i in range(len(p)):
            for j in range(len(s)):
                """
                p[i] is "*", so dp[i][j] =
                    1. dp[i-2][j]      # * matches 0 element in s;
                    2. dp[i-2][j-1]    # * matches 1 element in s;
                    3. dp[i][j-1]      # * matches more than one in s.
                """
                if p[i] == "*":
                    m_0 = dp[i - 2][j]
                    m_1 = (p[i - 1] == "." or p[i - 1] == s[j]) and dp[i - 2][j - 1]
                    m_more = (p[i - 1] == "." or p[i - 1] == s[j]) and dp[i][j - 1]
                    dp[i][j] = m_0 or m_1 or m_more

                    # p[i] matches "" is equal p[i-2] matches "".
                    dp[i][-1] = dp[i - 2][-1]

                else:
                    dp[i][j] = (dp[i - 1][j - 1] and
                                (p[i] == s[j] or p[i] == "."))
                    # p[i] doesn't match ""
                    dp[i][-1] = False
        print dp
        return dp[len(p) - 1][len(s) - 1]

sol = Solution()
print sol.isMatch("aab", "c*a*b")
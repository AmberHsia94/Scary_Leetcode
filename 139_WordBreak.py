# coding=utf-8
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

def word_break(arr, dict):
    if arr is None or dict is None:
        return

    dp = [False for i in range(len(arr)+1)]
    dp[0] = True    # 起始值初始化

    for i in range(1, len(arr)+1):     #split point
        for j in range(i):   #loop before the immediate point
            print i, j
            if arr[j:i] in dict and dp[j]:
                dp[i] = True
    print dp
    return dp[-1]

arr = "applepenapple"
dict = ["apple", "pen"]
print word_break(arr, dict)
print better(arr, dict)
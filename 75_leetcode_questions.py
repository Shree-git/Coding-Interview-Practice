# 3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(self, s: str) -> int:
        newStr = ''
        longLen = 0
        maxLen = 0
        for x in range(len(s)):
            for y in range(x, len(s)):
                if s[y] not in newStr:
                    newStr += s[y]
                    longLen += 1    
                else:
                    maxLen = max(maxLen, longLen)
                    newStr = ""
                    longLen = 0
                    break
        maxLen = max(maxLen, longLen)
        return maxLen 

# 5. Longest Palindromic Substring
def longestPalindrome(self, s: str) -> str:
        res = ''
        resSize = 0
        for x in range(len(s)):
            l = x
            r = x
            # Odd case
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l: r+1]) > resSize:
                    res = s[l:r+1]
                    resSize = len(s[l:r+1])
                l -= 1
                r += 1
    
            l = x
            r = x+1
            # Even case
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l: r+1]) > resSize:
                    res = s[l:r+1]
                    resSize = len(s[l:r+1])
                l -= 1
                r += 1
        return res

# 300. Longest Increasing Subsequence
def lengthOfLIS(self, nums: list) -> int:
    arr = [1] * len(nums)
    for x in range(len(arr)):
        subproblems = [arr[k] for k in range(x) if nums[k] < nums[x]]
        arr[x] = 1 + max(subproblems, default = 0)
    return max(arr)

# 62. Unique Paths
def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0]*(n+1)]*(m+1)
        arr[1][1] = 1
        for x in range(1,len(arr)):
            for y in range(1,len(arr[x])):
                arr[x][y] = arr[x-1][y] + arr[x][y-1]
        return arr[m][n]

# 125. Valid Palindrome
import re
def isPalindrome(self, s: str) -> bool:
    s= s.lower()
    s = re.findall('[0-9a-z]+', s)
    s = ''.join(s)

    if s == s[::-1]:
        return True
    else:
        return False

# 242. Valid Anagram
def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted (t):
            return True
        else:
            return False

# 128. Longest Consecutive Sequence
def longestConsecutive(self, nums: list) -> int:
    nums = list(set(nums))
    nums.sort()
    print(nums)
    arr = [1] * len(nums)
    for x in range(len(arr)):
        subproblems = [arr[k] for k in range(x) if (nums[k] == 1 + nums[x]) or (nums[k] == nums[x]-1)]
        arr[x] = 1 + sum(subproblems)
    print(arr)
    return max(arr) if len(arr) > 0 else 0

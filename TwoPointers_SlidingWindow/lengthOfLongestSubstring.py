s = "pwwkew"


def lengthOfLongestSubstring(s):
    left = 0
    right = 0
    seen = set()
    maxLen = 0
    while right < len(s):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1

        seen.add(s[right])
        maxLen = max(maxLen, right-left+1)

        right+=1
    return maxLen

# Brutforce soln with n^3 time complexity
# def lengthOfLongestSubstring(s):
#     maxLen = 0
#     for i in range(len(s)):
#         temp = ""
#         for j in range(i,len(s)):
#             if s[j] not in temp:
#                 temp+=s[j]
#                 maxLen = max(maxLen, len(temp))
#             else:
#                 break

#     return maxLen

print(lengthOfLongestSubstring(s))

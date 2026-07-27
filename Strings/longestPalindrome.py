s = 'babad'

# Brutforce Method
# def longestPalindrome(s):
#     lps = ''
#     n = len(s)
#     for i in range(0, n):
#         chars = ''
#         for j in range(i, n):
#             chars = chars + s[j]
#             left = 0
#             right = len(chars)-1
#             flag = True
#             while left <= right:
#                 if chars[left] != chars[right]:
#                     flag = False
#                     break
#                 left += 1
#                 right -= 1
#             if flag:
#                 if len(lps) < len(chars):
#                     lps = chars
#     return lps


# Optimal Solution
def checkPalindrome(s, left, right, temp, n):
    while left >= 0 and right < n:
        if s[left] == s[right]:
            temp = s[left]+temp+s[right]
            left -= 1
            right += 1
        else:
            break

    return temp

def longestPalindrome(s):
    lps = ''
    n = len(s)
    for i in range(n):
        even = checkPalindrome(s, i, i+1, '', n)
        odd = checkPalindrome(s, i-1, i+1, s[i], n)

        temp = even if len(even) > len(odd) else odd

        if len(temp) > len(lps):
            lps = temp
    return lps
print(longestPalindrome(s))

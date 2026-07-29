s = "aba"

#bruteforce with n^3
# def countSubstrings(s):
#     cnt = len(s)

#     for i in range(len(s) - 1):
#         for j in range(i + 1, len(s)):
#             left = i
#             right = j
#             flag = True
#             while left < right:
#                 if s[left] != s[right]:
#                     flag = False
#                     break

#                 left += 1
#                 right -= 1

#             if flag:
#                 cnt += 1
#     return cnt

# print(countSubstrings(s))




# optimal n^2

def checkPalindrome(s, left, right, n):
    cnt = 0
    while left >= 0 and right < n:
        if s[left] != s[right]:
            break
        cnt+=1
        left-=1
        right+=1
    return cnt

def countSubstrings(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        cnt += checkPalindrome(s, i, i,n)
        cnt += checkPalindrome(s, i, i+1,n)

    return cnt


print(countSubstrings(s))

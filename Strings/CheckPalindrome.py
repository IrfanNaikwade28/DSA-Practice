s = "0P"

def CheckPalindrome(s):
    s = "".join(i for i in s if i.isalnum())
    s = s.lower()
    rev = list(s)
    n = len(rev) - 1
    for i in range((n+1)//2):
        rev[i],rev[n-i] = rev[n-i], rev[i]

    rev = "".join(rev)
    return s==rev

print(CheckPalindrome(s))

# optimal Soln
# left = 0
# right = len(s) - 1

# while left < right:
#     if s[left] != s[right]:
#         return False
#     left += 1
#     right -= 1

# return True

s = ["h","e","l","l","o"]

# def ReverseString(s):
#     n = len(s)-1
#     for i in range(0, len(s)//2):
#         s[i], s[n-i] = s[n-i],s[i]

# ReverseString(s)
# print(s)


s = list(map(lambda i,: s[-i-1] ,range(len(s))))
print(s)

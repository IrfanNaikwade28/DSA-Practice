s = "anagram"
t = "nagaram"

s = list(s)
t = list(t)

def ValidAnagram(s, t):

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]

    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] > t[j]:
                t[i], t[j] = t[j], t[i]

    return s == t

print(ValidAnagram(s, t))



# Optimized Approach
# def ValidAnagram(s, t):

#     if len(s) != len(t):
#         return False

#     freq = {}

#     # Count letters in s
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1

#     # Remove letters using t
#     for ch in t:
#         if ch not in freq:
#             return False

#         freq[ch] -= 1

#         if freq[ch] < 0:
#             return False

#     return True

# print(ValidAnagram("anagram", "nagaram"))

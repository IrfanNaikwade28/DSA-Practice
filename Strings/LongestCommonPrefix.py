def LongestCommonPrefix(strs):
    lcp = strs[0]

    for i in range(1, len(strs)):
        temp = ""

        for j in range(min(len(lcp), len(strs[i]))):
            if lcp[j] == strs[i][j]:
                temp += lcp[j]
            else:
                break

        lcp = temp

    return lcp



#slicing soln:
# class Solution(object):
    # def longestCommonPrefix(self, strs):
    #     lcp = strs[0]

    #     for i in range(1, len(strs)):
    #         j = 0

    #         while j < len(lcp) and j < len(strs[i]) and lcp[j] == strs[i][j]:
    #             j += 1

    #         lcp = lcp[:j]

    #         if not lcp:
    #             return ""

    #     return lcp

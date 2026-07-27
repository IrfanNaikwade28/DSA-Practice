strs = ["eat","tea","tan","ate","nat","bat"]
def GroupAnagram(strs):
    groups = {}

    for s in strs:
        groupId = ''.join(sorted(s))
        if groupId not in groups:
            groups[groupId] = [s]
        else:
            groups[groupId].append(s)
    return list(groups.values())

print(GroupAnagram(strs))


# Optimal O(n*k)
def groupAnagrams(strs):
    groups = {}

    for s in strs:

        # Frequency array for 26 lowercase letha
        # ters
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Convert list to tuple (hashable)
        groupId = tuple(freq)

        if groupId not in groups:
            groups[groupId] = [s]
        else:
            groups[groupId].append(s)

    return list(groups.values())

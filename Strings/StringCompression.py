chars = ["a", "a", "b", "b", "c", "c", "c"]


def StringCompression(chars):
    n = len(chars)
    i = 0
    j = 0

    while i < n:
        currChar = chars[i]
        cnt = 0

        while i < n and chars[i] == currChar:
            # counting chars
            i += 1
            cnt += 1

        # assigning current character in j like [a,count]
        chars[j] = currChar
        j += 1

        if cnt > 1:
            # assigning count to char like [char,2]
            for s in str(cnt):
                chars[j] = s
                j += 1
    return j


print(StringCompression(chars))

piles = [3,6,7,11]
h = 8

# Brutforce method, get memory limit exceeded
# logic is right..!
# def KokoEatingBananas(piles, h):
#     n = len(piles)
#     low = 1
#     high = max(piles)

#     # used only when max function not allowed
#     # for i in range(n):
#     #     if piles[i] > high:
#     #         high = piles[i]

#     for k in range(low,high+1):
#         i = 0
#         hrCnt = 0
#         while i < n:
#             hours = piles[i] // k
#             if piles[i] % k != 0:
#                 hours += 1
#             hrCnt += hours
#             i+=1
#         if hrCnt <= h:
#             return k
#     return 1
#

def CalHour(piles, k):
    totalHour = 0
    for i in range(len(piles)):
        totalHour += piles[i] // k
        if piles[i] % k != 0:
            totalHour+=1
    return totalHour
def KokoEatingBananas(piles, h):
    low = 1
    high = max(piles)
    while low <= high:
        mid = (low+high)//2
        totalHour = CalHour(piles, mid)

        if totalHour <= h:
            high = mid-1
        else:
            low = mid+1
    return low

print(KokoEatingBananas(piles, h))

intervals = [[1,10],[2,3],[4,8]]
n = len(intervals)
i = 1

intervals.sort()


# By Modifying in place of arr
# while i < n:
#     if intervals[i][1] >= intervals[i+1][0]:
#         if intervals[i+1][1] >= intervals[i][1]:
#             intervals[i][1] = intervals[i+1][1]

#         intervals.remove(intervals[i+1])
#         i = 0
#         n-=1
#     else:
#         i+=1


# By keeping Extra Arr - Optimal soln
merged = [intervals[0]]
while i < n:
    if merged[-1][1] >= intervals[i][0]:
        if intervals[i][1] >= merged[-1][1]:
            merged[-1][1]= intervals[i][1]
    else:
        merged.append(intervals[i])   
    i+=1


print(merged)
# arr = [1,1,2,2,3,3,4]
# unique = []
# duplicate = []
# for i in range(0, len(arr)):
#     if arr[i] not in unique:
#         unique.append(arr[i])


# arr = unique

# print(arr)



arr = [1,2,3,4,2,1,3,5,4]

i = 0

while i < len(arr):
    j = i + 1

    while j < len(arr):
        if arr[i] == arr[j]:
            arr.pop(j)
        else:
            j += 1

    i += 1

print(arr)
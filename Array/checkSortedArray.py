arr = [1,3,4,7]
flag = True
for i in range(0,len(arr)-1):
    if arr[i] > arr[i+1]:
        print("Array is not sorted...!")
        flag = False
        break

if flag:
    print("Array is sorted...!")
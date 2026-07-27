arr = [1,2,3,4]
k = 2
def findKthPositive(arr, k):
        missingIntegers=[]
        n = len(arr)-1
        cnt = 1
        i = 0
        while i <= n:
            if arr[i] == cnt:
                i+=1
            else:
                missingIntegers.append(cnt)

            cnt+=1

        contiNum = arr[n] + 1
        j = 1
        while j <= k:
            missingIntegers.append(contiNum)
            j+=1
            contiNum+=1
        print(missingIntegers)
        return missingIntegers[k-1]

print(findKthPositive(arr,k))

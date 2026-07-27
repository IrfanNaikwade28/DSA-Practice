arr = [10, 20, 20, 5]
largest = float('-inf')
secLargest = float('-inf')

for i in arr:
    if i > largest:
        secLargest = largest
        largest = i
    
    elif i > secLargest and i!=largest:
        secLargest = i 

if secLargest == float('-inf'):
    print("No second largest element")
else:
    print(secLargest)
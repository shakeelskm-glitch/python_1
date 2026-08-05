'''# Step 1: Create an array (list) of integers
arr = [1, 2, 3, 2, 4, 5, 1]

# Step 2: Create an empty list to store duplicate elements
duplicates = []

# Step 3: Compare each element with others
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])
print(duplicates)'''

'''arr = [10, 25, 5, 40, 30]

# Step 2: Initialize largest and second largest
largest = arr[0]
second_largest = -1

# Step 3: Traverse the array
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(largest)
print(second_largest)''

arr=[10,40,30,50]
largest=arr[0]
smallest=arr[0]
for num in arr:
    if num < smallest:
        smallest=num
    if num>largest:
        largest=num
print(smallest)
print(largest)''

num=[1,2,3,4,5,6,7]
even_count=0
odd_count=0
for i in num:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count)
print(odd_count)

''

# Step 1: Create an array (list)
arr = [10, 20, 30, 40, 50]

# Step 2: Initialize start and end pointers
start = 0
end = len(arr) - 1

# Step 3: Reverse the array using swapping
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)'''


#binary search
arr=[20,30,40,50,60]
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1
data=[1,2,3,4,5]
search=binary_search_iterative(data,3)
print(search)
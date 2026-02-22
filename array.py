# 1- Reverse an array

arr = [2,6,3,9,12,1]

def reverse():
    n = len(arr)
    left = 0
    right = n-1
    while left <= right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr
print(reverse())

# 2. Find the Maximum & Minimum

arr = [2,6,3,9,12,1]

maxi = float("-inf")
mini = float("inf")

for i in arr:
    if i > maxi:
        maxi = i
for i in arr:
    if i < mini:
        mini = i
print(f"Maximum element of arr is : {maxi}")
print(f"Minimum element of arr is : {mini}")

# 3. Find the Sum of

arr = [2,6,3,9,6,12,1]

my_dict = {}
target_sum = 12

for i in range(len(arr)):
    my_dict[arr[i]] = i

for i in range(len(arr)):
    if target_sum-arr[i] in my_dict:
        print([i, my_dict[target_sum-arr[i]]])

# 4. Find the Second Largest Element

arr = [2,6,3,9,6,12,1]

largest_el = float("-inf")
slarge_el = float("-inf")

for i in arr:
    if i > largest_el:
        slarge_el = largest_el
        largest_el = i      
    if i > slarge_el and i < largest_el:
        slarge_el = i
print(f"second large element is : {slarge_el}")

# 5. Count Frequency of element

arr = [2,6,3,9,6,12,1]

my_dict = {}

for i in arr:
    my_dict[i] = my_dict.get(i, 0)+1

print(my_dict)

# 6. Check if Array is sorted

arr = [2,6,3,9,6,12,1]

def sorted():
    first = 0
    second = 1
    while second < len(arr):
        is_sorted = True
        if arr[first] > arr[second]:
            return False
        first += 1
        second +=1
    return is_sorted

print(sorted())  

# 7. Rotate Array by k Positions: Rotate the array to the right by k position
arr = [2,0,1,3,0,0,4,0,3,]
n = len(arr)
k = 2
k = k % n

def reverse(arr,left,right):

    while left <= right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1


reverse(arr,0,k-1)
reverse(arr,k,n-1)
reverse(arr,0,n-1)

print(arr)
 
# 8. Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.

arr = [2,6,3,9,6,12,1]

my_dict = {}
target_sum = 12

for i in range(len(arr)):
    my_dict[arr[i]] = i

for i in range(len(arr)):
    if target_sum-arr[i] in my_dict:
        print([i, my_dict[target_sum-arr[i]]])

# 9. Remove Duplicates from Array: Remove duplicates from the array while maintaining order.

arr = [2,6,3,9,6,12,1]
new_arr = []

my_dict = {}

for i in arr:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1
for key,val in my_dict.items():
    new_arr.append(key)

print(new_arr)

# 10. Merge Two Sorted Arrays

arr = [2,4,6,8,10]
arr2 = [1,3,5,7,9]

new_arr = arr+arr2
print(sorted(new_arr))

#11. Remove given Element from Array

arr = [2,4,6,8,10]

target = int(input("Enter the no. to delete :"))

for i in arr:
    if i == target:
        arr.remove(i)

print(arr)

# 12. Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.
# 13. Find Duplicates in an Array

arr = [2,6,4,4,6,8,6,10]

my_dict = {}

for i in arr:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for key,val in my_dict.items():
    if val > 1:
        print(key)

# 14. Find Intersection of Two Arrays: Find the common elements between two arrays.

arr = [2,6,4,4,6,8,6,10]
arr2 = [1,3,6,9]
common = []

for i in arr:
    if i in arr2:
        common.append(i)
print(set(common))

# 15. Find Union of Two Arrays

arr = [2,6,4,4,6,8,6,10]
arr2 = [1,3,6,9]

print(set(arr+arr2))

# 16. Check if Two Arrays Are Equal: if two arrays contain the same elements

arr = [2,6,4,4,6,8,6,10]
arr2 = [1,3,6,9]

if arr == arr2:
    print(True)
else:
    print(False)


#18. Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.

arr = [2,0,1,3,0,0,4,0,3,]

n = len(arr)
left = 0
right = n-1

while left < right:
    if arr[left] == 0:
        if arr[right] == 0:
            right -= 1
        else:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
    elif arr[left] != 0:
        if arr[right] == 0:
            right -= 1
        else:
            left += 1
print(arr)

# 20. Rotate Array to the Left by k

arr = [2,0,1,3,0,0,4,0,3,]
n = len(arr)
k = 2
k = k % n

def reverse(arr,left,right):

    while left <= right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1


reverse(arr,0,k-1)
reverse(arr,k,n-1)
reverse(arr,0,n-1)

print(arr)

# 21.Find the Kth Smallest element

arr = [2,0,1,3,0,0,4,0,3,]
n = len(arr)

kth_small = int(input("entet value of k"))

arr = sorted(set(arr))
kth_small = kth_small - 1

for i in range(len(arr)):
    if i == kth_small:
        print(arr[i])

# 24.Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.


arr = [2,0,1,3,6,0,4,5,3,]

arr = sorted(arr)
n = len(arr)

left = 0
right = n-1
result = []

while left <= right:
    if left != right:
        result.append(arr[right])
        result.append(arr[left])
    else:
        result.append(arr[left])
    left += 1
    right-= 1
print(result)

# 25.Find Majority Element: Find the element that appears more than n/2 times.

arr = [2,0,1,3,6,0,4,5,3,]

n = len(arr)

my_dict = {}

for i in arr:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for key,val in my_dict.items():
    if val > n//2:
        print(key)


"""array = [9,8,7,6,5,4,3,2,1] 
1. Split into groups of 3: [[9,8,7], [6,5,4], [3,2,1]] 
2. Reverse each sub-array: ? 
3. Find the maximum element in each sub-array: ? 
4. Calculate: sum_of_maximums - count_of_even_numbers_in_original_array"""

def splitArray(arr, n):
    
    new_arr = []
    for i in range(0, len(arr),n):
        new_arr.append(arr[i:i+n])
    return new_arr
    
def reverseSubArray(arr):
    rev = []
    val = []
    for i in range(0,len(arr)):
        for j in range(0, len(arr[i])):
            val = arr[i][::-1]
        rev.append(val)  
    return rev 

def findMaxinSubArray(arr):
    max_list = []
    for i in range(0, len(arr)):
        max_list.append(max(arr[i]))
    return max_list

def results(maxArry, originalArray):
    
    even_number_count = 0
    sum_max_arr = 0
    
    for i in range(0, len(originalArray)):
        if originalArray[i] % 2 == 0:
            even_number_count += 1
    
    for i in range(0,len(maxArry)):
        sum_max_arr = sum_max_arr + int(maxArry[i])
        
        
    return sum_max_arr - even_number_count
        
        
print(splitArray([9,8,7,6,5,4,3,2,1], 3))
print(reverseSubArray([[9,8,7], [6,5,4], [3,2,1]]))
print(findMaxinSubArray([[7, 8, 9], [4, 5, 6], [1, 2, 3]]))

print(results([9,6,3], [9,8,7,6,5,4,3,2,1]))
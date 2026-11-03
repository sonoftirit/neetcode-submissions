from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    list_sum = 0
    for n in nums:
        list_sum += n
    return list_sum

def get_min(nums: List[int]) -> int:
    min_val = nums[0]
    for n in nums:
        if n < min_val:
            min_val = n
    return min_val

def get_max(nums: List[int]) -> int:
    max_val = 0
    for n in nums:
        if n > max_val:
            max_val = n 
    return max_val

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))

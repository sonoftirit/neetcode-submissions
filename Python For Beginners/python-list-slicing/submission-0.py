from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    last_index = len(my_list) - 1
    rs_list = [my_list[last_index-2], my_list[last_index-1], my_list[last_index]]
    return rs_list
    
    


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))

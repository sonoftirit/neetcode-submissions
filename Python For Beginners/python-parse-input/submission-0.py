from typing import List

def read_integers() -> List[int]:
    line = input()
    strings = line.split(",") # list of strings 
    list_num = []

    for s in strings:
        list_num.append(int(s))
    return list_num


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

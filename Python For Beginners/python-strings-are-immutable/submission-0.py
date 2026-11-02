def remove_fourth_character(word: str) -> str:
    before_new = word[:3]
    after_new = word[4:]
    return before_new + after_new


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))

#22.	Write a function to find the second-largest number in a list.
def second_largest(lst):
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return None  # Not enough unique elements
    unique_lst.sort()
    return unique_lst[-2]
print(second_largest([29,45,6,787,34,233,34]))
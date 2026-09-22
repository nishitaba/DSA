#17.	Write a function to remove duplicate elements from a list.
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
print(remove_duplicates([57,67,87,45,67,34]))
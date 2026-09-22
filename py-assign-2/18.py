#18.	Write a function to count how many times an element appears in a list.
def count_occurrences(lst, element):
    return lst.count(element)
print(count_occurrences([45,56,45,45,79,97,34],45))
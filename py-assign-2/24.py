#24.	Write a function to merge two lists and remove duplicates.
def merge_and_remove_duplicates(lst1, lst2):
    return list(set(lst1 + lst2))
print(merge_and_remove_duplicates([10,20,30,40,50],[10,60,70,80,90,20]))
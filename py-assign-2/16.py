#16.	Write a function to find the largest element in a list.
def find_largest(lst):
    if not lst:
        return None
    return max(lst)
print(find_largest([20,56,34,768,67]))
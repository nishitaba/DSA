#23.	Write a function to sort a list without using sort().
def bubble_sort(lst):
    sorted_lst = lst.copy()
    n = len(sorted_lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_lst[j] > sorted_lst[j + 1]:
                # Swap the elements
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
    return sorted_lst
print(bubble_sort([34,567,87,54,345,65]))
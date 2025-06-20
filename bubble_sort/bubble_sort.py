def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                # Swap if the element found is greater
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list

pass
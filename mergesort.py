# Functions and variables should be snake_case: ASSIGNMENT -> assignment, mergeSort -> merge_sort

# The function name assignment not descriptive, assignment -> copy_element()
# The indices in the copy_element function can be renamed to i -> new_index and j -> old_index

# list_to_sort_by_merge is too long of a variable name (but list is a reserved keyword)
# We are supossed to indicate variable type by a suffix,thus: list_to_sort_by_merge -> input_list

# The if statements are redundant, we can just do len(list_to_..) > 1 (we are already covering all the cases)
# Instead of checking length > 1 and putting everything inside the if, we can check the inverse statement and return, if we do not want to continue

# We can set r, l, i to zero in one line
# The variables r, l, i correspond to right index, left index and merged index, so we rename them accordingly
# The variables left, right, and mid can be renamed to left_list, right_list, mid_index

# We dont have to explicitly set variables in function call of copy_element since they are not keywoard arguments: copy_element(input_list, merged_index, left, left_index)

# x = range(len(my_list)) is redundant, we only need it once

def copy_element(new_list, new_index, old_list, old_index):
    """
    This function assigns an element from a list at a specified index to another list at a specific position

    Parameters:
    - new_list (list): Destination list to assign the value to
    - new_index (int): Destination index in new_list where the value will be assigned
    - old_list (list): Source list to copy the value from
    - old_index (int): Source index in old_list to copy the value from

    Returns:
    - None: Since the assignment is in-place

    """
    # copy a single value from old_list[old_index] to new_list[new_index]
    new_list[new_index] = old_list[old_index]


def merge_sort(input_list):
    """
    This function sorts the input list in-place using a recursive merge sort

    Parameters:
    - input_list (list): list to be sorted

    Returns:
    - None: Since input list is sorted in place
    """
    # base case: perform empty return if a list of length 0 or 1 is already sorted
    if (len(input_list) <= 1):
        return

    # split the list into two halves
    mid_index = len(input_list) // 2
    left_list = input_list[:mid_index]
    right_list = input_list[mid_index:]

    # recursively sort both halves
    merge_sort(left_list)
    merge_sort(right_list)

    # initialize indices for left, right, and merged lists
    left_index = right_index = merged_index = 0

    # merge the sorted halves back into the original list
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            copy_element(input_list, merged_index, left_list, left_index)
            left_index += 1
        else:
            copy_element(input_list, merged_index, right_list, right_index)
            right_index += 1
        merged_index += 1

    # copy any remaining elements from the left half
    while left_index < len(left_list):
        input_list[merged_index] = left_list[left_index]
        left_index += 1
        merged_index += 1

    # copy any remaining elements from the right half
    while right_index < len(right_list):
        input_list[merged_index] = right_list[right_index]
        right_index += 1
        merged_index += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()

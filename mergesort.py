def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


# We can plot the sorted and unsorted in one bar plot with different colors:
# import maplotlib for visualization of the sorting
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
# create integer example data
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# create x-axis values for the data
x = range(len(my_list))

# plot the unsorted list, create a subplot for the first plot
plt.subplot(1, 2, 1)

# pot a bar chart with default color
plt.bar(x, my_list)

# add a title
plt.title("Before merge-sorting", fontsize = 20)

# add xlabel
plt.xlabel("Index", fontsize = 15)

# add ylabel
plt.ylabel("Value", fontsize = 15)

# sort the list by inplace, recursive mergesort
merge_sort(my_list)

# plot the unsorted list, create a subplot for the second one
plt.subplot(1, 2, 2)

# plot a bar chart with a different color
plt.bar(x, my_list, color="red")

# add a title
plt.title("After merge-sorting", fontsize = 20)

# add xlabel
plt.xlabel("Index", fontsize = 15)

# add ylabel
plt.ylabel("Value", fontsize = 15) # add ylabel
#Show the plot
plt.show()

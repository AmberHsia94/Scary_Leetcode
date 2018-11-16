# coding=utf-8
# Given a sorted array,
# such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 这题因为是排序好的，关键点是"删除多余元素"，这里其实不是真的删除，因为题目要求不能用额外的空间，所以最好的思路是替换。
# 题目也说了“It doesn't matter what you leave beyond the new length.”，所以我们只要把后面的元素放到前面来就行了。
def remove_for_sorted_arr(arr):
    # edge check
    if len(arr) < 2:
        return len(arr)

    new_length = 0  # pointer 1

    for length in range(1, len(arr)):  # pointer 2
        if arr[length] != arr[length - 1]:
            new_length = new_length + 1
            arr[new_length] = arr[length]

    return arr, new_length

# Given an array and a value, remove all instances of that value in place and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
def remove_a_value(arr,value):
    if value not in arr:
        return 0

    new_length = 0

    for length in range(len(arr)):
        if arr[length] != value:
            arr[new_length] = arr[length]
            new_length = new_length + 1
            print(arr, new_length)

    return arr, new_length


if __name__ == '__main__':
    arr = [1, 1, 2, 4, 5, 4]
    # print(remove_for_sorted_arr(arr))
    print(remove_a_value(arr, 4))


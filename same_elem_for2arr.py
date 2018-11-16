# find elements that is same for two arrays
def same_elements(arr1, arr2):
    # sorted O(nlogn)
    arr1_sorted = sorted(arr1)
    arr2_sorted = sorted(arr2)
    nums = []
    pointer1 = 0
    pointer2 = 0

    print(arr1_sorted, arr2_sorted)

    while pointer1 < len(arr1_sorted) and pointer2 < len(arr2_sorted):
        if arr1_sorted[pointer1] == arr2_sorted[pointer2]:
            nums.append(arr1_sorted[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif arr1_sorted[pointer1] < arr2_sorted[pointer2]:
            pointer1 += 1
        elif arr1_sorted[pointer1] > arr2_sorted[pointer2]:
            pointer2 += 1

    return nums



if __name__ == '__main__':
    arr1 = [1, 2, 5, 6, 4, 9]
    arr2 = [4, 7, 6, 9, 10, 2, 8]
    print(same_elements(arr1, arr2))

# coding=utf-8
# 给定有序数组，寻找目标值的起始位置
# Your algorithm's runtime complexity must be in the order of O(log n). If the target is not found, return [-1, -1]

def target_position(arr, target):
    if target not in arr:
        return [-1, -1]

    front = 0
    tail = len(arr) - 1
    result = []

    # Search for the left one
    while front < tail:
        print('f, e: ', front, tail)
        mid = front + (tail - front) / 2  # 防止溢出
        print('mid', mid)

        if arr[mid] < target:
            front = mid + 1
        else:
            tail = mid

    if arr[front] != target:
        return result
    else:
        result.append(front)

    # search for the right one
    tail = len(arr) - 1
    while front < tail:
        print('f, e: ', front, tail)
        mid = front + (tail - front) / 2 + 1 # make mid bias to the right
        print('mid', mid)

        if arr[mid] > target:
            tail = mid - 1
        else:
            front = mid

    result.append(tail)
    return result


if __name__ == '__main__':
    arr = [3, 4, 6, 7, 7, 7, 8, 8, 10]
    print(target_position(arr, 7))

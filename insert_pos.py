# coding=utf-8
# given a sorted and no duplicates array and a target value, return the index if the target is found
# if not, return the index where it should be inserted in order
# 二分查找
def insert_position(arr, target):
    if target in arr:
        return arr.index(target)
    else:
        front = 0
        tail = len(arr)-1

        while front < tail:
            mid = front + (tail - front)/2
            if arr[mid] < target:
                front = mid
            else:
                tail = mid

            if tail - front == 1:
                return [front, tail]

if __name__ == '__main__':
    arr = [1, 2, 5, 7, 9, 11, 12]
    print(insert_position(arr, target=10))
    print(insert_position(arr, target=4))
    print(insert_position(arr, target=8))
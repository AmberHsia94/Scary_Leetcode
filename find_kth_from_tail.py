# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# find the kth element in a linked list from tail.
# use two pointer with distance of k
# then slides these two pointers to the end,
class Solution:
    def FindKthToTail(self, head, k):
        # edge check
        if not head:  # linked-list is empty
            return head
        if k <= 0:
            return ListNode(0).next

        pointer_1 = head
        pointer_2 = head

        for i in range(k-1):
            # edge check, if k > length
            if pointer_2.next:
                pointer_2 = pointer_2.next
            else:
                return pointer_2.next

        while pointer_2.next:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
        return pointer_1

sol = Solution
print(sol.FindKthToTail())




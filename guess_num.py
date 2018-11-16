import random
# We are playing the Guess Game.
# I pick a number from 1 to n. You have to guess which number I picked.
#  Every time you guess wrong, I'll tell you whether the number is higher or lower.
#  -1 : My number is lower 1 : My number is higher 0 : Congrats! You got it!
def guess_num(n):
    front = 1
    tail = n

    while front < tail:
        mid = front - (front + tail) / 2
        if guess(mid, n) == 0:
            return mid
        elif guess(mid, n) < 0: #the number is too large
            tail = mid - 1
        else:
            front = mid + 1


def guess(mid, n):
    N = random(1, n)
    if mid == N:
        print('0: Congrats! You got it!')
    elif mid < N:
        print('1 : My number is higher')
    else:
        print('-1 : My number is lower')






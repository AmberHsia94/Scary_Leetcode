from pythonds.basic.stack import Stack

#  calculate the sum of a list of numbers such as: [1,3,5,7,9]
def sum_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + sum_list(l[1:])


# covert an integer to a string in any bases
# eg: convert the integer 10 to its string representation in decimal as "10", or to string in binary as "1010".
def int_to_str(n, base):
    lookup = '0123456789ABCDEF'
    if n < base:
        return lookup[n]
    else:
        return int_to_str(n / base, base) + lookup[n % base]


def stack_frame(n, base):
    lookup = '0123456789ABCDEF'
    s = Stack()
    while n:
        if n < base:
            s.push(lookup[n])
        else:
            s.push(lookup[n % base])
        n = n / base
    # print(s.items)

    str = ''
    while not s.isEmpty():
        str = str + s.pop()
    return str

if __name__ == '__main__':
    testList = [1, 3, 5, 7, 9]
    # print(sum_list(testList))

    print(int_to_str(1453, 16))
    print(stack_frame(1453, 16))
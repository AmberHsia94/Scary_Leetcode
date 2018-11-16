# the classic anagram detection problem for strings.
# strings with same length and characters, but different orders.
# like 'heart' and 'earth', 'python' and 'typhon'.

def count_compare(s1, s2):
    d1 = {}

    for c in s1:
        if c not in d1:
            d1[c] = 1
        else:
            d1[c] += 1
    print(d1)

    for s in s2:
        if s in d1:
            d1[s] -= 1
        else:
            print('%s and %s are not anagram. ' % (string1, string2))
    print(d1.values())

    if d1.values().count(0) == len(d1.values()):  # check if a list only contains 0
        print('%s and %s are anagram. ' % (string1, string2))
    else:
        print('%s and %s are not anagram. ' % (string1, string2))


def sort_compare(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    match = 0
    for pos in range(len(alist1)):  # same length
        if alist1[pos] == alist2[pos]:
            match += 1
        else:
            print('%s and %s are not anagram. ' % (string1, string2))
            break
    if match == len(alist1):
        print('%s and %s are anagram. ' % (string1, string2))


if __name__ == '__main__':
    string1 = 'python'
    string2 = 'typhon'
    count_compare(string1, string2)
    sort_compare(string1, string2)

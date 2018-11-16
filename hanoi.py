from pythonds.basic.stack import Stack


# move the n-1 disks to an intermediate pole,
# move the last disks in n to the final pole,
# move the n-1 disks to the final pole
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)


moveTower(3, "A", "B", "C")

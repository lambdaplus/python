# coding=utf-8


def merge_loop(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if len(l1) < len(l2):
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]

    tmp.extend(l1)
    tmp.extend(l2)
    return tmp

l1 = [1, 2, 3]
l2 = [4, 5, 6, 7, 8]
print(merge_loop(l1, l2))

# [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]


def combinator(list1, list2):
    combine = []
    for i in range(len(list1)):
        combine.append(list1[i])
        combine.append(list2[i])
    return combine


print(combinator([1, 2, 3], [11, 22, 33]))

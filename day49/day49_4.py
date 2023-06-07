def mountain_scape(tops):

    total_area = 0
    covered = set()

    for x, y in tops:
        height = y
        for i in range(x - height+1, x + height ):
            for j in range(1,  height - abs(i-x)+1):
                if (i, j) in covered:
                    continue
                else:
                    covered.add((i, j))
                    total_area += 1
    return total_area

# test the function with some examples
print(mountain_scape([(1, 1), (4, 2), (7, 3)]))  # should print 13
print(mountain_scape([(0, 2), (5, 3), (7, 5)]))  # should print 29
print(mountain_scape([(1, 3), (5, 3), (5, 5), (8, 4)]))  # should print 37

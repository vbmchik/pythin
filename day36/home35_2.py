def coloda(n):
    nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Валет", "Дама", "Король", "Туз"]
    kinds = ["Пики", "Буби", "Крести", "Череви"]
    col = []
    for _ in range(n):
        for x in kinds:
            for y in nums:
                col.append((x, y))
        yield (col)


c = coloda(4)
print(next(c))

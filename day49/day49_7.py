def mountain_scape(triangles):
    # Sort triangles by their x-coordinate
    triangles = sorted(triangles, key=lambda t: t[0])

    # Calculate the area of each triangle
    areas = []
    for i in range(len(triangles)):
        if i == 0:
            # First triangle
            base = triangles[i+1][0] - triangles[i][0]
            height = triangles[i][1]
        elif i == len(triangles) - 1:
            # Last triangle
            base = triangles[i][0] - triangles[i-1][0]
            height = triangles[i][1]
        else:
            # Middle triangle
            left_base = triangles[i][0] - triangles[i-1][0]
            right_base = triangles[i+1][0] - triangles[i][0]
            base = min(left_base, right_base)
            height = triangles[i][1]

        area = 0.5 * base * height
        areas.append(area)

    # Calculate the total area
    total_area = sum(areas)

    # Calculate the overlapping area
    overlapping_area = 0
    for i in range(len(triangles) - 1):
        left_triangle = triangles[i]
        right_triangle = triangles[i+1]

        if left_triangle[1] > right_triangle[1]:
            # Left triangle is higher than right triangle
            left_height = left_triangle[1] - right_triangle[1]
            right_height = right_triangle[1]
        else:
            # Right triangle is higher than left triangle
            left_height = left_triangle[1]
            right_height = right_triangle[1] - left_triangle[1]

        base = right_triangle[0] - left_triangle[0]
        overlapping_area += 0.5 * base * min(left_height, right_height)

    # Subtract the overlapping area from the total area
    total_area -= overlapping_area

    return int(total_area)


print(mountain_scape([(1, 1), (4, 2), (7, 3)]))  # should print 13
print(mountain_scape([(0, 2), (5, 3), (7, 5)]))  # should print 29
print(mountain_scape([(1, 3), (5, 3), (5, 5), (8, 4)]))  # should print 37

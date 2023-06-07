

  # Define a function to calculate the area of a triangle given its top coordinates


def triangle_area(x, y):
  # The base is always on the x-axis, so the height is equal to the y coordinate
  # The slope angle is 45 degrees, so the base is equal to the height
  # The area is half of the base times the height
  return 0.5 * y * y

# Define a function to calculate the total area of a mountain scape given a list of top coordinates


def mountain_scape(coords):
  # Initialize the total area to zero
  total_area = 0
  # Initialize a set to store the x coordinates that have been visited
  visited = set()
  # Loop through the list of coordinates
  for x, y in coords:
    # If the x coordinate has not been visited before
    if x not in visited:
      # Add the area of the triangle to the total area
      total_area += triangle_area(x, y)
      # Add the x coordinate to the visited set
      visited.add(x)
  # Return the total area
  return total_area


# Test the function with some examples
print(mountain_scape([(1, 1), (4, 2), (7, 3)]))  # Should print 13
print(mountain_scape([(0, 2), (5, 3), (7, 5)]))  # Should print 29
print(mountain_scape([(1, 3), (5, 3), (5, 5), (8, 4)]))  # Should print 37

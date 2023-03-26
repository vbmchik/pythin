numbers = [1, 2, 3, 4, 5]
letters = ('a', 'b', 'c')
characters = 'abnskdfjskdf'
print(iter(numbers))
print(numbers[2], letters[1], characters[6])

unorders = {1, 2, 3}
for n in unorders:
    print(n)

p = enumerate(unorders)
for index, element in p:
    print(index, element)

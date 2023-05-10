str = "My mind is clear"

res = ' '.join([x[::-1] for x in str.split()])

print(res)

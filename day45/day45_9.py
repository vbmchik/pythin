import collections


with open('advs.txt', 'r') as f:
    t = f.read()
t = ''.join(filter(lambda x: x.isalpha() or x == ' ', t))
words = t.lower().split()

counter = collections.Counter(words)
most_common, occ = counter.most_common()[0]
longest = max(words, key=len)

print(most_common, longest, occ)


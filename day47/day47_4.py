from typing import Iterable


def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    # your code here
    
    d = [ (x, items.count(x)) for x in items ]
    d.sort( key = lambda x: x[1], reverse=True)
    l = []
    for x in d:
        if x[0] not in l:
            l.extend([x[0]]*x[1])
    return l


print("Example:")
print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))


from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    text += '_' if len(text) % 2 != 0 else ''
    return [ text[i:i+2] for i in range(0, len(text), 2)]


print("Example:")
print(list(split_pairs("abcd")))

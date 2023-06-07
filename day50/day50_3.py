def cut_sentence(line: str, length: int) -> str:
    result = ""
    for word in line.split(" "):
        if len(word.replace("...","")) + len(result) < length:
            if result != "":
                result += " "
            result += word 
        else:
            break
    if result[-3:] != "..." and result != line:
        result += "..."
    return result


print("Example:")
print(cut_sentence("Hi my name is Alex", 20))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")

def is_family(tree: list[list[str]]) -> bool:
    fathers = [ x[0] for x in tree]
    sons = [x[1] for x in tree]
    tops = set()
    for father in fathers:
        if father not in sons:
            tops.add(father)
    if len(tops)!=1:
        return False
    ideal_family = []
    while(len(tops)>0):
        t = []
        for x in filter(lambda x: x[0] in tops, tree):
            t.append(x[1])
            ideal_family.append(x)
        tr = list(filter(lambda x: x[0] in tops and x[1] in tops,tree))
        if len(tr) > 0:
            return False   
        tops = t
    
    return len(tree) == len(ideal_family)


print("Example:")
print(
    is_family( 
        [
            ['Logan', 'Mike'], ['Alexander', 'Jack'], ['Jack', 'Logan']
         ]
    )
)

assert is_family([["Logan", "Mike"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"],
                 ["Mike", "Alexander"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"],
                 ["Mike", "Logan"]]) == False
assert is_family([["Logan", "Mike"], ["Logan", "Jack"],
                 ["Mike", "Jack"]]) == False
assert (
    is_family([["Logan", "William"], ["Logan", "Jack"],
              ["Mike", "Alexander"]]) == False
)
assert is_family([["Jack", "Mike"], ["Logan", "Mike"],
                 ["Logan", "Jack"]]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

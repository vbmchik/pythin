from functools import reduce


def boolean_and(my_list):
    if len(my_list) > 1:
        return my_list.pop(0) and boolean_and(my_list)
    else:
        return my_list.pop()


def boolean_or(my_list):
    if len(my_list) > 1:
        return my_list.pop() or boolean_or(my_list)
    else:
        return my_list.pop()


def boolean_xor(my_list):
    if len(my_list) > 1:
        return my_list.pop(0) ^ boolean_xor(my_list)
    else:
        return my_list.pop()


print(boolean_or([True, True, False, False]))

def add_two_numbers(l1, l2):
    # l1 and l2 are lists of digits in reverse order
    l1.reverse()
    l2.reverse()

    l1 = "".join(map(str, l1))
    l2 = "".join(map(str, l2))

    l1 = int(l1)
    l2 = int(l2)
    add = list(str(l1+l2))
    add.reverse()

    response = map(int, add)

    return list(response)
    
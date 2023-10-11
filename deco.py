def fact(a: int):
    """
    # 4! = 4 * 3 * 2 * 1
    """
    # fact = 1
    # for i in range(a,1,-1):
    #     fact = fact * i

    a = 10_000
    if a == 1:
        return a

    return a * fact(a - 1)

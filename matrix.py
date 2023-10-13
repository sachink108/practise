def transpose():
    a = [[1, 2, 3, 4], [4, 5, 9, 9], [7, 8, 1, 1]]  # 3x2
    # ta = [[1, 4, 7], [2, 5, 8]] # 2x3

    rows = len(a)
    cols = len(a[0])
    ta = [[0 for i in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            ta[j][i] = a[i][j]

    print(ta)


transpose()

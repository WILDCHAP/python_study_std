for i in range(1, 10):  # i: 1-9
    for j in range(1, i + 1):  # j: 1-i+1
        print("%d * %d = %d " % (j, i, i * j), end = '\t')
    print("\n")
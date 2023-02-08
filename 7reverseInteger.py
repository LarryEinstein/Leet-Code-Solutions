def reverser(x):
    mylist = x
    y = str(abs(x))
    print(y)
    y = y.strip()
    print(y)
    y = y[::-1]

    output = int(y)

    if output >= 2** 31 -1 or output <=-2**31:
        return 0
    elif x < 0 :
        return -1 * output
    else:
        print(output)
reverser(3238746)
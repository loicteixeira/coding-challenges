def seven(m, times=0):
    if m < 100:
        return m, times
    else:
        x, y = divmod(m, 10)
        m = x - 2 * y
        return seven(m, times + 1)

def l2d(filename):
    d = {}
    key = filename.readline().strip().split()
    val = filename.readline().strip().split()
    for k, v in zip(key, val):
        d[k] = int(v)
    return d
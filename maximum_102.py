def maximum(l):
    if len(l) == 1:
        return l[0]

    if l[0] >= maximum(l[1:]):
        return l[0]
    else:
        return maximum(l[1:])
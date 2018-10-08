def reverse_list(l):
    if len(l) == 0:
        return []

    return l[-1:] + reverse_list(l[:-1])
from stack_092 import Stack

lefties = '({['
righties = ')}]'
mapping = {v: k for k, v in zip(lefties, righties)}


def matcher(s):
    stack = Stack()
    for e in s:
        if e in lefties:
            stack.push(e)
        try:
            if e in righties and stack.top() == mapping[e]:
                stack.pop()
        except IndexError:
            return False
    if stack.is_empty():
        return True
    return False
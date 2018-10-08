def callme03(x):
    try:
        y = 1/x
        return y
    except ZeroDivisionError:
        print('In exception handler')
    else:
        print('Reached end of try')
    finally:
        print('Exiting the function')

print(callme03(1))
print(callme03(0))

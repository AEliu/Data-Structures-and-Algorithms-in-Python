##def is_even(k):
##    i = 0
##    pk = k if k > 0 else -k
##    while i < pk:
##        i += 2
##    if i == pk:
##        return True
##    else:
##        return False

def is_even(k):
##    if not isinstance(k, int):
##        return False
##    else:
        return str(k).endswith(('0', '2', '4', '6', '8'))
        

if __name__ == '__main__':
    print(is_even(3))
    print(is_even(0))
    print(is_even(-54))
##    print(is_even(-54.2))

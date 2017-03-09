def is_multiple(n ,m):
##    if n % m == 0:
##        return True
##    else:
##        return False
    result = True if n % m == 0 else False
    return result

if __name__ == '__main__':
    print(is_multiple(4, 2))
    print(is_multiple(11, 2))
    

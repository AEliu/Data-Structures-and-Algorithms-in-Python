def is_product_odd(data):
    data = list(set(data))
    data = [ i for i in data if i % 2 != 0]
    return False if len(data) < 2 else True
if __name__ == '__main__':
    print(is_product_odd([1, 3, 4, 5, 3]))
    print(is_product_odd([3, 3, 4, 2]))
    print(is_product_odd([3, 3, 4, 2, 5]))
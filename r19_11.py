def  range_test():
    print(list(range(50, 81, 10)))
    print(list(range(8, -9, -2)))
    print([2**i for i in range(9)])

if __name__ == "__main__":
    range_test()
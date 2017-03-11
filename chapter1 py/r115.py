def is_all_diff(data):
    for outdata in range(len(data) - 1):
        for indata in range(outdata + 1, len(data)):
            if data[outdata] == data[indata]:
                return False
    return True

if __name__ == '__main__':
    print(is_all_diff([1, 3, 4, 5]))
    print(is_all_diff([3, 3, 4, 2]))
    print(is_all_diff([9, 3, 4, 2, 5]))
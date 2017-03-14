def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

if __name__ == '__main__':
    a = [1, 1, 1, 3, 5, 7, 7, 10, 10, 11, 13, 13, 14, 16, 16, 18, 18, 20, 20, 23, 23, 23, 25, 26, 30, 32, 33, 34, 35, 35, 36, 41, 42, 45, 46, 47, 47, 47, 50, 50, 52, 52, 56, 56, 59, 60, 60, 61, 62, 66, 66, 69, 76, 79, 79, 81, 83, 83, 84, 84, 85, 87, 88, 89, 89, 89, 90, 90, 94, 94, 94, 94, 95, 96, 96, 97, 99, 99, 99, 102, 105, 106, 106, 109, 110, 111, 114, 117, 117, 118, 119, 119, 120, 123, 123, 124, 125, 125, 125, 126, 127, 129, 130, 131, 131, 132, 132, 133, 137, 138, 138, 138, 138, 138, 138, 139, 140, 141, 141, 142, 142, 144, 144, 145, 145, 146, 146, 146, 148, 148, 149, 153, 158, 161, 161, 161, 161, 162, 164, 165, 166, 167, 168, 171, 171, 172, 173, 176, 177, 179, 180, 182, 188, 188, 189, 197, 198, 199, 200, 200, 201, 203, 206, 206, 206, 207, 207, 208, 209, 209, 210, 210, 213, 214, 214, 217, 218, 218, 218, 220, 225, 225, 228, 230, 232, 232, 233, 240, 241, 242, 244, 244, 248, 248, 248, 249, 249, 249, 251, 251, 252, 252, 253, 254, 255, 255, 256, 257, 258, 258, 260, 263, 263, 264, 265, 266, 268, 269, 274, 275, 276, 276, 277, 277, 279, 280, 284, 285, 285, 286, 286, 287, 289, 290, 290, 297, 297, 299, 300, 300]
    high = len(a) - 1
    print(binary_search(a, 45, 0, high))
    print(binary_search(a, 99, 0, high))
    print(binary_search(a, 6, 0, high))

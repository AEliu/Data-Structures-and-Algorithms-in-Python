def reverse_s(s, low, high):
    mid = (high - low) // 2
    if high == low:
        return s
    elif high - low == 1:
        return s[high] + s[low]
    # elif (high - low) % 2:
    #     return reverse_s(s, mid+1, high) + reverse_s(s, low, mid)
    else:
        return s[high] + reverse_s(s, low + 1, high -1) + s[low]

if __name__ == '__main__':
    s = 'abcdefsdagagagdsag'
    print(reverse_s(s, 0, len(s) - 1))
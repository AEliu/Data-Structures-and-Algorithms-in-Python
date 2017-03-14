def is_palindrome(s, low, high):
    if high - low < 1:
        return True
    else:
        return s[low] == s[high] and is_palindrome(s, low + 1, high - 1)

if __name__ == '__main__':
    print(is_palindrome('abc', 0, 2))
    print(is_palindrome('aba', 0, 2))
    print(is_palindrome('acbca', 0, 4))
    print(is_palindrome('acbda', 0, 4))
    print(is_palindrome('acca', 0, 3))


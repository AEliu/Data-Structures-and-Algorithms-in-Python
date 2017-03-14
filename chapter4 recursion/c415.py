def subset(s):
    if len(s) == 1:
        return s
    else:
        a = [s[0]]
        for i in subset(s[1:]):
            a.append(i + s[0])
            a.append(i)
        return a

if __name__ == '__main__':
    s = 'abcdefghijklmn'
    subset_num = subset(s)
    print(subset_num)
    print(len(subset_num))
    print()
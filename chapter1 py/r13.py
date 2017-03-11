def minmax(*data):
    max = min = data[0]
    for i in data:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)

if __name__ == '__main__':
    print(minmax(2, 10, 13, 15, 4, 8, 1))
        

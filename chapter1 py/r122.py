def dotmul(a, b):
    return [a[i]*b[i] for i in range(len(a))]

if __name__ == '__main__':
    print(dotmul([1,4],[2,4]))
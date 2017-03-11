def foo(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

if __name__ == '__main__':
    print(foo(4)) #<generator object foo at ......>
    for i in foo(4): #1	4	2
        print(i, end = '\t')

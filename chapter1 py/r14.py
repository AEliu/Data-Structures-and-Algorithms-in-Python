def  sum_sqr(n):
    return int(n * (n - 1) * (2 * n - 1) / 6)

if __name__ == "__main__":
    print(sum_sqr(6))
    print(sum_sqr(3))
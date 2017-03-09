def  sum_odd_sqr(n):
    n = n -2 if n % 2 == 1 else n-1
    if n > 0:
        return int((n + 1)/2 * ((n + 1)**2 - 1)/3)
    else:
        raise ValueError('opp! Below zero!')

if __name__ == "__main__":
    print(sum_odd_sqr(6))
    print(sum_odd_sqr(3))
    print(sum_odd_sqr(1))
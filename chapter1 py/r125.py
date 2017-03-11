def punremove(s):
    slist = list(s)
    reslist = [letter for letter in slist if letter.isalpha() or letter.isspace()]
    return ''.join(reslist)

if __name__ == '__main__':
    print(punremove("Let's go, Mike!"))
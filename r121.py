def input_line():
    line = []
    while (True):
        try:
            i = input()
            line.append(i)
        except EOFError:
            line.reverse()
            print(line)
            raise

if __name__ == '__main__':
    input_line()
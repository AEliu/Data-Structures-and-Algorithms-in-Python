import random
import datetime

def birthday_generate(n):
    assert n > 0
    for i in range(n):
        date = datetime.date(1985, 1, 1)+datetime.timedelta(days=random.randrange(0, 365))
        yield (date.month, date.day)

if __name__ == '__main__':
    for i in birthday_generate(30):
        print(i)
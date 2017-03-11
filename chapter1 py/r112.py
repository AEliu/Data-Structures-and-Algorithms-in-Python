import random

def rand_choice(data):
    return data[random.randrange(len(data))]

if __name__ == '__main__':
    print(rand_choice([1, 3, 5, 'hi', True]))

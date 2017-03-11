def word_freq(words):
    wordli = words.split(' ')
    wordset = list(set(wordli))
    wordfreq = []
    index = 0
    for word in wordset:
        print("{0:12} frequncy is {1}".format(word, wordli.count(word)))
    return

if __name__ == '__main__':
    word_freq(r'this is a puppy , John love her very much ! When he was a boy , the puppy ran with him every evening !')

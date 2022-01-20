from random import sample
from wordlist import WORDS


class Wordle():

    def __init__(self):

        self.word_list = WORDS
        self.corpus = [word for word in self.word_list]
        self.letFreq = {chr(i): 0 for i in range(97, 97+26)}
        self.targetWord = sample(self.corpus, 1)[0]
        for word in self.corpus:
            for let in word.lower():
                self.letFreq[let] += 1

    # Define what you think is the best word to guess
    # I provided self.letFreq which is a dictionary of frequency of letters
    # But you might want to use other options, this wordscore is based only on letterfrequency * not having repeated letters
    # this works okay but you make improvements
    def wordscore(self, word):
        total = 0
        for l in word:
            total += self.letFreq[l]
        return total * len(set(word))

    def findBestGuess(self):
        max = 0
        bestword = ''
        for word in self.corpus:
            score = self.wordscore(word)
            if score > max:
                bestword = word
                max = score

        return bestword

    def filter(self, word):
        for i, letter in enumerate(word):
            if self.targetWord[i] == letter:
                self.corpus = [w for w in self.corpus if w[i] == letter]
            elif letter not in self.targetWord:
                self.corpus = [w for w in self.corpus if letter not in w]
            else:
                self.corpus = [w for w in self.corpus if letter in w]

    def enterFilter(self, guess, map):
        for i, r in enumerate(map):
            if r == 'g':
                self.corpus = [w for w in self.corpus if w[i] == guess[i]]
            elif r == 'b':
                self.corpus = [w for w in self.corpus if guess[i] not in w]
            else:
                self.corpus = [w for w in self.corpus if guess[i] in w]

    def returnFilter(self, guess):
        res = []
        for i, letter in enumerate(guess):
            if letter == self.targetWord[i]:
                res.append('g')
            elif letter not in self.targetWord:
                res.append('b')
            else:
                res.append('y')
        return ''.join(res)

    def guess(self, word):
        if word == self.targetWord:
            return True
        else:
            filter(word, self.targetWord)
            return False

    def getWord(self):
        for word in self.corpus:
            yield word

    def game(self):
        guesses = 0
        word = self.findbestGuess()
        while not self.guess(word, self.targetWord) and guesses < 7:
            guesses += 1
            word = self.findbestGuess()

        return guesses

    def newGame(self):
        self.corpus = [word[:-1] for word in self.word_list]
        self.targetWord = sample(self.corpus, 1)[0]

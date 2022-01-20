from wordleSolver import Wordle
import random


class CustomSolver(Wordle):
    def __init__(self):
        Wordle.__init__(self)

    # custom wordscore method
    # You can look in wordleSolver to see an example, where it is based on most frequently occouring letters.
    # and limiting repeated letters.
    # params:
    #   String: word, the word you want to evaluate
    # returns
    #   Int: The score for the word you evaluate based on your metrics
    def wordscore(self, word):
        return random.randint(0, 100)


wins = 0
w = Wordle()
#w = CustomSolver()
l = []
for word in w.getWord():
    w.newGame(word)
    guesses = w.game()
    wins += int(guesses < 7)
    if guesses < 7:
        l.append(guesses)

print("{0} Wins out of {1}".format(wins, len(w.word_list)))
print()
print("Average: {}".format(sum(l)/len(l)))

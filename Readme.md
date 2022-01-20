usage:

Python -i wordleSolver.py

w = Wordle()

w.findBestGuess()

w.enterFilter(<word you guessed>, <encoded response>)

filter encoding:
 'g' correct letter correct spot
 'b' incorrect letter
 'y' correct letter wrong spot


To improve this it is best if you change the 'wordScore' method to be more intelligent.

The only metric I provided was letter frequency which can be found with letFreq member variable
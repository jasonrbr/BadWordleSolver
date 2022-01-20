### Usage:
    >Python -i wordleSolver.py

    w = Wordle()

    #repeat until you get the correct answer
    w.findBestGuess()

    w.enterFilter('word you guessed', 'encoded response')


### Filter encoding:
 >'g' correct letter correct spot
 >'b' incorrect letter
 >'y' correct letter wrong spot


To improve this it is best if you change the 'wordScore' method to be more intelligent.

The only metric I provided was letter frequency which can be found with letFreq member variable, but you 
could make different ones if you add them to the __init__ in CustomSolver on WordleTester.py



To test out your wordscore run python WordleTest.py. It will let you know how many words your strategy worked on and how 
many guesses on average it took.

It implements a custom Wordle game wher you can change the wordscore method and test it out by commenting the and uncommenting lines 21 /22

You can also uncomment the last line to see what words it couldn't solve in 6 tries.
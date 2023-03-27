# Hangman game
import random
import string

class Hangman:

    def __init__(self, wordlist_file):
        with open(wordlist_file, 'r') as f:
            self.wordlist = [w.lower() for w in f.read().split()]
        
        self.secretWord = ''
        self.resetStats()
        self.resetGame()

    def chooseWord(self):
        """
        wordlist (list): list of words (strings)

        Returns a word from wordlist at random
        """
        return random.choice(self.wordlist)


    def isWordGuessed(self):
        '''
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far
        returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
        '''
        secretWordSet = set(self.secretWord)

        for c in secretWordSet:
            if c not in self.lettersGuessed:
                return False

        return True



    def getGuessedWord(self):
        '''
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far
        returns: string, comprised of letters and underscores that represents
        what letters in secretWord have been guessed so far.
        '''
        result = []
        print(self.secretWord)
        for c in self.secretWord:
            if c in self.lettersGuessed:
                result += c
            else:
                result += '_'
        
        return ' '.join(result)



    def getAvailableLetters(self):
        '''
        lettersGuessed: list, what letters have been guessed so far
        returns: string, comprised of letters that represents what letters have not
        yet been guessed.
        '''
        return [c for c in list(string.ascii_lowercase) if c not in lettersGuessed]

    
    def resetStats(self):
        self.gamesWon = 0
        self.gamesLost = 0
        self.wordsWon = []
        self.wordsLost = []
    
    def getStats(self):
        return self.wordsWon, self.wordsLost, self.gamesWon, self.gamesLost

    def resetGame(self):
        self.lettersGuessed = set()
        self.missedGuesses = 0
        self.secretWord = self.chooseWord()
        

    def playModel(self, guess, max_guesses = 8):

        newGame = False
        wonGame = False
        lostGame = False
        correctGuess = False

        if not self.secretWord:
            self.resetGame()
            newGame = True
            return self.getGuessedWord(), max_guesses - self.missedGuesses, newGame, wonGame, lostGame, correctGuess


        if guess in self.secretWord:
            correctGuess = True
            self.lettersGuessed.add(guess)
            wonGame = self.isWordGuessed()
            if wonGame:
                self.gamesWon += 1
                self.wordsWon += [self.secretWord]
                self.secretWord = ''

            return self.getGuessedWord(), max_guesses - self.missedGuesses, newGame, wonGame, lostGame, correctGuess

        
        self.lettersGuessed.add(guess)
        self.missedGuesses += 1
        
        if self.missedGuesses == max_guesses:
            lostGame = True
            self.gamesLost += 1
            self.wordsLost += [self.secretWord]
            if lostGame:
                self.secretWord = ''

        return self.getGuessedWord(), max_guesses - self.missedGuesses, newGame, wonGame, lostGame, correctGuess





    def playInteractive(self, MAX_GUESSES=8):
        '''
        secretWord: string, the secret word to guess.

        Starts up an interactive game of Hangman.

        * At the start of the game, let the user know how many 
        letters the secretWord contains.

        * Ask the user to supply one guess (i.e. letter) per round.

        * The user should receive feedback immediately after each guess 
        about whether their guess appears in the computers word.

        * After each round, you should also display to the user the 
        partially guessed word so far, as well as letters that the 
        user has not yet guessed.

        Follows the other limitations detailed in the problem write-up.
        '''
        hint, _, _, _, _, _ = self.playModel('!')

        while True:
            print(hint)
            hint, guessesLeft, newGame, wonGame, lostGame, correctGuess  = self.playModel(input("Gimme a guess"))
            print(hint, "left", guessesLeft, "new game", newGame, "did you win", wonGame, "did you lose", lostGame, "\nis guess correct", correctGuess)
            print()

            if wonGame:
                assert not lostGame
                print("you won")
                hint, _, newGame, _, _, _ = self.playModel('!')
                print(self.getStats())
                assert newGame
            
            elif lostGame:
                assert not wonGame
                print("you lost")
                hint, _, newGame, _, _, _ = self.playModel('!')
                print(self.getStats())
                assert newGame



#Hangman('words.txt').playInteractive()
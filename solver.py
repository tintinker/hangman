from hangman import Hangman
import string
import random
from tqdm import tqdm

def preprocessing(wordlist):
    max_word_length = max([len(w) for w in wordlist])

    mapper = {}

    for i in range(max_word_length):
        mapper[i] = {}

        for c in list(string.ascii_lowercase):
            possible_words = [w for w in wordlist if len(w) > i and w[i] == c]
            mapper[i][c] = possible_words

    return mapper

def get_possible_words(hint, mapper):
    chars = hint.split()
    possible_words_sets = []

    for i in range(len(chars)):
        c = chars[i]
        if not c == '_':
            possible_words_sets += [set(mapper[i][c])]
    
    u = set.intersection(*possible_words_sets)
    return u


def algo(hint):
    return random.choice(list(string.ascii_lowercase))

def playSingleGame(h):
    hint, _, _, _, _, _ = h.playModel('!')

    while True:
        print(hint)
        hint, guessesLeft, newGame, wonGame, lostGame, correctGuess  = h.playModel(algo(hint))
        print("left", guessesLeft, "new game", newGame, "did you win", wonGame, "did you lose", lostGame, "\nis guess correct", correctGuess)
        print()

        if wonGame:
            return True
        
        elif lostGame:
            return True

def run():
    h = Hangman('words_250000_train.txt')
    #mapper = preprocessing(h.wordlist)

    for w in h.wordlist:
        if set(w) == set('aple'):
            print(w)
        

    return 
    hint = "a _ _ l _"
    hintlength = 5
    print([w for w in get_possible_words(hint, mapper) if len(w) == hintlength])
    return

    for _ in tqdm(range((10000))):
        playSingleGame(h)

    print(h.getStats())
    h.resetStats()

run()
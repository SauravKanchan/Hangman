# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    value= True
    for i in secretWord:
        if i not in  lettersGuessed:
            value= False
            break
    return value

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word=''
    for i in secretWord:
        if i in  lettersGuessed:
            word+=i
        else:
            word+='_'
    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters='abcdefghijklmnopqrstuvwxyz'
    for i in lettersGuessed:
        letters=letters.replace(i,'')
    return letters


def hangman(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord) ,' letters long.')
    print('-------------')
    lg=[]
    g=8
    won=False
    while 0<g<=8:
        print('You have {0} guesses left.'.format(g))
        print('Available letters:',getAvailableLetters(lg))
        guess=input('Please guess a letter:').lower()
        if guess in lg:
            x=getGuessedWord(secretWord, lg)
            print("Oops! You've already guessed that letter:",x)
            g+=1
        else:
            lg.append(guess)
            if guess in secretWord:
                print("Good guess:",getGuessedWord(secretWord, lg))
                g+=1
            else:
                print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lg))
            if isWordGuessed(secretWord,lg):
                won=True
                print('-----------')
                break
        g-=1
        print('-----------')
    if not won:
        print('Sorry, you ran out of guesses. The word was {0}. '.format(secretWord))
    else:
        print('Congratulations, you won!')

if __name__=='__main__':
    hangman(random.choice(wordlist))
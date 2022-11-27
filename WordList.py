def spliting_words():
    # String of all possible words in the game
    with open('WordTxt.txt') as f:
        secret_wordlist = f.read()
        str(secret_wordlist)

    # Important for giving the list to the main program
    return secret_wordlist.split()

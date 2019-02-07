def hangman():

    word = input('Choose a word: ').lower()
    if not word.isalpha():
        print('That is not a word')
        hangman()
    else:
        temp = ['_' for i in range(len(word))]  ## shown on screen, are blanks for each letter in the word
        turns = 6
        guessed = ''
        
        while turns != 0:   ## Game plays while you still have strikes left
            print('\n'*100 + 'HANGMAN ' + '\n'*4 + 'Strikes left: ' + str(turns) + '\n'*3 + 'Guessed: ' + guessed + '\n' * 5 + ' '.join(temp))
            if not '_' in temp: ## once you've guessed all the letters, you win!
                return 'You Win'
            letter = input('Enter a letter: ')  ## get user's input to guess a letter
            if letter.isalpha() and len(letter) == 1: ## makes sure that input is actually a letter and only a single letter
            
                if letter in word and not letter in guessed:
                    guessed += letter   ## add the letter to the list of already guessed letter
                    position = [pos for pos, char in enumerate(word) if char == letter] ## finds the position of the letter in the word and returns it into a list
                    for i in position:
                        temp[i] = letter    ## fill in the blanks with the correct letter
                elif not letter in word and not letter in guessed:  ## if the letter is not in the word and you haven't already guessed the letter
                    turns -= 1                                      ## you lose a strike
                    guessed += letter               
                
        print('\n' *3 + 'You Lose!' + '\n'*2 + 'The word was: ' + word + '\n'*3)  ## you lose if you run out of strikes
        
        choice = True
        while choice:
            repeat = input('Play Again? (Y/N)')
        
            if repeat == 'Y':
                choice = False
                hangman()
            elif repeat == 'N':
                return 'Thanks for playing!'
            else:
                print('\n' + 'This is not a valid option!')
            
        
            
hangman()
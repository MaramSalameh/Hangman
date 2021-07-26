from hangman_support import *



def playhangman(secretword):
    secretword = secretword.upper()
    #create window
    win = GraphWin('Hangman', WINSIZE, WINSIZE)
    headpoint = draw_gallows(win, WINSIZE)
    wordbox = draw_word_box(win, WINSIZE)
    entrybox = draw_entry_box(win, WINSIZE)
    messagebox = draw_message_box(win, WINSIZE)

    #initialize progress
    progress = list()
    for i in range(0, len(secretword)):
        progress.append("_")
        progress.append(' ')
    progress.pop()


    guesses = list()

    misses = 0
    stop = False
    messagebox.setText('Guess a letter.\nAlready guessed:'+''.join(guesses))
    while stop == False:
        if '_' not in "".join(progress):
            messagebox.setText('You win')
            break
        entrybox.setText("")
        wordbox.setText("".join(progress))
        if misses == 1:
            draw_head(win, headpoint)
        if misses == 2:
            draw_body(win, headpoint)
        if misses == 3:
            draw_limb(win, headpoint, True, True)
        if misses == 4:
            draw_limb(win, headpoint, True, False)
        if misses == 5:
            draw_limb(win, headpoint, False, True)
        if misses == 6:
            draw_limb(win, headpoint, False, False)
            messagebox.setText('You lose.')
            wait_for_guess(win, WINSIZE)
            break

        wait_for_guess(win, WINSIZE)
        guess = entrybox.getText()
        guess = guess.upper()
        if guess.isalpha() == False:
            messagebox.setText('Error enter a letter.\nAlready guessed:'+''.join(guesses))
            continue
        if len(guess) != 1:
            messagebox.setText('Error enter one letter.\nAlready guessed:'+''.join(guesses))
            continue
        if guess in guesses:
            messagebox.setText('Already guessed:'+''.join(guesses))
            continue
        if guess in secretword:
            for i in range(0, len(secretword)):
                if secretword[i]==guess:
                    progress[2*i]= guess
            guesses.append(guess)
            guesses.sort()
            messagebox.setText('Guess a letter.\nAlready guessed:'+''.join(guesses))
            continue
        else:
            misses = misses + 1
            guesses.append(guess)
            guesses.sort()
            messagebox.setText('Guess a letter.\nAlready guessed:'+''.join(guesses))
                
    wait_for_guess(win, WINSIZE)
    win.close()
        
        
    
def main():
    try:
        infile = open('hangman.txt', "r")
    except IOError:
        sys.exit('Error Could not open file.')
    text = infile.read()
    text_list = text.split()
    counter = 0
    for i in range(len(text_list)):
        if text_list[i].isalpha():
            playhangman(text_list[i])
            counter = counter + 1
    if counter == 0:
        print('Error no usable words.')
    infile.close()
        
    
    
    
main()
    
    

''' 
Program: CS 115 Project 3
Author: Maram Salameh
Description: This program will play a series of interactive,
graphical games of Hangman with the user.
'''

from hangman_support import *
#from graphics import *

def hangman(word):
    word = word.upper()
    win = GraphWin('Hangman', WINSIZE, WINSIZE)
    headpoint = draw_gallows(win, WINSIZE)
    wordbox = draw_word_box(win, WINSIZE)
    entrybox = draw_entry_box(win, WINSIZE)
    messagebox = draw_message_box(win, WINSIZE)

    #Loop over the lenght of the word to play a round of hangman
    play = list()
    for i in range(0, len(word)):
        play.append("_")
        play.append(' ')
    play.pop()

def wait_for_guess(win, WINSIZE):
        guess = entrybox.getText()
        guess = guess.upper()
        messagebox = draw_message_box(win, WINSIZE)
        if guess.isalpha() == False:
            messagebox.setText('Error enter a letter.\nAlready guessed:'+''.join(guesses))
        if len(guess) != 1:
            messagebox.setText('Error enter one letter.\nAlready guessed:'+''.join(guesses))
        if guess in guesses:
            messagebox.setText('Already guessed:'+''.join(guesses))
        if guess in word:
            for i in range(0, len(word)):
                if word[i]==guess:
                    play[2*i]= guess
            guesses.append(guess)
            guesses.sort()
            messagebox.setText('Guess a letter.\nAlready guessed:'+''.join(guesses))
        else:
            Incorrect = Incorrect + 1
            guesses.append(guess)
            guesses.sort()
            messagebox.setText('Guess a letter.\nAlready guessed:'+''.join(guesses))
                            
        return wait_for_guess(win, WINSIZE)
        win.close()

#Test whether the player guessed a correct letter and draw a part of hang man if guess is incorrect
def misses(Incorrect):
    messagebox = draw_message_box(win, WINSIZE)
    guesses = list()
    Incorrect = 0
    stop = False
    messagebox.setText('Guess a letter.\nAlready guessed:'+''.join(guesses))
    while stop == False:
        if '_' not in "".join(play):
            messagebox.setText('You win')
            break
        entrybox.setText("")
        wordbox.setText("".join(play))
        if Incorrect == 1:
            draw_head(win, headpoint)
        if Incorrect == 2:
            draw_body(win, headpoint)
        if Incorrect == 3:
            draw_limb(win, headpoint, True, True)
        if Incorrect == 4:
            draw_limb(win, headpoint, True, False)
        if Incorrect == 5:
            draw_limb(win, headpoint, False, True)
        if Incorrect == 6:
            draw_limb(win, headpoint, False, False)
            messagebox.setText('You lose.')
            wait_for_guess(win, WINSIZE)
            break


def main():
    
    try:
        infile = open('hangman.txt', "r")
    except IOError:
        sys.exit('Error could not open file.')
    text = infile.read()
    text_list = text.split()
    counter = 0
    for i in range(len(text_list)):
        if text_list[i].isalpha():
            hangman(text_list[i])
            misses(text_list[i])
            wait_for_guess(win, WINSIZE)
            counter = counter + 1
    if counter == 0:
        print('Error no usable words.')
    infile.close()     
    
main()

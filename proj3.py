"""
Program: CS 115 Project 3
Name: Maram Salameh
Description: This program will ask the user if they wish to play a game of
hangman
"""


import sys
from graphics import *
from hangman_support import *


def create_word_box(window, WINSIZE):
    """
    parameteres:
        window - the window to create box in
        WINSIZE - the winsize predifined by hangman support
    returns: textbox object
    """
    text_box = Text(Point(0.75 * WINSIZE / 2, 0.75 * WINSIZE / 2), '')
    text_box.setFace('times roman')
    text_box.setSize(36)
    text_box.draw(window)
    return text_box


def create_bottom_line(win, gallows_upper_left, gallows_lower_right):
    """
    parameters:
        win - the window to draw in
        gallows_upper_left - a Point for the upper left point of the
        gallows area
        gallows_lower_right - a Point for the lower right point of
        the gallows area
    """
    line_Y = gallows_lower_right.getY() - 20
    left_pt = Point(20 + gallows_upper_left.getX(), line_Y)
    right_pt = Point(20 + gallows_lower_right.getX(), line_Y)
    bottom_line = Line(left_pt, right_pt)
    bottom_line.draw(win)
    return bottom_line


def create_gallows(win, WINSIZE):
    """
    parameteres:
        win - the window to create box in
        WINSIZE - the winsize predifined by hangman support
    returns: gallows
    """
    # make gallows corners
    upper_left = Point(0.75 * WINSIZE, 0)
    lower_right = Point(WINSIZE, 0.75 * WINSIZE)

    bottom_line = create_bottom_line(win, upper_left, lower_right)

    # Vertical line:
    vert_top = Point(bottom_line.getCenter().getX(), upper_left.getY() + 20)
    vert_line = Line(vert_top, bottom_line.getCenter())
    vert_line.draw(win)

    # Horizontal line at top:
    horz_left = Point(bottom_line.getP1().getX(), vert_top.getY())
    horz_line = Line(horz_left, vert_top)
    horz_line.draw(win)

    #small vertical:
    head_top = Point(horz_left.getX(), horz_left.getY() + 50)
    Line(horz_left, head_top).draw(win)
    return head_top


def create_entry_box(win, WINSIZE):
    """
    parameteres:
        win - the window to create box in
        WINSIZE - the winsize predifined by hangman support
    returns: entry box object
    """
    entry_box = Entry(Point(WINSIZE * 0.75 / 2, WINSIZE * 0.9), 1)
    guess_box = Rectangle(Point(WINSIZE * 0.75 / 2 + 50, WINSIZE * 0.9 - 20),
                  Point(WINSIZE * 0.75 / 2 + 100, WINSIZE * 0.9 + 20))
    guess_text = Text(Point(WINSIZE * 0.75 / 2 + 75, WINSIZE * 0.9),
                'Guess!')
    entry_box.setSize(16)
    entry_box.draw(win)
    guess_box.setFill('white')
    guess_box.draw(win)
    guess_text.draw(win)
    return entry_box


def create_message_box(win, WINSIZE):
    """
    parameteres:
        win - the window to create box in
        WINSIZE - the winsize predifined by hangman support
    returns: message box object
    """
    message_box = Text(Point(WINSIZE * 0.75 / 2, WINSIZE * 0.8),
           'Guess a letter.\nAlready guessed:')
    message_box.setSize(25)
    message_box.draw(win)
    return message_box


def wait_for_guess(win, WINSIZE):
    """
    parameteres:
        win - the window to create box in
        WINSIZE - the winsize predifined by hangman support
    returns: loops forever and break when mouse is clicked on the box button
    """
    while True:
        mouse_click = win.getMouse()
        if WINSIZE * 0.75 / 2 + 50 < mouse_click.getX() \
             < WINSIZE * 0.75 / 2 + 100 \
           and WINSIZE * 0.9 - 20 < mouse_click.getY() \
             < WINSIZE * 0.9 + 20:
            return


def create_head(win, head_point):
    """
    parameteres:
        win - the window to create box in
        head_point - point where head will be
    """
    Circle(Point(head_point.getX(), head_point.getY() + 50), 50).draw(win)


def draw_body(win, head_point):
    """
    parameteres:
        win - the window to create box in
        head_point - point where head will be
    """
    top = Point(head_point.getX(), head_point.getY() + 100)
    bottom = Point(top.getX(), top.getY() + 200)
    Line(top, bottom).draw(win)


def draw_limb(win, head_point, isLeft, isArm):
    """
    parameteres:
        win - the window to create box in
        head_point - point where head will be
        isleft - true if you want a left arm/ leg
        isarm - true if you want right arm/leg
    """
    offset_X = 75
    if is_Left is True:
        offsetX *= -1
    if is_Arm is True:
        offsetYbody = 200
        offsetYend = 150
    else:
        offsetYbody = 300
        offsetYend = 350
    body = Point(head_point.getX(), head_point.getY() + offsetYbody)
    end = Point(head_point.getX() + offset_X, head_point.getY() + offsetYend)
    Line(body, end).draw(win)


def readfile(filename):
    """
    Reads the entire contents of a file into a single string using
    the read() method.

    Parameter: the name of the file to read (as a string)
    Returns: the text in the file as a large, possibly multi-line, string
    """

    infile = open(filename, "r")  # open file for reading
    word_list = []
# Use Python's file read function to read the file contents
    filetext = infile.read().splitlines()
    infile.close()  # close the file
# check for valid words
    for item in filetext:
        if item.isalpha() is True:
            word_list.append(item)
# return a list with valid words
    return word_list


def print_list(list_to_print):
    """
    Print the contents of a list.

    Parameter: the list to print
    Returns: nothing
    """

    for i, item in enumerate(list_to_print):
            print(i, ': ', item, sep="")


def main():
    word_list = readfile('hangman.txt')
    if len(word_list) == 0:
        print('Error Could not open file/ invalid file.')
        sys.exit()
    secret_word = choose_word(word_list)
    secret_word = secret_word.upper()
    while True:
        play = input('Would you like to play a game of Hangman? \nreply with Y or N: ')
        if play == 'Y' or play == 'y':
            window = GraphWin('Hangman', WINSIZE, WINSIZE)
            headpoint = create_gallows(window, WINSIZE)
            wordbox = create_word_box(window, WINSIZE)
            entrybox = create_entry_box(window, WINSIZE)
            messagebox = create_message_box(window, WINSIZE)
            progress = list()
            for i in range(0, len(secret_word)):
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
                    create_head(window, headpoint)
                if misses == 2:
                    draw_body(window, headpoint)
                if misses == 3:
                    create_limb(window, headpoint, True, True)
                if misses == 4:
                    create_limb(window, headpoint, True, False)
                if misses == 5:
                    create_limb(window, headpoint, False, True)
                if misses == 6:
                    create_limb(window, headpoint, False, False)
                    messagebox.setText('You lose.')
                    wait_for_guess(window, WINSIZE)
                    break

                wait_for_guess(window, WINSIZE)
                guess = entrybox.getText()
                guess = guess.upper()
                if guess.isalpha() == False:
                    messagebox.setText('Error enter a letter.\nAlready guessed:'
                                       +''.join(guesses))
                    continue
                if len(guess) != 1:
                    messagebox.setText('Error enter one letter.\nAlready guessed:'
                                       +''.join(guesses))
                    continue
                if guess in guesses:
                    messagebox.setText('Already guessed:'
                                       +''.join(guesses))
                    continue
                if guess in secret_word:
                    for i in range(0, len(secret_word)):
                        if secret_word[i] == guess:
                            progress[2*i] = guess
                    guesses.append(guess)
                    guesses.sort()
                    messagebox.setText('Guess a letter.\nAlready guessed:'
                                       +''.join(guesses))
                    continue
                else:
                    misses = misses + 1
                    guesses.append(guess)
                    guesses.sort()
                    messagebox.setText('Guess a letter.\nAlready guessed:'
                                       +''.join(guesses))
                        
            window.getMouse()
            window.close()

        elif play == 'N' or play == 'n':
            sys.exit()
        else:
        #print error message
            print('Error: Invalid answer!')
   

main()

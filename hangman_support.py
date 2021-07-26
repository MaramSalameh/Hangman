''' Helpful Hangman functions

    Includes:
    - draw_word_box: create and draw text box for the secret word
      so that you only have to call setText to change it
    - draw gallows: draw the initial gallows (no hangman included)
    - draw_entry_box: create and draw a box for the user to enter
      their guess
    - draw_message_box: create and draw a text box to print
      messages for the user (initialized to 'Guess a letter')
    - wait_for_guess: waits for the user to click the 'Guess!' button
   
    Functions for drawing body parts:
    - draw_head
    - draw_body
    - draw_limb

    See the specific documentation for each function.

    Author: Suzanne Rivoire ''' 

from graphics import *

WINSIZE = 600

# Function: draw_word_box 
# Parameters:
#    - win = the window to draw in (should be square)
#    - WINSIZE = the width (also height) of the window
# 
# Creates and draws an empty text box
# This box will contain the text (or blanks) for the
# user's secret word.
#
# Returns the text box object so that you can update
# the text with the user's guesses by calling setText.
def draw_word_box(win, WINSIZE):
    textbox = Text(Point(0.75 * WINSIZE / 2, 0.75 * WINSIZE / 2), '')
    textbox.setFace('courier')
    textbox.setSize(36)
    textbox.draw(win)
    return textbox
    

# Function: draw_gallows
# Parameters:
#    - win = the window to draw in (should be square)
#    - WINSIZE = the width (or height of the window) --
#      assumed to be at least 100x100
# Draws the gallows on the window
#
# You only have to call this once.
#
# Returns the coordinates of the point where the top of the head
# should go
#
def draw_gallows(win, WINSIZE):
    # Establish gallows corners
    gallows_upper_left = Point(0.75 * WINSIZE, 0)
    gallows_lower_right = Point(WINSIZE, 0.75 * WINSIZE)

    bottom_line = draw_bottom_line(win, gallows_upper_left,
        gallows_lower_right)

    # Vertical line: draw from center of bottom line to
    # 10% of the distance from the top of the gallows area
    vtop = Point(bottom_line.getCenter().getX(), 
        gallows_upper_left.getY() + 20)
    vline = Line(vtop, bottom_line.getCenter())
    vline.draw(win)

    # Horizontal line at top: draw from top of vertical line
    # to left of the bottom line
    hleft = Point(bottom_line.getP1().getX(), vtop.getY())
    hline = Line(hleft, vtop)
    hline.draw(win)

    # Tiny little vertical line to hang a guy from
    headtop = Point(hleft.getX(), hleft.getY() + 50)
    Line(hleft, headtop).draw(win)
    return headtop


# Function: draw_bottom_line
# This is a helper function - YOU DO NOT NEED TO CALL IT FROM YOUR CODE
# Parameters:
#    - win = the window to draw in
#    - gallows_upper_left = a Point for the upper-left corner of the
#      gallows area
#    - gallows_lower_right = a Point for the lower-right corner of
#      the gallows area
# Draws the bottom horizontal line of the gallows, which will
# go across the bottom of the allowed gallows area
# (minus a small offset in case the bottom of the gallows area
# is also the bottom of the window)
#
# Returns the line it drew (as a Line)
def draw_bottom_line(win, gallows_upper_left, gallows_lower_right):
    lineY = gallows_lower_right.getY() - 20
    left_pt = Point(20 + gallows_upper_left.getX(), lineY)
    right_pt = Point(20 + gallows_lower_right.getX(), lineY)
    bottom_line = Line(left_pt, right_pt)
    bottom_line.draw(win)
    return bottom_line

# Function: draw_entry_box
# Parameters:
#     - win = the window to draw in
#     - WINSIZE = the size of the window
# Creates a box for the user to enter a guess and a
# big 'Guess' button
#
# Returns the entry box so that you can retrieve the user's guess from it
def draw_entry_box(win, WINSIZE):
    entrybox = Entry(Point(WINSIZE * 0.75 / 2, WINSIZE * 0.9), 1)
    guessbox = Rectangle(Point(WINSIZE * 0.75 / 2 + 50, WINSIZE * 0.9 - 20),
                  Point(WINSIZE * 0.75 / 2 + 100, WINSIZE * 0.9 + 20))
    guesstext = Text(Point(WINSIZE * 0.75 / 2 + 75, WINSIZE * 0.9),
                'Guess!')
    entrybox.setSize(16)
    entrybox.draw(win)
    guessbox.setFill('LightGray')
    guessbox.draw(win)
    guesstext.draw(win)
    return entrybox

# Function: draw_message_box
# Parameters: win, WINSIZE
# Creates a text box for communicating with user
# and initializes to 'Guess a letter.'
#
# Returns text box so that you can update it with messages for the user
def draw_message_box(win, WINSIZE):
    messagebox = Text(Point(WINSIZE * 0.75 / 2, WINSIZE * 0.8),
           'Guess a letter.\nAlready guessed:')
    messagebox.setSize(20)
    messagebox.draw(win)
    return messagebox

# Function: wait_for_guess
# Parameters: win, WINSIZE
# Waits for the user to type some text and click the 'Guess!' button
# After this function is called, it's safe to call getText() on the
# entry box
def wait_for_guess(win, WINSIZE):
    # Infinite loop - will break out of it by 
    # returning if the user clicks the button
    while True:
        mousept = win.getMouse()
        if WINSIZE * 0.75 / 2 + 50 < mousept.getX() \
             < WINSIZE * 0.75 / 2 + 100 \
           and WINSIZE * 0.9 - 20 < mousept.getY() \
             < WINSIZE * 0.9 + 20:
            return 

# Function: draw_head
# Parameters:
#   - win (the window)
#   - headpoint (the Point where the top of the hanged
#     man's head should be)
# Draws the head on the gallows
def draw_head(win, headpoint):
    Circle(Point(headpoint.getX(), headpoint.getY() + 50), 50).draw(win)


# Function: draw_body
# Parameters:
#   - win (the window)
#   - headpoint (the Point where the top of the hanged
#     man's head should be)
# Draws the body on the gallows
def draw_body(win, headpoint):
    top = Point(headpoint.getX(), headpoint.getY() + 100)
    bottom = Point(top.getX(), top.getY() + 200)
    Line(top, bottom).draw(win)


# Function: draw_limb
# Draws an arm or leg on the gallows
# Parameters:
#   - win (the window)
#   - headpoint (the Point where the top of the hanged
#     man's head should be)
#   - isLeft: True if you want to draw a left arm
#     or left leg, otherwise False
#   - isArm: True if you want a left or right arm,
#     otherwise False
def draw_limb(win, headpoint, isLeft, isArm):
    offsetX = 75
    if isLeft: offsetX *= -1
    if isArm:
        offsetYbody = 200
        offsetYend = 150
    else:
        offsetYbody = 300
        offsetYend = 350
    body = Point(headpoint.getX(), headpoint.getY() + offsetYbody)
    end = Point(headpoint.getX() + offsetX, headpoint.getY() + offsetYend)
    Line(body, end).draw(win)



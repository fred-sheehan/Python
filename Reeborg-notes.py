# ===========================================================
# Home 1 and Home 2

move()
move()

# ===========================================================
# Home 3

move()
move()
turn_left()
move()

# ===========================================================
# Home 4

# create a function to move 3 squares
def move_3():
    move()
    move()
    move()

# create a function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# create a function to traverse each inside path
def big_left():
    move_3()
    turn_left()
    move_3()

# create a function to travel around the end corners
def little_right():
    turn_right()
    move()
    turn_right()

# loop through the first 3 inside paths and around the end corners using the functions we created
for corners in range(3):
    big_left()
    little_right()

# and finally travel the last inside path to home
big_left()

# ===========================================================
# around 1 and around 1 variable

put()   # leave a token to stop us at the end
move()  # move at least a square else...

# ...this loop will not run if there is a token on
# its starting square.
while not object_here(): # while there is no token...
    if front_is_clear(): # and we have a clear path...
        move()           # just move..
    else:
        turn_left()     # but turn left if we hit a wall

# ===========================================================
# Around 1 apple

for square in range(36):
    if front_is_clear():
        move()
    if object_here():
        take()
    if wall_in_front():
        turn_left()

# ===========================================================
# Around 2

# create a function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

put()  # drop a token to stop us later
move() # move so our loop starts

while not object_here():  # while not at the end...
    if right_is_clear():  # check our right side is clear,
        turn_right()      # if so, we always turn right...
        move()            # and move
    elif wall_in_front(): # but if there is a wall in front,
        turn_left()       # always turn left, until clear
    else:
        move()            # if no wall, just move

# ===========================================================
# Centre 1

def turn():
    turn_left()
    turn_left()

def move_a_step():
    take('token')
    move()
    put('token')

put('token')

while front_is_clear():
    move()

put('token')
turn()
move_a_step()

while front_is_clear():
    move()
    if object_here():
        turn()
        move_a_step()

turn()

while front_is_clear():
    move()
    if object_here():
        take('token')
        break

# ===========================================================
# Hurdles 1 to 4

# create a function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():      # while not at the end...
    if right_is_clear():  # check our right side is clear,
        turn_right()      # if so, we always turn right...
        move()            # and move
    elif wall_in_front(): # but if there is a wall in front,
        turn_left()       # always turn left, until clear
    else:
        move()            # if no wall, just move

# ===========================================================
# Maze 1 to 4 and edge cases

# create a function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# only added to handle (rare) edge case of the maze
while front_is_clear():
    move()
turn_left()

while not at_goal():      # while not at the end...
    if right_is_clear():  # check our right side is clear,
        turn_right()      # if so, we always turn right...
        move()            # and move
    elif wall_in_front(): # but if there is a wall in front,
        turn_left()       # always turn left, until clear
    else:
        move()            # if no wall, just move

# ===========================================================
# Newspapers 0

# create a function to move 2 squares
def move_2():
    move()
    move()

# create a function to turn around
def turn_around():
    turn_left()
    turn_left()

# create a function to turn right
def turn_right():
    turn_around()
    turn_left()

# going up or down stairs is always the same movements
def up_or_down():
    turn_left()
    move()
    turn_right()

# take() the newspaper...
take()

# ...and carry it upstairs using the functions we created
for levels in range(3):
    up_or_down()
    move_2()

# put() newspaper down at location...
put()

turn_around()

# ...and make our way back downstairs in reverse order
for levels in range(3):
    move_2()
    up_or_down()

# ===========================================================
# Newspapers 1

# create a function to move 2 squares
def move_2():
    move()
    move()

# create a function to turn around
def turn_around():
    turn_left()
    turn_left()

# create a function to turn right
def turn_right():
    turn_around()
    turn_left()

# going up or down stairs is always the same movements
def up_or_down():
    turn_left()
    move()
    turn_right()

# take() the newspaper...
take()

# ...and carry it upstairs using the functions we created
for levels in range(3):
    up_or_down()
    move_2()

# put() newspaper down at location...
put()

turn_around()

# make sure we take('token') left for us
take('token')

# ...and make our way back downstairs in reverse order
for levels in range(3):
    move_2()
    up_or_down()

# ===========================================================


# ===========================================================
# building up our libarary of functions

# we can then import these functions into our main program
from library import turn_right, turn_around, step_back, move_2, move_3, move_4, move_5

def move_2():
    move()
    move()

def move_3():
    move()
    move()
    move()

def move_4():
    move()
    move()
    move()
    move()

def move_5():
    move()
    move()
    move()
    move()
    move()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
    turn_left()

def step_back():
    turn_around()
    move()
    turn_around()

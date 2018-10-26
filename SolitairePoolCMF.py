##Cassie Fox
##24 of May 2017
##CS 21 Spring 2017

##Program: Solitaire Pool
##Opens graphics window to play game with user.

##User has to 'shoot' white ball at red ball.
##User has to hit a randomly selected number of walls before
##eventually hitting the red ball.

#importing full graphics library, math library, randrange, and sleep
from graphics import *
from random import randrange
from math import *
from time import sleep

##makeText function takes a graphics window, a string,
##an integer for the text size, and ints for the x and y coords.
##of the text

##makeText then creates the text according to the given parameters
##makeText draws the text and returns it in case we wish
##to store it in main
def makeText(window,string,size,x_pos,y_pos):
    text_line = Text(Point(x_pos, y_pos),string)
    text_line.setOutline("white")
    text_line.setSize(size)
    
    text_line.draw(window)

    return text_line

##eraseText takes a list of items and marches through the list,
##undrawing each item
def eraseText(list_of_things):
    for item in list_of_things:
        item.undraw()

##our intro function only takes a window
def intro(window):
    ##we first create a title string
    title = "Solitaire Pool"

    ##then we make an empty list that will house each string of 
    ##the game instructions.

    ##we do not add the title to this list because we eventually 
    ##will want to erase instructions while keeping title.
    text_list = []

    ##we call each string one part of the directions and add it to
    ##our list of direction strings.
    direction1 = "In this game, we'll start with a rectangular game board with 4 walls."
    text_list.append(direction1)

    direction2 = "A randomly placed white 'cue ball' will appear,"
    text_list.append(direction2)

    direction3 = "and a randomly placed red 'target ball' will appear."
    text_list.append(direction3)

    direction4 = "Then, a random integer will be given as your 'goal.'"
    text_list.append(direction4)

    direction5 = "You will then have to click somewhere, and the cue ball will go in that direction."
    text_list.append(direction5)

    direction6 = "Your goal is to hit the cue ball on walls the 'goal' number of times."
    text_list.append(direction6)

    direction7 = "After hitting it on the walls exactly that many times,"
    text_list.append(direction7)

    direction8 = "the final objective is to hit the target ball."
    text_list.append(direction8)

    direction9 = "Think you can do it? Click anywhere when you're ready."
    text_list.append(direction9)

    ##we then create the title a bit above the center of the graphics window
    title_created = makeText(window,title,15,300,425)

    ##then we make a new list that, rather than being a list of strings,
    ##it will be a list of the actual created text.
    created_text_list=[]

    ##our title is at y=425, and we want our instructions to start at y=375
    ##so we call 375 the y_position; it will be our y-coord for
    ##the very first instruction
    y_position = 375

    ##then we march through each string in our list of strings
    for item in text_list:
        ##we call the newly made text created_text
        created_text = makeText(window,item,12,300,y_position)
        ##we subtract 25 from our y_position because we want a new line of text
        ##every 25 pixels in the y direction
        y_position -= 25
        ##we then append the created text to our list
        ##this will allow for easy erasure of instructions
        created_text_list.append(created_text)

    ##we ask the user to click anwhere to start the game...
    window.getMouse()

    ##after they click, all of that text that we created is erased via eraseText
    eraseText(created_text_list)
    
    ##the only thing we care about now is that title text that we created
    ##so we return it to main
    return title_created

##makeWalls takes 2 points as inputs
##it then creates a white line between the two points, width 3 pixels
##returns the created line, but does not draw it in the window
def makeWalls(point1,point2):
    wall = Line(point1,point2)
    wall.setOutline("white")
    wall.setWidth(3)

    return wall

##we only need 2 circles in the game - the cue and target balls
##both are in random locations, with the same radius
##the only thing different in their creation is their color
##so, makeCircle only takes a color, and does the rest internally
##both circles have a radius of 15
def makeCircle(color):
    ##we use randrange to randomly generate x and y coords
    ##game board x goes from 30 to 570, and since circle radius is 15,
    ##we make sure that the center of the circle is at least 20 pixels away
    ##from a wall
    x_coord = randrange(50,550)
    y_coord = randrange(50,455)

    ##after getting coords, we turn them into a point, the center
    center_pt = Point(x_coord,y_coord)

    ##then, we make the circle with center found above and radius 15
    the_circle = Circle(center_pt,15)
    ##outline and fill are the input color
    the_circle.setOutline(color)
    the_circle.setFill(color)

    ##function returns the circle
    return the_circle

##this function takes the two circles - cue ball and target
def diff_btwn_circ(cue,target):
    ##grabs the center point of cue ball
    cue_pt = cue.getCenter()
    ##then grabs x and y coords of cue ball center
    cueX = cue_pt.getX()
    cueY = cue_pt.getY()

    ##grabs the center point of target ball
    target_pt = target.getCenter()
    ##then grabs x and y coords of target ball center
    targetX = target_pt.getX()
    targetY = target_pt.getY()

    ##diff is the distance formula sqrt(((x1-x2)^2)+((y1-y2)^2))
    ##applied with the center points of each ball
    diff = sqrt(((cueX-targetX)**2)+((cueY-targetY)**2))

    ##the distance betweeen center points, diff, is returned
    return diff

##self-explanatory, gets a random number between 1 and 4
##this is the number of walls user must hit before hitting the ball
def get_num_walls():
    num_walls = randrange(1,4)

    ##the number of walls is then returned to main
    return num_walls

##this function takes the point the user clicked, the two circles,
##the list of the walls, and the number of walls to hit
##it moves the cue ball where it ends up going to, and it returns
##True or False, true if it's a win, or false if it's a loss
##Boolean function
def win_or_lose(user_click,cue_circle,target_circle,list_of_walls,walls_to_hit):
    ##first thing we do is get coords of user click
    userX = user_click.getX()    
    userY = user_click.getY()

    ##then we get coords of cue ball center
    cue_center = cue_circle.getCenter()
    cueX = cue_center.getX()
    cueY = cue_center.getY()

    ##dx is difference between x-coords, divided by 50 to make a tiny dx
    ##dy is same but w/ y-coords
    ##these will be how much at a time the ball is moved by
    dx = (userX - cueX)/50
    dy = (userY - cueY)/50

    ##we find the distance between the balls initially before moving
    ball_diff = diff_btwn_circ(cue_circle,target_circle)

    ##we tell our function that initially, the cue ball is not
    ##next to the left and right walls (Xwalls), nor is it next to the top and bottom walls
    ##(Ywalls)
    close_to_Xwall = False
    close_to_Ywall = False

    ##we count up the number of times the cue ball hits wall - accumulation loop
    wall_hits = 0

    ##now we start a while loop that continues until we hit walls more than the goal
    ##number of times or until the distance between the balls is less than their
    ##two radii, less than 30
    while (wall_hits <= walls_to_hit) and (ball_diff > 30):

        ##within it is nested another while loop; this continues while the cue ball is not
        ##close to any walls and while the distance between the balls is greater than 30

        ##while these conditions are true, we move the cue ball dx and dy, then pause the
        ##program for .05 seconds, then check to see if the balls are touching
        ##if they are not touching, we check to see if the cue is close to any walls

        ##if the balls are touching, we exit out of the big while loop, so this choose
        ##your own adventure goes straight down to the bottom

        ##if the cue is touching a wall, we do other things
        while (close_to_Xwall == False) and (close_to_Ywall == False) and (ball_diff > 30):
            cue_circle.move(dx,dy)
            sleep(0.05)
            ball_diff = diff_btwn_circ(cue_circle,target_circle)
            close_to_Xwall = nearXWall(cue_circle,list_of_walls)
            close_to_Ywall = nearYWall(cue_circle,list_of_walls)

        ##if we are close to the left or right wall,
        ##we add one to our number of hits to the wall, and make dx negative
        if close_to_Xwall == True:
            wall_hits += 1
            dx *= -1
            ##then, with our new dx, we take two "steps" away from the wall
            for i in range(2):
                cue_circle.move(dx,dy)
                sleep(0.05)
            ##then, we get a new Boolean on if we are close to a left or right wall
            ##(should be false, which should take us back to the start of our while loop)
            close_to_Xwall = nearXWall(cue_circle,list_of_walls)

        ##if we are close to the top or bottom wall,
        ##we add one to our number of hits to the wall, and make dy negative 
        if close_to_Ywall == True:
            wall_hits += 1
            dy *= -1
            ##then, with our new dy, we take two "steps" away from the wall
            for i in range(2):
                cue_circle.move(dx,dy)
                sleep(0.05)
            ##then, we get a new Boolean on if we are close to a top or bottom wall
            ##(should be false, which should take us back to the start of our while loop)
            close_to_Ywall = nearYWall(cue_circle,list_of_walls)

    ##the only way to win is if the number of walls hit is equal to goal
    ##so that is the only way we get True back
    if wall_hits == walls_to_hit:
        return True
    ##anything else returns False
    else:
        return False

##function to check if cue ball is near top or bottom wall
##returns True or False, True if it is near a wall, False if not
def nearYWall(cue_circle,list_of_walls):
    ##gets coords of center of cue ball
    cue_center = cue_circle.getCenter()
    cueX = cue_center.getX()
    cueY = cue_center.getY()

    ##sets up accumulation loop to tell us how many walls we are close to
    wall_close_count = 0

    ##marches through each wall, only really focuses on 1 and 3 in list,
    ##which are top and bottom, respectively
    for item in list_of_walls:
        ##if we are looking at index 1, it is top wall
        if item == list_of_walls[1]:
            ##diff in Y values is 475, y coords of top line, minus y coord of cue
            dy = 475 - cueY
            ##radius is 15, width of line is 3 so if dy <= 17,
            ##we are close to the wall and its time to bounce off
            if dy <= 17:
                ##so we add 1 to our wall_close_count
                wall_close_count+=1
        ##index 3 is bottom wall
        if item == list_of_walls[3]:
            ##diff in Y values is the y coord of the cue minus 30, y coords of bottom
            ##line
            dy = cueY - 30
            ##radius is 15, width of line is 3 so if dy <= 17,
            ##we are close to the wall and its time to bounce off
            if dy <= 17:
                wall_close_count+=1

    ##if wall_close_count is greater than zero, we must move, as we are too close
    ##(True is returned)
    if wall_close_count > 0:
        return True
    else:
        return False

##function to check if cue ball is near left (index 0) or right (index 2) wall
##returns True or False, True if it is near a wall, False if not
##please see above function for detailed explanation; this is essentially
##the same
def nearXWall(cue_circle,list_of_walls):
    cue_center = cue_circle.getCenter()
    cueX = cue_center.getX()
    cueY = cue_center.getY()

    wall_close_count = 0
    
    for item in list_of_walls:
        if item == list_of_walls[0]:
            dx = cueX - 30
            if dx <= 17:
                wall_close_count+=1
        if item == list_of_walls[2]:
            dx = 570 - cueX
            if dx <= 17:
                wall_close_count+=1

    if wall_close_count > 0:
        return True
    else:
        return False
        
def main():
    ##we create our graphics window, 600 x 600,
    ##it has a black background for ease of reading
    win = GraphWin("Pool Solitaire", 600, 600)
    win.setCoords(0, 0, 600, 600)
    win.setBackground("black")

    ##we begin a master list of text to eventually be erased
    text_erasure_list = []

    ##the title of the game is captured here from intro
    the_game_title = intro(win)
    ##we add the title to list of text erasures
    text_erasure_list.append(the_game_title)

    ##we then move the title up to the top of the window 
    the_game_title.move(0,125)

    ##now we create a master list of objects to eventually be erased
    object_erasure_list = []

    ##and NOW we make a list of walls for our 'pool table'
    walls = []

    ##here, we use the makeWalls function to - what do ya know - make some walls
    ##the game board is rectangle w/ corner Point(30,30), opposite corner
    ##Point(570,475)
    wall1 = makeWalls(Point(30,30),Point(30,475))
    ##as we go, we add the created walls to the list of walls
    walls.append(wall1)
    
    wall2 = makeWalls(Point(30,475),Point(570,475))
    walls.append(wall2)
    
    wall3 = makeWalls(Point(570,475),Point(570,30))
    walls.append(wall3)
    
    wall4 = makeWalls(Point(570,30),Point(30,30))
    walls.append(wall4)

    ##marches through each wall in list of walls
    ##draws each wall
    ##then, adds each wall to list of objects to eventually erase
    for item in walls:
        item.draw(win)
        object_erasure_list.append(item)

    ##now, we use the makeCircle function to make a white circle, the cue ball
    cue_ball = makeCircle("white")
    ##then, we draw the cue ball
    cue_ball.draw(win)
    ##then, we add it to our object erasing list
    object_erasure_list.append(cue_ball)

    ##we then make a circle for the target ball
    target_ball = makeCircle("red")
    
    ##before we draw the target ball though, we need to make sure it isn't
    ##too close to the cue ball, so we send both balls through the diff_btwn_circ function
    ball_diff = diff_btwn_circ(cue_ball,target_ball) 

    ##since both balls have a radius of 15, the closest they should really be is 31
    ##pixels apart, center to center

    ##31 apart would mean not touching, but just barely
    ##hardly any space between them, so we made it so if the distance between the balls
    ##is less than or equal to 40, a new target ball is created, and we calculate
    ##the distance between cue and this new ball

    ##while the distance between the randomly generated balls is less equal to 40,
    ##we keep creating new target balls until finally they are a proper distance apart
    while ball_diff <=40:
        target_ball = makeCircle("red")
        ball_diff = diff_btwn_circ(cue_ball,target_ball) 

    ##finally, once we have appropriate cue and target balls, we draw the target ball
    ##then we add it to object erasure list
    target_ball.draw(win)
    object_erasure_list.append(target_ball)

    ##now, we want to know how many walls we have to hit to win
    ##so we get a randomly generated number from get_num_walls
    walls_hit_goal = get_num_walls()

    ##then, we make a string telling you how many walls you need to hit
    text = "Goal: Hit "+str(walls_hit_goal)+" wall(s)."

    ##after creating this string, we use makeText to bring the string to life in the graphics window
    ##then, we add that goal text to the text erasure list
    num_goal = makeText(win,text,10,300,525)
    text_erasure_list.append(num_goal)

    ##now, we make a string asking the user to click the direction
    ##they want the ball to go in
    click_string = "Click in the direction you want the cue ball to go."
    ##we use makeText to make the text
    click_where = makeText(win,click_string,10,300,500)
    ##we don't bother adding it to the erasure list because we will delete it
    ##as soon as the user clicks something, but we want to leave the rest of the text be

    ##user clicks, and we store that click because it is very important
    user_click = win.getMouse()

    ##after the user clicks, the clicking instructions are undrawn
    click_where.undraw()

    ##now, we want the result - if the user wins or loses, which goes to a Boolean function
    ##this Boolean moves the cue ball until a win or loss situation is reached
    ##True = win, False = loss
    result = win_or_lose(user_click,cue_ball,target_ball,walls,walls_hit_goal)

    ##if we win, then we erase all of the objects and text in our erasure lists
    if result == True:
        eraseText(object_erasure_list)
        eraseText(text_erasure_list)
        ##then, we make a string win_text to tell user they win
        win_text = "Yay! Looks like you won this round of Solitaire Pool!"

        ##we then create the text
        makeText(win,win_text,13,300,312)

        ##create string telling user to click to exit
        exit_click = "Click anywhere to exit."

        ##create the text
        makeText(win,exit_click,13,300,288)

        ##get mouse click and close window
        win.getMouse()
        win.close()

    ##if we lose, then we erase all of the objects and text in our erasure lists
    if result == False:
        eraseText(object_erasure_list)
        eraseText(text_erasure_list)
        ##then, we make a string win_text to tell user they lost
        loss_text = "Whoops! Looks like you lost this round of Solitaire Pool!"

        ##we then create the text
        makeText(win,loss_text,13,300,312)

        ##create string telling user to click to exit
        exit_click = "Click anywhere to exit."

        ##create the text
        makeText(win,exit_click,13,300,288)

        ##get mouse click and close window
        win.getMouse()
        win.close()


        

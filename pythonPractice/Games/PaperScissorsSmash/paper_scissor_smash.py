#Daniel Kolodziej
#4/25/18
#ITMD 413 Final Project
import os
import random
import time
import math
from tkinter import messagebox
import turtle
import pygame

#vars to store sound/music
file = 'zap.wav'
file2 = 'paperRip.wav'
file3 = 'gameMusic.mp3'

#play pregame music with pygame
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file3)
pygame.mixer.music.play()


#Change the window size
turtle.setup(750, 750)
turtle.fd(0) #just in case for MacOSX
#Set the animations speed to the maximum
turtle.speed(0)
#Change the background color
turtle.bgcolor("black")
#Change the window title
turtle.title("Paper, Scissors, Smash!")
#Change the background image to starting splash screen
turtle.bgpic("my-splash-screen.gif")
#Hide the default turtle
turtle.ht()
#This saves memory
turtle.setundobuffer(1)
#This speeds up drawing
turtle.tracer(0)

#Register sprite shapes
turtle.register_shape("transparent_paper.gif")
turtle.register_shape("transparent_stone.gif")
turtle.register_shape("transparent_scissors.gif")
turtle.register_shape("transparent_scissors45.gif")
turtle.register_shape("transparent_scissors90.gif")
turtle.register_shape("transparent_scissors135.gif")
turtle.register_shape("transparent_scissors180.gif")
turtle.register_shape("transparent_scissors225.gif")
turtle.register_shape("transparent_scissors270.gif")
turtle.register_shape("transparent_scissors315.gif")
    
#main parent class of game objects
class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1
        
    def move(self):
        self.fd(self.speed)
        
        #Boundary border detection to rotate and bounce off
        if self.xcor() > 280:
            self.setx(280)
            self.rt(60)
        
        if self.xcor() < -280:
            self.setx(-280)
            self.rt(60)
        
        if self.ycor() > 280:
            self.sety(280)
            self.rt(60)
        
        if self.ycor() < -280:
            self.sety(-280)
            self.rt(60)
    #method to check if a sprite has collided with another object        
    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False
#child class of Sprite                
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 2
        self.lives = 3
        self.headPosition = 90

    #methods for controls' actions
    def turn_left(self):
        self.lt(45)
        self.headPosition -= 45
        if self.headPosition < 0:
            self.headPosition = 360
        print(self.headPosition)
        
    def turn_right(self):
        self.rt(45)
        self.headPosition +=45
        if self.headPosition > 360:
            self.headPosition = 0
        print(self.headPosition)

    def accelerate(self):
        self.speed += 1
        
    def decelerate(self):
        self.speed -= 1

    #'''
    #override move method to changer for player class
    def move(self):
        self.fd(self.speed)
        
        #Boundary border detection to rotate and bounce off
        if self.xcor() > 280:
            self.setx(280)
            self.rt(45)
            self.headPosition += 45
            if self.headPosition > 360:
                self.headPosition = 0
            print(self.headPosition)
        
        if self.xcor() < -280:
            self.setx(-280)
            self.rt(45)
            self.headPosition += 45
            if self.headPosition > 360:
                self.headPosition = 0
            print(self.headPosition)
        
        if self.ycor() > 280:
            self.sety(280)
            self.rt(45)
            self.headPosition += 45
            if self.headPosition > 360:
                self.headPosition = 0
            print(self.headPosition)
        
        if self.ycor() < -280:
            self.sety(-280)
            self.rt(45)
            self.headPosition += 45
            if self.headPosition > 360:
                self.headPosition = 0
            print(self.headPosition)
    #'''

#child class of Sprite class      
class Paper(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 5   #speed at which object will move
        self.setheading(random.randint(0,360)) #to move in diff direction

#child class of Sprite class        
class Rock(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 7
        self.setheading(random.randint(0,360))

#override move method to changer for rock class
    def move(self):
        self.fd(self.speed)
        
        #Boundary border detection
        if self.xcor() > 280:
            self.setx(280)
            self.lt(60)
        
        if self.xcor() < -280:
            self.setx(-280)
            self.lt(60)
        
        if self.ycor() > 280:
            self.sety(280)
            self.lt(60)
        
        if self.ycor() < -280:
            self.sety(-280)
            self.lt(60)

#child class of Sprite class
class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000,-1000)
        self.frame = 0

    #starting position for particles to form   
    def explode(self, startx, starty):
        self.goto(startx,starty)
        self.setheading(random.randint(0,360))
        self.frame = 1
    #particles move to simulate explosion
    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1

        if self.frame > 15:
            self.frame = 0
            self.goto(-1000, -1000)

#game class for game state rules
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "splash"
        self.pen = turtle.Turtle()
        self.lives = 3
        self.count = 0
        
    def draw_border(self):
        #Draw Border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.ht()
        self.pen.penup()
        
    def show_status(self):
        self.pen.undo()
        #displays top message according to amount of player lives
        if game.lives > 0:
            msg = "Level: %s Lives: %s Score: %s " %(self.level, self.lives, self.score)        
        else: 
            msg = "Game Over Score: %s" %(self.score)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.write(msg, font=("Arial", 16, "normal"))

    #displays initial splash art screen, waits 5 seconds and changes game state
    def show_splash(self):
        turtle.bgpic("my-splash-screen.gif")
        turtle.update()
        time.sleep(6)
        turtle.bgpic("newbackground.gif")
        self.state = "setup"    
        
    def set_state(self, state):
        states = ["splash", "setup", "playing", "restart", "gameover"]
        if state in states:
            self.state = state
        else:
            state = "splash"

#Create game object
game = Game()

#Draw the game border
game.draw_border()

#Show the game status
game.show_status()


if game.state == "splash":
    game.show_splash()

if game.state == "setup":
    #Create my sprites
    player = Player("transparent_scissors90.gif", "white", 0, 0) #registered shape
    
    #Keyboard bindings to methods
    turtle.onkey(player.turn_left, "Left")
    turtle.onkey(player.turn_right, "Right")
    turtle.onkey(player.accelerate, "Up")
    turtle.onkey(player.decelerate, "Down")
    turtle.listen()
    #papers sprite list to populate with paper objects
    papers =[]
    for i in range(4):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        papers.append(Paper("transparent_paper.gif", "red", x, y))

    #rocks sprite list to populate with rock objects
    rocks =[]
    for i in range(3):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        rocks.append(Rock("transparent_stone.gif", "blue", x, y))
    #particles sprite list to populate with particle object
    particles = []
    for i in range(20):
        particles.append(Particle("circle", "gray", 0, 0))

    game.state = "playing"

#Main game loop
while True:
    #reset trackers when game restarts
    if game.state == "restart":
        game.lives = 3
        game.score = 0
        player.speed = 0
        player.goto(0,0)
        player.setheading(0)
        game.count = 0
        player.headPosition = 90
        game.show_status()

        #spawn sprites in random location
        for paper in papers:
            paper.goto(random.randint(-200, 200), random.randint(-200, 200))

        for rock in rocks:
            rock.goto(random.randint(-200, 200), random.randint(-200, 200)) 
            
        game.state = "playing"
        

    if game.state == "playing":
        turtle.update()
        time.sleep(0.02)
        #allows player to move with set key bindings
        player.move()
        if player.headPosition == 90:
            player.shape("transparent_scissors90.gif")
        elif player.headPosition == 45:
            player.shape("transparent_scissors45.gif")
        elif player.headPosition == 135:
            player.shape("transparent_scissors135.gif")
        elif player.headPosition == 225:
            player.shape("transparent_scissors225.gif")
        elif player.headPosition == 315:
            player.shape("transparent_scissors315.gif")
        elif player.headPosition == 180:
            player.shape("transparent_scissors180.gif")
        elif player.headPosition == 270:
            player.shape("transparent_scissors270.gif")
        elif player.headPosition == 360:
            player.shape("transparent_scissors.gif")
        elif player.headPosition == 0:
            player.shape("transparent_scissors.gif")
        elif player.headPosition < 0:
            player.headPosition == 360
        elif player.headPosition > 360:
            player.headPosition == 0

        #makes all paper sprite move on own
        for paper in papers:
            paper.move()
            
            #Check for a collision with the player
            if player.is_collision(paper):
                #Play rip sound with pygame
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(file2)
                pygame.mixer.music.play()
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                paper.goto(x, y)
                game.score += 100
                game.count += 1
                #tracks "kills" in order to add bonus lives
                if game.count == 3:
                    game.lives += 1
                    game.count = 0
                game.show_status()
                
        #makes all rock sprite move on own   
        for rock in rocks:
            rock.move()

            #Check for a collision between the missile and the ally
            if player.is_collision(rock):
                #Play explosion sound with pygame
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                for particle in particles:
                    particle.explode(rock.xcor(), rock.ycor())
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                rock.goto(x, y)
                #Decrease the score
                game.score -= 50
                game.count -= 1
                #reset bonus lives count if wrong crash
                if game.count < 0:
                    game.count = 0
                game.lives -= 1
                if game.lives < 1:
                    game.state = "gameover"
                game.show_status()

    #makes all particle sprites move on own
    for particle in particles:
        particle.move()
    #checks if game state is gameoever in which player is given option to play again
    if game.state == "gameover":
        for i in range(360):
            player.rt(1) 
            
        if messagebox.askyesno("Game Over", "Play again?") == True:
            game.state = "restart"
        else:
            exit()

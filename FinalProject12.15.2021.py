#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 07:32:19 2021
@author: rachelwildeson

This animation builds an image of a sunset. Upon starting the code the song
begins and the different beams of sunlight filter through different colors randomly,
providing a different image each time the code loops. 

Please press the start button to run this code and begin the animation.

My inspiration was this gif image I found online. I wanted to create something 
relaxing in the spirit of finals season. Here is the link to the gif:
    https://www.shutterstock.com/video/clip-1066112242-retro-hippie-background-sun-rays-shining-stars

The song is "Never Give Up" by an artist called Ketsa. I found this song here:
    https://freemusicarchive.org/music/Ketsa
This song has a creative commons license. 

"""
# ================ IMPORT LIBRARIES ==========================

import turtle 
import random
import time 
import pygame

# colors // legal OOP per matchOOP in Class Code 
halfSunColors = [ (255, 127,81), (255, 141, 83), (255,155,84), (237, 211, 130), (245, 185, 105) ] #coral, mango tango, sandy brown, buff, sunray
innerSideBeamColors = [(255, 164, 126), (255, 153, 135), (242, 122, 92), (242, 112, 89), (242, 92, 84)] #light salmon, vivid tangerine, burnt sienna, bittersweet, fire opal
outerSideBeamColors = [(247, 178, 103), (247, 157, 101), (255, 141, 143), (254, 120, 53), (245, 125, 118) ] #mellow apricot, atomic tangerine, light coral, orange crayola, congo pink
middleBeamColors = [(250, 179, 85), (242, 243, 174), (237, 211, 130), (245, 185, 105), (249, 160, 63)] #yellow orange, pale spring bud, buff, sunray, deep saffron
triangleBeamColors = [(242, 112, 89), (242, 92, 84), (242, 122, 92), (255, 164, 126), (246, 124, 104)] #bittersweet, fire opal, burtn sienna, light salmon, salmon

# ==================== CLASSES ===============================
#HALF SUN
class halfSun(turtle.Turtle):
    def __init__(self, x=150, y = -200, color = random.choice(halfSunColors)):
        super().__init__()
        self.panel = turtle.Screen()
        self.halfSunDraw(x,y)
        self.halfSunChangeColor(x,y)
        self.color(color)
        
    def halfSunDraw(self, x =150, y=-200):
        ''' Draws half sun shape. '''
        self.up()
        self.goto(x,y)
        self.down()
        self.fillcolor(random.choice(halfSunColors))
        self.begin_fill()
        self.right(90)
        self.circle(-150,-180)
        self.right(90)
        self.forward(300)
        self.end_fill()
        self.hideturtle()
        self.panel.update()
        self.halfSunChangeColor(x,y)
        
    def halfSunChangeColor(self, x=150,y=-200):
        ''' Draws new half sun shape with different fill color. '''
        for i in halfSunColors:
            turtle.tracer(0)
            self.up()
            self.goto(x,y)
            self.down()
            self.fillcolor(random.choice(halfSunColors))
            self.begin_fill()
            self.right(90)
            self.circle(-150, -180)
            self.right(90)
            self.forward(300)
            self.end_fill()
            self.hideturtle()
            time.sleep(0.1)
            self.panel.update()
        
#RECTANGLE        
class Rectangle(turtle.Turtle):
    def __init__(self, x=-300, y=-200, color = random.choice(halfSunColors)):  
        super().__init__()
        self.panel = turtle.Screen()
        self.rectangleDraw(x,y)
        self.rectChangeColors(x,y)
        self.color(color)

    def rectangleDraw(self, x=-300, y=-200):
        ''' Draws rectangle border shape. '''
        self.up()
        self.goto(x,y)
        self.down()
        self.fillcolor(random.choice(halfSunColors))
        self.begin_fill()
        for i in range(2): 
            self.forward(600)
            self.right(-90)
            self.forward(400)
            self.right(-90)
        self.end_fill()
        self.hideturtle()
        self.panel.update()
        self.rectChangeColors(x,y)
 
    def rectChangeColors(self, x=-300,y=-200):
        ''' Draws new rectangle shape with different fill color. '''
        for i in halfSunColors:
            turtle.tracer(0)
            self.up()
            self.goto(x,y)
            self.down()
            self.fillcolor(random.choice(halfSunColors))
            self.begin_fill()
            for i in range(2): 
                self.forward(600)
                self.right(-90)
                self.forward(400)
                self.right(-90)
            self.end_fill()
            self.hideturtle()
            time.sleep(0.1)
            self.panel.update()

# INNER SIDE BEAMS
class SideBeam(turtle.Turtle):
    def __init__(self, x=-0, y = -198, color = random.choice(innerSideBeamColors)):
        super().__init__()
        self.panel = turtle.Screen()
        self.sideBeamDraw(x,y)
        self.sideBeamChangeColors(x,y)
        self.color(color)
        
    def sideBeamDraw(self, x =0, y=-198):
        ''' Draws side beam shape. '''
        self.up()
        self.goto(x,y)
        self.down()
        self.fillcolor(random.choice(innerSideBeamColors))
        self.begin_fill()
        self.right(-55)
        self.forward(486)
        self.right(55)
        self.forward(-173)
        self.right(105)
        self.forward(414)
        self.right(-105)
        self.end_fill()
        self.hideturtle()
        self.panel.update()
        self.sideBeamChangeColors(x,y) 
    
    def sideBeamChangeColors(self, x =0 ,y=-198):
        ''' Draws new side beam shape with different fill color. '''
        for i in innerSideBeamColors:
            turtle.tracer(0)
            self.up()
            self.goto(x,y)
            self.down()
            self.fillcolor(random.choice(innerSideBeamColors))
            self.begin_fill()
            for i in range(1):
                self.right(-55)
                self.forward(486)
                self.right(55)
                self.forward(-173)
                self.right(105)
                self.forward(414)
                self.right(-105)
            self.end_fill()
            self.hideturtle()
            time.sleep(0.1)
            self.panel.update()

# Idea for how to use inheritence to mirror side beams from Youtube video linked below. 
# Here, I create new methods that take commands from the Parent class and 'flip' them 
# so that the directions are able to mirror the image. The 'change' piece is like a 
# pass function that will take whatever direction is above, for example "forward 486
# and send that through my method to mean left 486. I decided to pass the phrase 'change'
# through as it seemed intuitive to what the method would be doing to that value. 
# https://www.youtube.com/watch?v=gbC3X8GUnUk&t=256s&ab_channel=KentD.Lee
class SideBeamOpposite(SideBeam):
    def __init__(self, x=0, y=-198, color = random.choice(innerSideBeamColors)):
        super().__init__(x=0,y=-198, color = random.choice(innerSideBeamColors))
        
    def right(self,change):
        super().left(change)
        
    def forward(self,change):
        super().backward(change)

# OUTER SIDE BEAMS
class OuterSideBeam(turtle.Turtle):
    def __init__(self, x=-0, y = -198, color = random.choice(outerSideBeamColors)):
        super().__init__()
        self.panel = turtle.Screen()
        self.outerSideBeamDraw(x,y)
        self.outerSideBeamChangeColors(x,y)
        self.color(color)
        
    def outerSideBeamDraw(self, x =0, y=-198):
        ''' Draws outer beam shape. '''
        self.up()
        self.goto(x,y)
        self.down()
        self.fillcolor(random.choice(outerSideBeamColors))
        self.begin_fill()
        self.right(-33)
        self.forward(358)
        self.right(123)
        self.forward(-203)
        self.right(90)
        self.forward(21)
        self.right(-55)
        self.forward(488)
        self.right(-125)
        self.end_fill()
        self.hideturtle()
        
        self.end_fill()
        self.hideturtle()
        self.panel.update()
        self.outerSideBeamChangeColors(x,y) 
    
    def outerSideBeamChangeColors(self, x =0 ,y=-198):
        ''' Draws new outer beam shape with different fill color. '''
        for i in outerSideBeamColors:
            turtle.tracer(0)
            self.up()
            self.goto(x,y)
            self.down()
            self.fillcolor(random.choice(outerSideBeamColors))
            self.begin_fill()
            self.right(-33)
            self.forward(358)
            self.right(123)
            self.forward(-203)
            self.right(90)
            self.forward(21)
            self.right(-55)
            self.forward(488)
            self.right(-125)
            self.end_fill()
            self.hideturtle()
            self.end_fill()
            self.hideturtle()
            time.sleep(0.1)
            self.panel.update()

class OuterSideBeamOpposite(OuterSideBeam):
    def __init__(self, x=0, y=-198, color = random.choice(outerSideBeamColors)):
        super().__init__(x=0,y=-198, color = random.choice(outerSideBeamColors))
        
    def right(self,change):
        super().left(change)
        
    def forward(self,change):
        super().backward(change)

# MIDDLE BEAM
class MiddleBeam(turtle.Turtle):
    def __init__(self, x=0, y=-200, color = random.choice(middleBeamColors)):
        super().__init__()
        
        self.panel = turtle.Screen()
        self.middleBeamDraw(x,y)
        self.middleBeamChangeColors(x,y)
        self.color(color)

    def middleBeamDraw(self, x=0, y=-200):
        ''' Draws middle beam shape. '''
        self.up()
        self.goto(x,y)
        self.down()
        self.fillcolor(random.choice(middleBeamColors))
        self.begin_fill()
        self.right(-75)
        self.forward(414)
        self.right(-105)
        self.forward(215)
        self.right(-105)
        self.forward(414)
        self.right(-75)
        self.end_fill()
        self.hideturtle()
        self.panel.update()
        self.middleBeamChangeColors(x,y)
 
    def middleBeamChangeColors(self, x=0,y=-200):
        ''' Draws new middle beam shape with different fill color. '''
        for i in middleBeamColors:
            turtle.tracer(0)
            self.up()
            self.goto(x,y)
            self.down()
            self.fillcolor(random.choice(middleBeamColors))
            self.begin_fill()
            self.right(-75)
            self.forward(414)
            self.right(-105)
            self.forward(215)
            self.right(-105)
            self.forward(414)
            self.right(-75)
            self.end_fill()
            self.hideturtle()
            time.sleep(0.1)
            self.panel.update()
        
# TRIANGLE BEAMS 
class TriangleBeam(turtle.Turtle):
    def __init__(self, x=0, y=-200, color = random.choice(triangleBeamColors)):
        super().__init__()
        
        self.panel = turtle.Screen()
        self.triangleBeamDraw(x,y)
        self.triangleChangeColors(x,y)
        self.color(color)

    def triangleBeamDraw(self, x=0, y=-200):
        ''' Draws triangle beam shape. '''
        self.up()
        self.goto(x,y)
        self.down()
        self.fillcolor(random.choice(triangleBeamColors))
        self.begin_fill()
        self.right(-180)
        self.forward(300)
        self.right(90)
        self.forward(195)
        self.right(123)
        self.forward(358)
        self.right(-33)
        self.end_fill()
        self.hideturtle()
        self.panel.update()
        self.triangleChangeColors(x,y)
 
    def triangleChangeColors(self, x=0,y=-200):
        ''' Draws new triangle beam shape with different fill color. '''
        for i in triangleBeamColors:
            turtle.tracer(0)
            self.up()
            self.goto(x,y)
            self.down()
            self.fillcolor(random.choice(triangleBeamColors))
            self.begin_fill()
            self.right(-180)
            self.forward(300)
            self.right(90)
            self.forward(195)
            self.right(123)
            self.forward(358)
            self.right(-33)
            self.end_fill()
            self.hideturtle()
            time.sleep(0.1)
            self.panel.update()

class TriangleBeamOpposite(TriangleBeam):
    def __init__(self, x=0, y=-200, color = random.choice(triangleBeamColors)):
        super().__init__(x=0,y=-200, color = random.choice(triangleBeamColors))
        
    def right(self,change):
        super().left(change)
        
    def forward(self,change):
        super().backward(change)

# ============== ANIMATION CLASS MANAGER =====================

class animationManager():
    def __init__(self):
        self.panel = turtle.Screen()
        self.running = True
        self.setup()
  
    def setup(self):
        turtle.colormode(255)
        turtle.tracer(0)
        self.panel = turtle.Screen()
        w = 1200
        h = 1200
        self.panel.setup(width=w,height=h)
        self.panel.bgcolor(42, 157, 143)
        
        # Use of sound modified from pySound.py in Class Code
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        global bgMusic
        bgMusic = pygame.mixer.music.load('NeverGiveUp.wav')
        
        self.run()
        
    def run(self):
        pygame.mixer.music.play(0)
        rectangle = Rectangle(-300,-200)
        leftTriangle = TriangleBeam(0,-200)
        outerRightSideBeam = OuterSideBeamOpposite(0,-198)
        leftSideBeam = SideBeamOpposite(0,-198)
        middleBeam = MiddleBeam(0,-200)
        rightSideBeam = SideBeam(0,-198)
        outerLeftSideBeam = OuterSideBeam(0,-198)
        rightTriangle = TriangleBeamOpposite(0,-200)
        halfSunOne = halfSun(150,-200) 

        while self.running: 
            rectangle.rectChangeColors()
            leftTriangle.triangleChangeColors()
            outerRightSideBeam.outerSideBeamChangeColors()
            leftSideBeam.sideBeamChangeColors()
            middleBeam.middleBeamChangeColors()
            rightSideBeam.sideBeamChangeColors()
            outerLeftSideBeam.outerSideBeamChangeColors()
            rightTriangle.triangleChangeColors()
            halfSunOne.halfSunChangeColor() 

                                   
# ================= START ANIMATION =========================

if __name__=='__main__':
    animationManager()
    
# ====================== SETUP ===============================

turtle.mainloop()
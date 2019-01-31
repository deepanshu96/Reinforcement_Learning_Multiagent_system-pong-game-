from numpy import random
import pygame, sys
from pygame.locals import *
import pygame.surfarray as sarray
import numpy as np

white = (255,255,255)
black = (0,0,0)

window_width = 400
window_height = 400

paddle_width = 10
paddle_height = 60
paddle_buffer = 10 

ball_width = 10
ball_height = 10

paddle_speed = 2
ball_x_speed = 3
ball_y_speed = 2

screen = pygame.display.set_mode((window_width, window_height))

# Possible actions -1,0,1

class PongObject :
    def __init__(self, pos):
        self.pos = pos
        self.action = [0,1,0]
        self.score = 0
    def update_paddle(self, act):
        self.act = act
        sum = 0
        for i in range(0,3):
            if(self.act[i]==1):
                sum = i-1
                break
            
        self.pos[1] = self.pos[1] + sum*paddle_speed
        if(self.pos[1] < 0):
            self.pos[1] = 0
        if(self.pos[1] > window_height - paddle_height):
            self.pos[1] = window_height - paddle_height
        
class PongBall():
    def __init__(self, pos):
        self.pos = pos
        num = np.random.randint(1, 10)
        self.xdir = np.random.randint(-1, 2)
        self.ydir = np.random.randint(-1, 2)
        if(0 < num < 3):
            self.xdir = 1
            self.ydir = 1
        if (3 <= num < 5):
            self.xdir = -1
            self.ydir = 1
        if (5 <= num < 8):
            self.xdir = 1
            self.ydir = -1
        if (8 <= num < 10):
            self.xdir = -1
            self.ydir = -1
        
    def rest(self):
        num = np.random.randint(1, 10)
        self.xdir = np.random.randint(-1, 2)
        self.ydir = np.random.randint(-1, 2)
        if(0 < num < 3):
            self.xdir = 1
            self.ydir = 1
        if (3 <= num < 5):
            self.xdir = -1
            self.ydir = 1
        if (5 <= num < 8):
            self.xdir = 1
            self.ydir = -1
        if (8 <= num < 10):
            self.xdir = -1
            self.ydir = -1
    #def update_ball():
        #None
class PongGame():
    #metadata = {'render.modes' : ['human', 'rgb_array']}    
    #Rect(left, top, width, height)
    def __init__(self):
        self.paddle1 = PongObject([paddle_buffer, window_height/2 - paddle_height/2])
        self.paddle2 = PongObject([window_width-paddle_buffer-paddle_width, window_height/2 - paddle_height/2])
        self.ball  = PongBall([window_width/2 - ball_width/2, window_height/2 + ball_height/2])

    def reset_(self):
        self.paddle1 = PongObject([paddle_buffer, window_height/2 - paddle_height/2])
        self.paddle2 = PongObject([window_width-paddle_buffer-paddle_width, window_height/2 - paddle_height/2])
        self.ball  = PongBall([window_width/2 - ball_width/2, window_height/2 + ball_height/2])
        self.ball.rest()
        self.step_([0,1,0], [0,1,0])
        
    def step_(self, act1, act2):

        self.paddle1.update_paddle(act1)
        self.paddle2.update_paddle(act2)

        pad1Ypos = self.paddle1.pos[1]
        pad2Ypos = self.paddle2.pos[1]
        
        #Update Ball
        ballXpos = self.ball.pos[0]
        ballYpos = self.ball.pos[1]

        ballXpos = ballXpos + self.ball.xdir * ball_x_speed
        ballYpos = ballYpos + self.ball.ydir * ball_y_speed

        #agent1
        if( ballXpos <= paddle_buffer + paddle_width and
            ballYpos + ball_height >= pad1Ypos and ballYpos - ball_height<= pad1Ypos + paddle_height):
            self.ball.xdir = 1
            self.paddle1.score+=1
            self.paddle2.score+=1
            #ballXpos = paddle_buffer + paddle_width

        elif(ballXpos <= 0):
            self.ball.xdir = 1
            self.paddle1.score-=1
            self.paddle2.score-=1

        #agent2
        if(ballXpos >= window_width - paddle_width - paddle_buffer and
           ballYpos + ball_height>=pad2Ypos and ballYpos - ball_height <= pad2Ypos + paddle_height):
            self.ball.xdir = -1
            self.paddle1.score+=1
            self.paddle2.score+=1
            #ballXpos = window_width - paddle_width - paddle_buffer - ball_width

        elif(ballXpos > window_width - ball_width):
            self.ball.xdir = -1
            self.paddle1.score-=1
            self.paddle2.score-=1

        #ball hits top
        if(ballYpos <=0):
            ballYpos = 0
            self.ball.ydir = 1
        #ball hits the bottom
        if(ballYpos >= window_height - ball_height):
            ballYpos = window_height - ball_height
            self.ball.ydir = -1

        self.ball.pos[0] = ballXpos
        self.ball.pos[1] = ballYpos

        screen2 = self.getFrame()
                 
        return [screen2, self.paddle1.score, self.paddle2.score]
    

    def getFrame(self):
        pygame.event.pump()
        screen.fill(black)

        #draw paddle
        p1 = pygame.Rect(self.paddle1.pos[0], self.paddle1.pos[1],paddle_width, paddle_height)
        pygame.draw.rect(screen, white, p1)
        p2 = pygame.Rect(self.paddle2.pos[0], self.paddle2.pos[1], paddle_width, paddle_height)
        pygame.draw.rect(screen, white, p2)

        #draw ball
        bll = pygame.Rect(self.ball.pos[0], self.ball.pos[1], ball_width, ball_height)
        pygame.draw.rect(screen, white, bll)

        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        pygame.display.flip()
        return image_data
'''
a = PongGame()
i = 0
temp = a.reset_()
for i in range(10000):
    act1 = [0,0,0]
    act2 = [0,0,0]
    j = np.random.randint(-1,2)
    act1[j] = 1
    j = np.random.randint(-1,2)
    act2[j] = 1
    temp = a.step_(act1, act2)
    #print(a.paddle1.score," ",a.paddle2.score) 
'''



        
        
        
                
        

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 06:31:38 2018

@author: john
"""

#Two-player zero-sum soccer env. for testing multi-agent learning algorithms. 
#Taken from - "Markov games as a framework for multi-agent reinforcement learning" 
#Littman 1994. 

import random
import numpy as np
from time import sleep


#ACTIONS 
left=-1 #1
right=1 #2
up=-4 #3
down=4 #4
stick=0 #0


class player(object):
    def __init__(self):   
        self.pos=0
        self.has_ball=False
              
    #boundary checking for field moves here
    def set_pos(self, pos):
        if pos>7 or pos<0:
            return
        #edge case check - moving from top right to bottom left and vice versa
        elif self.pos==3 and pos==4:
            return
        elif self.pos==4 and pos==3:
            return
        else:
            self.pos=pos
      
class soccer_env(object):
    def __init__(self):   
        self.a=player()
        self.b=player()
        self.reset_env()
        self.state=self.get_state()
        self.total_states=200
        self.total_actions=5
   
    def reset_env(self):
        self.a.set_pos(2)
        self.b.set_pos(1)
        self.a.has_ball=False
        self.b.has_ball=True
        self.state=self.get_state()
        return self.state
        
    def get_state(self):
        poss=self.b.has_ball*100
        a_pos=self.a.pos*10
        b_pos=self.b.pos
        state=poss+a_pos+b_pos
        return state  
    
    #method set_ball to ensure only one player has the ball
    def set_ball(self, player):
        if player==self.a:
            self.a.has_ball=True
            self.b.has_ball=False
        else:
            self.a.has_ball=False
            self.b.has_ball=True
       
    #0 stick
    #1 left
    #2 right
    #3 up
    #4 down
    def get_action(self, action):
        if action==0:
            action=stick
        if action==1:
            action=left
        if action==2:
            action=right
        if action==3:
            action=up
        if action==4:
            action==down
        return action
    
    #move player 
    def move(self, a_action, b_action):
        
        #convert actions to env action values
        a_action=self.get_action(a_action)
        b_action=self.get_action(b_action)
              
        #flip a coin to see who moves first
        a_first=False
        if np.random.random()>=.5:
            a_first=True

        #save old positions and set new positions
        a_pos=self.a.pos
        b_pos=self.b.pos
        #print "old positions a, b=", a_pos, b_pos
        self.a.set_pos(self.a.pos+a_action)
        self.b.set_pos(self.b.pos+b_action)
        
        #edge case, check for first mover to move to second mover current spot
        if a_first:
            if self.a.pos==b_pos:
                self.a.pos=a_pos
                self.b.pos=b_pos
                self.set_ball(self.b)
        else:
            if self.b.pos==a_pos:
                self.b.pos=b_pos
                self.a.pos=a_pos
                self.set_ball(self.a)
        
        #if players collide change possession if needed
        #and reset second player position
        if self.a.pos==self.b.pos:     
            #print "collide"
            if a_first:
                #print "a first - reset b.pos to", b_pos
                self.b.pos=b_pos
                #player without ball cannot steal by moving into player with ball
                #if b move is not stick, change possession (if needed)
                if not b_action==0:
                    self.set_ball(self.a)
                #extra check/edge case 
                if self.a.pos==self.b.pos: 
                    self.a.pos=a_pos
            else:
                #print "b first - reset a.pos to", a_pos
                self.a.pos=a_pos
                #player without ball cannot steal by moving into player with ball
                #if a move is not stick, change possession (if needed)
                if not a_action==0:
                    self.set_ball(self.b)   
                #extra check/edge case
                if self.a.pos==self.b.pos: 
                    self.b.pos=b_pos
        
        new_state=self.get_state()
        
        #set reward and done
        #reward assumes player a (negate for player b)
        done=False
        reward=0.
        if self.b.has_ball: 
            #if b has ball and pos = 3 or 7, done=True and Reward = 100
            if self.b.pos==3 or self.b.pos==7:
                done=True
                reward=-100.
            #if b has ball and pos = 0 or 4, done=True and Reward = -100 
            elif self.b.pos==0 or self.b.pos==4:
                done=True
                reward=100.
        elif self.a.has_ball:
            #if a has ball and pos = 3 or 7, done=True and Reward = -100
            if self.a.pos==3 or self.a.pos==7:
                done=True
                reward=-100.
            #if a has ball and pos = 0 or 4, done=True and Reward = 100
            elif self.a.pos==0 or self.a.pos==4:
                done=True
                reward=100.
                
        info=None   
        self.state=new_state
        return (new_state, reward, done, info)
    
    #render env. 
    def render(self):
        column1=[] 
        column2=[]
        for i in range(0,4):
            if self.a.pos==i:
                column1.append('a')
            elif self.b.pos==i:
                column1.append('b')
            else:
                column1.append('#')

        for i in range(4,8):
            if self.a.pos==i:
                column2.append('a')
            elif self.b.pos==i:
                column2.append('b')
            else:
                column2.append('#')
                
        #print char1,char2,char3,char4
        print(column1)
        print(column2)
        
        #print self.a.pos, self.b.pos
        if self.a.has_ball:
            print("a has ball")
        else:
            print("b has ball")

if __name__=="__main__":
    soccer=soccer_env()
    iters=1
    a_rewards=np.zeros([iters])
    b_rewards=np.zeros([iters])
    
    for i in range(0, iters):
        done=False
        
        soccer.reset_env()
        soccer.render()
        while not done:
            #sleep(0.6) # Time in seconds.
            a_action = np.random.randint(5)
            b_action = np.random.randint(5)
            new_state, reward, done, info = soccer.move(a_action, b_action)
            print("a action, b action", a_action, b_action)
            soccer.render()
            
        a_rewards[i]=reward
        b_rewards[i]=-reward
    print("player a reward=", reward)
    print("player b reward=", -reward)
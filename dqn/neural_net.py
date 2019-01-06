#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:03:18 2019

@author: john
"""
import numpy as np
import random
import gym
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from keras.optimizers import Adam, RMSprop

#from pseudocode - deep q learning with experience replay
#https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf
#https://arxiv.org/pdf/1312.5602.pdf

class neural_net(object):
    def __init__(self, env_params):
        self.env = gym.make(env_params['env_name'])     
        self.total_states = self.env.observation_space.shape[0]
        self.total_actions = self.env.action_space.n
        self.memory=deque(maxlen=50000)
        
        #hyperparameters
        self.lr=env_params['lr'] #nn lr
        self.gamma=env_params['gamma']
        self.explore=env_params['explore'] #egreedy exploration
        self.decay=env_params['decay'] #exploration decay
        self.min_explore=env_params['min_explore'] #min explore
        self.episodes=env_params['episodes'] #number episodes
        self.batch_size=env_params['batch_size'] #batch size (for experience replay)
        self.minimum_samples=env_params['minimum_samples'] #number of samples needed before training
        self.gamma_exp = env_params['gamma_exp']
        self.gamma_max = env_params['gamma_max']     
       
        #nn
        self.model = Sequential()
        self.model.add(Dense(env_params['layer1_size'], input_dim=self.total_states, activation='relu'))
        self.model.add(Dense(env_params['layer2_size'], activation='relu'))
        self.model.add(Dense(self.total_actions, activation='linear'))
        self.model.compile(loss='mse', optimizer=Adam(lr=self.lr))
        #self.model.compile(loss='mse', optimizer=RMSprop(lr=self.lr, rho=0.95, epsilon=0.01))
        self.model_name=env_params['model_name']
        
        self.finalScores = np.zeros([self.episodes])
        
    def load_model(self):
        print "loading model ", self.model_name
        self.model=load_model(self.model_name)

    def save_model(self):
        self.model.save(self.model_name)
        
    #egreedy (training)
    def select_action(self, state):
        if self.explore < self.min_explore:
            self.explore=self.min_explore
        values = self.model.predict(state.reshape(1, self.total_states))[0]
        if np.random.rand() <= self.explore:
            action = np.random.randint(len(values))
        else:
            action = np.argmax(values)
        return action
        
    #greedy (testing)
    def select_action2(self, state):
        values = self.model.predict(state.reshape(1, self.total_states))[0]
        action = np.argmax(values)
        return action
    
    def train_model(self):
    
        for episode in range(self.episodes):
            state = self.env.reset() #initialize sequence 
            state = np.reshape(state, [1, self.total_states])
            totalReward = 0 #episode total reward
            done=False
            #decay exploration
            self.explore=self.explore*self.decay
            self.gamma=self.gamma*self.gamma_exp
            if self.gamma>self.gamma_max:
                self.gamma=self.gamma_max
           
            while not done:    
                
                #select with proability e random action a_t (egreedy action selection)
                action = self.select_action(state)
                
                #execute action in emulator and observe reward
                #openai gym env.step Returns observation, reward, done, info.
                observation, reward, done, info = self.env.step(action)
                #reshape observation for keras predict
                observation = np.reshape(observation, [1, self.total_states])
                #add to memory for batch sampling
                self.memory.append((state, action, reward, observation, done))
                state = observation #change current state
                totalReward=totalReward+reward #add reward to total episode reward
                
            print "episode, explore, gamma, totalReward=", episode, self.explore, self.gamma, totalReward
            self.finalScores[episode]=totalReward
            
            #memory replay/nn training once per episode
            #build up min_samples before training
            if len(self.memory) > self.minimum_samples:  
                #experience replay
                self.experience_replay()
        
        self.save_model()        
        return self.finalScores
    
    def experience_replay(self):
        #experience replay
        #sample random minibatch of transitions from memory (D)
        batch = random.sample(self.memory, self.batch_size)
        for state, action, reward, s_prime, done in batch:
            if done:
                value = reward
            else:
                value = reward + self.gamma * np.max(self.model.predict(s_prime)[0])
            new_value = self.model.predict(state) #current estimated value of Q(s,a)
            new_value[0][action] = value #new value of Q(s,a)
            #peform gradient descent using current prediction/new value
            self.model.fit(state, new_value, verbose=0)
        
    def test_model(self):
        episodes=100
        totalSumReward=0 
        self.load_model()
        for i in range(0,episodes):
            state=self.env.reset()
            done=False
            totalReward = 0 #episode total reward
            
            while not done:
                self.env.render()
                action = self.select_action2(state)
                observation, reward, done, info = self.env.step(action)
                state=observation
                totalReward=totalReward+reward
                
            print "reward=", totalReward
            totalSumReward=totalSumReward+totalReward
            print totalSumReward, totalReward
        print "avg reward=", totalSumReward/episodes 
        print "num episodes=", episodes
        
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 19:11:03 2018

@author: john
"""

import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class dqnLearner(object):
    def __init__(self, env, mode):
        env_params= self.get_env_parameters(env)
        from neural_net import neural_net
        nn = neural_net(env_params)
        if mode=="train":
            nn.train_model()
            self.plot_scores()
        elif mode=="test":
            nn.test_model()
            self.plot_scores()
        else:
            print "invalid mode"
    
    #retrieve from json
    def get_env_parameters(self, env):
        if env=="CartPole-v0":
            with open('cartpole.json', 'r') as fp:
                env_params = json.load(fp)
            return env_params
        elif env=="Acrobot-v1":
            with open('acrobot.json', 'r') as fp:
                env_params = json.load(fp)
            return env_params
        else:
            return "defaults"
        
    def display_env_parameters(self, env):
        print env, self.get_env_parameters(env)
    
    def plot_scores(self):
        print "...print scores..."


if __name__=="__main__":
    
    dqnLearner = dqnLearner("Acrobot-v1", "test")
    #dqnLearner.display_env_parameters("CartPole-v0")
    

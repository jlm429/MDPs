### Markov Decision Process 

> From any state the agent can perform one of four actions, up, down, left or right, which have a stochastic effect. With probability 2/3, the actions cause the agent to move one cell in the corresponding direction, and with probability 1/3, the agent moves instead in one of the other three directions, each with probability 1/9. (Sutton, R.S. and Precup, D. and Singh, S., 1999).  The reward function sets the terminal state to zero (the grey circle at the top right) and all other state/action transitions to negative one.   
>
> Coding Resource <a href="https://github.com/jmacglashan/burlap">Brown-UMBC Reinforcement Learning and Planning (BURLAP) java code library</a>


### Value Iteration (<a href="https://github.com/jlm429/MDPs/blob/master/src/GridWorldVI.java">src/GridWorldVI.java</a>)
It took value iteration 20 iterations to converge on the grid world domain.   Below is a list of the rewards given after convergence with red values denoting higher negatives and blues closer to the terminating state 0.  

![Component Diagram](https://github.com/jlm429/MDPs/blob/master/images/ValueIterationRewards.PNG)

### Policy Iteration (<a href="https://github.com/jlm429/MDPs/blob/master/src/GridWorldPI.java">src/GridWorldPI.java</a>)

It took policy iteration 14 iterations to converge on the grid world domain.   Below is an image of the policies after convergence with reward values.  
![Component Diagram](https://github.com/jlm429/MDPs/blob/master/images/PolicyIterationGrid.PNG)


### Q-Learning (<a href="https://github.com/jlm429/MDPs/blob/master/src/GridWorldQL.java">src/GridWorldQL.java</a>)

The Q-Learning algorithm converges around 100 iterations on the grid world domain taking approximately 25 time steps to reach the termination state.   It takes longer to learn the environment but has more value in real world applications since it is a learning algorithm as opposed to a planning algorithm. Below is a graph that includes the time steps per iteration for Q-learning in the grid world domain with gamma=.99 and a learning rate of .9.   


![Component Diagram](https://github.com/jlm429/MDPs/blob/master/images/smallgridworldQLearning.png)


### Summary

Both value and policy iteration converge to the same answer.  Policy iteration often converges in fewer iterations than value iteration, as it did in this case, presumably because the value function changes little from one policy to the next (Sutton and Barto, 1988).  Greedy exploration strategies were faster and due to the simplicity of the grid world domain equally as effective.  A more exploratory Q-Learning algorithm might be helpful for more complex domains. Below are gamma values with complexity charts for Q-Learning. 


![Component Diagram](https://github.com/jlm429/MDPs/blob/master/images/LargeGridWorldQL.PNG)

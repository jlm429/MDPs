### Fun with MDPs
>
> Coding Resource <a href="https://github.com/jmacglashan/burlap">Brown-UMBC Reinforcement Learning and Planning (BURLAP) java code library</a>

### Policy Iteration (<a href="https://github.com/jlm429/MDPs/blob/master/src/GridWorldPI.java">src/GridWorldPI.java</a>)

Below is an image of the policy after convergence.  
![Component Diagram](https://github.com/jlm429/MDPs/blob/master/images/PolicyIterationGrid.PNG)


### Q-Learning (<a href="https://github.com/jlm429/MDPs/blob/master/src/GridWorldQL.java">src/GridWorldQL.java</a>)

The Q-Learning algorithm converges around 100 iterations on the grid world domain taking approximately 25 time steps to reach the termination state.   It learns directly from interacting with the environment rather than planning based on a model. Below is a graph that includes the time steps per iteration for Q-learning in the grid world domain with gamma=.99 and a learning rate of .9.   


![Component Diagram](https://github.com/jlm429/MDPs/blob/master/images/smallgridworldQLearning.png)


### Summary

Both value and policy iteration converge to the same answer. Greedy exploration strategies were faster and, due to the simplicity of the grid world domain, equally as effective. Below are gamma values with complexity charts for Q-Learning. 


![Component Diagram](https://github.com/jlm429/MDPs/blob/master/images/LargeGridWorldQL.PNG)

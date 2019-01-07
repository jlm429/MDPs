> ## Deep Q-Learning (<a href="https://github.com/jlm429/RL/blob/master/dqn/dqnLearner.py">dqnLearner.py</a>, <a href="https://github.com/jlm429/RL/blob/master/dqn/neural_net.py">neural_net.py</a>)  
> OpenAI domains (<a href="https://gym.openai.com/envs/CartPole-v0/">CartPole</a>, <a href="https://gym.openai.com/envs/Acrobot-v1/">Acrobot</a>)

Q-learning uses temporal differences to estimate state-action values and discretization or function approximation to evaluate the state.
Instead of using a Q-table, a neural network can be used to approximate q-values. Many function
approximators, such as neural nets and local weighted regression, can cause instability in reinforcement
learning by exaggerating the difference between target values (Gordon 1995). Deep Q-learning 
uses experience replay to help resolve this issue by randomizing samples.  The
behavior distribution is averaged over many previous states which breaks correlations and reduces the
variance of the updates (Minh et al. 2013). The concept of experience replay has roots in neuroscience
and the belief that time-compressed reactivation of recently experienced trajectories during offline periods
provide a mechanism for updating value functions (Minh et al. 2015). Representation learning with deep
learning enables automatic feature engineering and end-to-end learning through gradient descent, so that
reliance on domain knowledge is significantly reduced or even removed (Li 2017).  

>DQN pseudocode (from <a href="https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf"> DQN Nature Paper</a>)

![DQN pseudocode](https://github.com/jlm429/RL/blob/master/images/dqnpseudocode.PNG)

Complex domains such as lunar lander and mountain car require precise hyper-parameter tuning and more sophisticated
techniques to prevent overfitting and instability.  These can include soft target updates, Boltzmann and Bayesian exploration methods, and 
vectorized neural net updates for improved training times.  Below is a training graph using a dqn with some of these additional methods implemented 
to solve the lunar lander domain (200 point average over 100 consecutive runs).   

><a href="https://gym.openai.com/envs/LunarLander-v2/"> Lunar Lander</a> DQN Training Graph  

![Lunar Lander](https://github.com/jlm429/RL/blob/master/images/lunarlander.PNG)


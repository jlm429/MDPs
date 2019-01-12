> ## Deep Q-Learning (<a href="https://github.com/jlm429/RL/blob/master/dqn/dqnLearner.py">dqnLearner.py</a>, <a href="https://github.com/jlm429/RL/blob/master/dqn/neural_net.py">neural_net.py</a>)  
> OpenAI domains (<a href="https://gym.openai.com/envs/CartPole-v0/">CartPole</a>, <a href="https://gym.openai.com/envs/Acrobot-v1/">Acrobot</a>)

Q-learning uses temporal differences to estimate state-action values and discretization or function approximation to evaluate the state.
Instead of using a Q-table, a neural network can be used to approximate q-values. Many function
approximators, such as neural nets and local weighted regression, can cause instability in reinforcement
learning by exaggerating the difference between target values 
<a href="https://www.sciencedirect.com/science/article/pii/B9781558603776500402"> (Gordon 1995)</a>. Deep Q-learning 
uses experience replay to help resolve this issue by randomizing samples. The 
behavior distribution is averaged over many previous states which breaks correlations and reduces the
variance of the updates <a href="https://arxiv.org/pdf/1312.5602.pdf"> (Minh et al. 2013)</a>. It should be noted however that Q-learning with function 
approximation does not have the same guaranteed convergence properties as the original Q-learning algorithm (<a href="http://www.leemon.com/papers/1995b.pdf">Baird 1995</a>).  
<br>
The concept of experience replay has roots in neuroscience
and the belief that time-compressed reactivation of recently experienced trajectories during offline periods
provide a mechanism for updating value functions <a href="https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf"> (Minh et al. 2015)</a>. 
Representation learning with deep learning can enable automatic feature engineering and end-to-end learning through gradient descent, so that
reliance on domain knowledge is significantly reduced or even removed
<a href="https://arxiv.org/pdf/1701.07274.pdf"> (Li 2017)</a>.  

>DQN pseudocode (from <a href="https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf"> DQN Nature Paper</a>)

![DQN pseudocode](https://github.com/jlm429/RL/blob/master/images/dqnpseudocode.PNG)

Complex domains such as <a href="https://gym.openai.com/envs/LunarLander-v2/">lunar lander</a> and 
<a href="https://gym.openai.com/envs/MountainCarContinuous-v0/"> mountain car</a> require precise hyper-parameter tuning and more sophisticated
techniques to prevent overfitting and instability.  These can include soft target updates 
<a href="https://arxiv.org/pdf/1509.02971.pdf"> (Lillicrap et al. 2015) </a>, Boltzmann and Bayesian exploration, and 
vectorized neural net updates for improved training times.  Below is a training graph using a dqn with some of these additional methods implemented 
to solve the lunar lander domain (200 point average over 100 consecutive runs).   

><a href="https://gym.openai.com/envs/LunarLander-v2/"> Lunar Lander</a> DQN Training Graph  

![Lunar Lander](https://github.com/jlm429/RL/blob/master/images/lunarlander.PNG)


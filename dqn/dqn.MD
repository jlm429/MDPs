> ## Deep Q-Learning (<a href="https://github.com/jlm429/RL/blob/master/dqn/dqnLearner.py">dqnLearner.py</a>, <a href="https://github.com/jlm429/RL/blob/master/dqn/neural_net.py">neural_net.py</a>)  
> OpenAI domains (<a href="https://gym.openai.com/envs/CartPole-v0/">CartPole</a>, <a href="https://gym.openai.com/envs/Acrobot-v1/">Acrobot</a>)

Deep Q-learning uses experience replay to help resolve instability issues when using Q-learning with function approximation 
<a href="http://www.leemon.com/papers/1995b.pdf">(Baird 1995)</a>.  The concept of experience replay has roots in neuroscience
and the belief that time-compressed reactivation of recently experienced trajectories during offline periods
provide a mechanism for updating value functions <a href="https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf"> (Minh et al. 2015)</a>. 

>DQN pseudocode (from <a href="https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf"> DQN Nature Paper</a>)

![DQN pseudocode](https://github.com/jlm429/RL/blob/master/images/dqnpseudocode.PNG)

<a href="https://gym.openai.com/envs/LunarLander-v2/">Lunar lander</a> and 
<a href="https://gym.openai.com/envs/MountainCarContinuous-v0/"> mountain car</a> require more precise hyper-parameter tuning and
additional techniques to speed up training and reduce instability.  These can include soft target updates 
<a href="https://arxiv.org/pdf/1509.02971.pdf"> (Lillicrap et al. 2015) </a>, Boltzmann and Bayesian exploration, and 
vectorized neural net updates.  Below are training results with some of these additional methods implemented used
to solve the lunar lander domain (200 point average over 100 consecutive runs).   

><a href="https://gym.openai.com/envs/LunarLander-v2/"> Lunar Lander</a> DQN Training Graph  

![Lunar Lander](https://github.com/jlm429/RL/blob/master/images/lunarlander.PNG)

>Trained Agent

![Video](https://www.youtube.com/watch?v=r-64RxCRyRM)


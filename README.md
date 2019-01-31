# Reinforcement Learning in Multiagent system (pong game)

In this project my aim is to investigate if two agents are capable of interacting with each other in a pong environment and how they would coordinate with each other in order to not let the pong ball hit the vertical walls behind the paddles. These agents are trained by reinforcement learning technique.

- [Multiagent Pong Game Environment (both agents can be controlled)](https://github.com/deepanshu96/Reinforcement_Learning_Multiagent_system-pong-game-/blob/master/Pong2.py)
- [Model for training both the agents simultaneously](https://github.com/deepanshu96/Reinforcement_Learning_Multiagent_system-pong-game-/blob/master/mlagent.ipynb)
- Youtube Video (https://www.youtube.com/watch?v=J3B3H2fU7jo)



## Building the game environment 

- The first and foremost requirement of the project was to build such a game environment in which I could control both the game playing agents (paddles in my case). For this I created a PongObject class and PongBall class for the two paddles (my learning agents) and the ball respectively. Both the classes had the initialization method in which their positions, action and initial score were initialized. 

- The PongObject class also had an update method which was used to update the position of the paddle according to the given action. The ball in the game environment was initially sent into a random direction and after that the game was played by the paddle.

- The major class in the pong game was the PongGame class. It had 2 objects of the PongObject class namely paddle1 and paddle2 and one object of the PongBall class that is the ball.

- The PongGame class has a step_() method which is used to take in action1 and action2 parameters. They are the actions provided by the model, to be given to the paddle1 and paddle2 objects. It also has the whole update method for the ball in the pong game as to how it will react in different situations depending upon the actions taken by the paddle.

- Finally the score is also updated in this method according to the action and state of the paddle and ball. The PongGame class also has a getFrame() method  which is used to return the current frame of the game screen to be used as state in our model. Also the step_() function returns the paddle1 and paddle2 score along with the frame after taking the given actions. 

###  Game Environment
<img src="https://github.com/deepanshu96/Reinforcement_Learning_Multiagent_system-pong-game-/blob/master/Screen%20Shot%202018-12-09%20at%208.12.27%20PM.png" width="300" hspace = 10> <img src="https://github.com/deepanshu96/Reinforcement_Learning_Multiagent_system-pong-game-/blob/master/Screen%20Shot%202018-12-09%20at%208.12.35%20PM.png" width="300">

## Model for reinforcement learning

- I used reinforcement learning method known as deep q learning for solving the above problem and developing a suitable model for the game. 

- In my network the input was a grayscale image of 84x84 size and 4 of them were stacked in order to give the correct representation of the state. They were passed to the network and finally a three value solution was obtained which corresponded to each of the action of the paddle that is go up, stay there and go down action. The maximum value between the 
three was selected as the action to be taken. 

- I also used experience relay technique in which sample of each state, action, best action taken to maximise reward and reward were stored which were used to train my deep convolutional neural network. A random sample of batch of data was selected at each transition and was used to update the parameters of the network. 

- I also used exploration vs exploitation in which based on a certain probability the agent took a random action which was not the maximising reward action. This was done so that the agent does not get trapped in a local maxima and return erroneous actions. The probability of random action was decreased monotonically with time as the network learned better. The deep q learning model :-
<img src="https://github.com/deepanshu96/Reinforcement_Learning_Multiagent_system-pong-game-/blob/master/Picture5.png" width="400" > 

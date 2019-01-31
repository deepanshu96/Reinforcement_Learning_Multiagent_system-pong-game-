# Reinforcement Learning in Multiagent system (pong game)

In this project my aim is to investigate if two agents are capable of interacting with each other in a pong environment and how they would coordinate with each other in order to not let the pong ball hit the vertical walls behind the paddles. These agents are trained by reinforcement learning technique.



## Building the game environment 

- The first and foremost requirement of the project was to build such a game environment in which I could control both the game playing agents (paddles in my case). For this I created a PongObject class and PongBall class for the two paddles (my learning agents) and the ball respectively. Both the classes had the initialization method in which their positions, action and initial score were initialized. 

- The PongObject class also had an update method which was used to update the position of the paddle according to the given action. The ball in the game environment was initially sent into a random direction and after that the game was played by the paddle.

- The major class in the pong game was the PongGame class. It had 2 objects of the PongObject class namely paddle1 and paddle2 and one object of the PongBall class that is the ball.

- The PongGame class has a step_() method which is used to take in action1 and action2 parameters. They are the actions provided by the model, to be given to the paddle1 and paddle2 objects. It also has the whole update method for the ball in the pong game as to how it will react in different situations depending upon the actions taken by the paddle.

- Finally the score is also updated in this method according to the action and state of the paddle and ball. The PongGame class also has a getFrame() method  which is used to return the current frame of the game screen to be used as state in our model. Also the step_() function returns the paddle1 and paddle2 score along with the frame after taking the given actions. 

###  Game Environment
<img src="https://github.com/deepanshu96/Reinforcement_Learning_Multiagent_system-pong-game-/blob/master/Screen%20Shot%202018-12-09%20at%208.12.27%20PM.png" width="300" hspace = 10> <img src="https://github.com/deepanshu96/Reinforcement_Learning_Multiagent_system-pong-game-/blob/master/Screen%20Shot%202018-12-09%20at%208.12.35%20PM.png" width="300">

## Model for reinforcement learning

I used reinforcement learning method known as deep q learning for solving the above problem and developing a suitable model for the game. The deep q learning algorithm :-

<img src="https://github.com/deepanshu96/Reinforcement_Learning_Multiagent_system-pong-game-/blob/master/Picture4.png" width="400" > 

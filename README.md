# AI Project - Reinforcement Learning with OpenAI Gym Taxi-v3

The project delves into a comparative study of several state-of-the-art Reinforcement Learning algorithms using the Taxi-v3 environment provided by [OpenAI Gym](https://gym.openai.com/). _OpenAI Gym_ provides an array of gaming and virtual environments with pre-defined state spaces and action spaces. This makes for an ideal candidate for developers to explore their own AI algorithms or even implement state-of-the-art Reinforcement Learning algorithms. the Taxi-v3 environment has been selected for our project, because it provides a finite number of state spaces with and ideal number of action spaces. The environment also employs certain sub-missions such as pickups and drop-offs which is beneficial while performing comparative algorithm analysis as it is always desirable to have a certain level of complexity within the problem.
The algorithms selected are as follows:
* Random Search - to create a baseline
* Q-Learning
* SARSA (State Action Reward State Action)
* Expected SARSA
* Deep Q Networks

## The Taxi-v3 Environment ##

The [Taxi-v3 environment](https://gym.openai.com/envs/Taxi-v3/) provides a basic real-world transportation problem environment with a single taxi that acts as the agent, a passenger that needs to be picked up from his pick up location and dropped at his drop-off location. The taxi may or may not be at the pick up location at the initial stage. Therefore, essentiall the taxi needs to move towards the passenger, pick them up, travel towards the drop-off location and then drop them off. These set of actions constitute the total action space available to the agent. Additionally there are also certain obstrutions in the environment which the agent needs to avoid. An image of the environment frame is shown below:


![Picture alt](https://github.com/scrntnstrnglr/AIProject/blob/master/AIDemo/graphs/frames.png)

There are four possible locations for pick up and drop off, these are the ones marked by R,G,B and Y. For a particular iteration, the pickup spot will be highlighted by blue, while the drop off spot will be highlighted by purple. Therefore, from the initial state as shown in the image, the taxi needs to pick the passenger up from B and drop them off at location Y. When the passenger is not in the taxi, the colour of the agent/taxi is denoted as yellow, if the passenger has been picked up by the taxi, its colour changes to green. And finally, once the taxi drops the passenger off, it's colour changes back to yellow. The straigh lines | denote obstructions through which the agent cannot pass. The possible actions the agent can take are:
* North - move up from current location
* South - move down from current location
* West - move left from current location
* East - move right from current location
* Pickup - pick the passenger up.
* Drop-off - drop the passenger off.

The agent is rewarded a point of -1 on taking any action, if the agent picks up of drops the passenger off at an incorrect location, it incurs a reward of -10, and finally when the agent drops the passenger off at the correct location it is reward a point of +20. This is to ensure that the agent is able to differentiate between the right and wrong steps.
A sample run through of the environment can be seen below:


![run through](https://github.com/scrntnstrnglr/AIProject/blob/master/AIDemo/img/frames_sample.gif)

## Project Setup ##

To analyze our algorithms effectively, this project has been setup with certain parameter restrictions:
* Number of iterations for each algorithm : 5000
* Measurable quantities: 
    - Epochs : time step for the agent to reach the final state from the initial state.
    - Penalties : if reward == -10 then penalty++. We have opted to count the number of times the agent takes an incorrect step.
* Baseline algorithm : Random Search
* Hyperparameters:
    - alpha : learning rate.
    - gamma : discount factor.
    - epsilon : balance factor between exploration and exploitation.

### Usage ###
The following steps should be followed to re-use this project:
* Clone or download this project into your own repo or local machine
```
git clone https://github.com/scrntnstrnglr/AIProject
```
* The repo contains a virtual environment setup that should appear on your code editor with the name 'AIDemo'
* Install dependencies -- __Necessary to have pipenv__
```
pipenv install
```
* The following jupyter notebooks contain respective algorithms as follows:
    - gymdemo.ipynb : Q-Learning, Random Search.
    - SARSA_V2.ipynb : SARSA.
    - expected_SARSA.py : Expected SARSA.
    - DQN.ipynb : Deep Q-Networks.
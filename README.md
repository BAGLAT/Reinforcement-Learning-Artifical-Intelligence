# AI Project - Reinforcement Learning with OpenAI Gym Taxi-v3

The project delves into a comparative study of several state-of-the-art Reinforcement Learning algorithms using the Taxi-v3 environment provided by [OpenAI Gym](https://gym.openai.com/). _OpenAI Gym_ provides an array of gaming and virtual environments with pre-defined state spaces and action spaces. This makes for an ideal candidate for developers to explore their own AI algorithms or even implement state-of-the-art Reinforcement Learning algorithms. the Taxi-v3 environment has been selected for our project, because it provides a finite number of state spaces with and ideal number of action spaces. The environment also employs certain sub-missions such as pickups and drop-offs which is beneficial while performing comparative algorithm analysis as it is always desirable to have a certain level of complexity within the problem.
The algorithms selected are as follows:
* Random Search - to create a baseline
* Q-Learning
* SARSA (State Action Reward State Action)
* Expected SARSA
* Deep Q Networks

## The Taxi-v3 Environment ##

The [Taxi-v3 environment](https://gym.openai.com/envs/Taxi-v3/) provides a basic real-world transportation problem environment with a single taxi that acts as the agent, a passenger that needs to be picked up from his pick up location and dropped at his drop-off location. The taxi may or may not be at the pick up location at the initial stage. Therefore, essentiall the taxi needs to move towards the passenger, pick them up, travel towards the drop-off location and then drop them off. These set of actions constitute the total action space available to the agent. Additionally there are also certain obstrutions in the environment which the agent needs to avoid. 


![Picture alt](https://github.com/scrntnstrnglr/AIProject/blob/master/AIDemo/graphs/frames.png)
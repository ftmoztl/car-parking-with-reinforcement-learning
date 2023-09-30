# Q-learning Application to Find an Optimal Parking Slot

This study aims to solve the parking issues faced by drivers in cities by proposing a framework based on Reinforcement Learning (RL).

Consider an individual who commutes to work and wants to find a parking spot close to their office/target place. They approach from the east and desire a spot as close as possible to their target place. However, their visibility is limited, and they can only assess the availability of parking spots at their current location. They must decide whether to park in the current spot or continue searching for a closer one, weighing the benefits against the additional time and effort required.

Existing solutions to this problem rely on technologies like smart cameras and sensors, but they are heavily dependent on the performance of applications and detection models. This study seeks to reduce these dependencies by adopting a game-like approach to parking, where uncertain results can be learned through reinforcement learning. 

You can find this problem in this [Operation Research][book]* book, in the Probabilistic Dynamic Programming section. So, the problem is tried to solve by various methods and applications. You can find the demo of probabilistic dynamic programming approach for this study in the [‘probabilistic-dp.ipynb’][prob] Jupyter Notebook.

**Winston, Wayne L. Operations research: applications and algorithms. Cengage Learning, 2022.*

[book]: https://www.academia.edu/48990438/Operational_Research_Winston_Wayne
[prob]: https://github.com/ftmoztl/car-parking-with-reinforcement-learning/blob/main/Codes/probabilistic-dp.ipynb
# Methods & Algorithms
In this approach, in the car parking problem, the agent (our actor) would take actions (park or move forward to find a more close parking slot) and receive rewards (e.g., parking done in a short time and closest area to the target) from the user. The nature of this problem is interactive, sequential, and agent-based. Q-learning is more flexible and can handle larger state spaces and unknown transition probabilities. It is suitable when the state space is large or continuous, and the transition probabilities are unknown or difficult to model. 
* Q-learning is a model-free algorithm, meaning it does not require prior knowledge or explicit knowledge of the environment dynamics. 
* Q-learning incorporates the exploration-exploitation trade-off, which is crucial in solving complex problems. 
* Q-learning employs value iteration to iteratively update the Q-values, which represent the expected rewards for taking specific actions in specific states. Q represents quality. So the agent will learn quickly and consciously by updating the Q table with mote qualified results of the action.

# Learning Environment Creation
The actors of the environment of learning are below; 
* Agent: Car or car driver, 
* Actions: 5 actions are available, turn left, turn right, go up and down, park, 
* States: Location of the agent with parked or not parked, 
* Environment: The focus area includes the target place, and it will include restrictions that can be on the road (lines that indicate the out of road, traffics, etc.)
* Reward: Regular movement rewards with constants and parking rewards with closeness to the target. 

The simulation environments are developed to create this restricted environment with these factors. It is assumed that each resource, each driver, and each destination has a known location associated with it in a 2–dimensional Euclidean space as indicated in this study.

## Reward Policy
The studied environment is a static environment with its constant. Luckily, the area to move and park can be explained with a cartesian coordinate system, so locations are explained by 2D values. So, the environments are created with the X and Y coordination. So, the following variables are kept constant to tune the environment consciously:
* Size of the area/cartesian coordinate system: 20
* Starting location of the agent: (19, 12)
* Target place to want to reach and park: (5, 5)
* Other available and empty parking spaces: [[12, 16], [9, 12], [14, 7], [5, 5]]
* Road coordination's and directions: x-coordination: [[5,6],[11,12]], y-coordination: [[7, 8], [12, 13]]

Action in the environment is designed with a determined road. For example, if the y coordination of the agent is 8, the agent should go in the right direction according to the traffic flow rules. These rules are implemented in the environment with the rewards of the end of the action. If the agent acts against the rules, it will punish. For example, if the agent goes out off the road, the agent will punish with a high minus reward. But the important point is that, if the agent parks the target position, should get the highest reward. According to the reward and punishment rules, the agent will act well. So, the reward policy is really important to direct the agent to the best location. In the experiment phase, lots of rewarding policy is tried to see agent behavior. You can find 7 of them in the [‘environments.py’][env] with explanations. These are used to find the best reward policy.

In this process, it's important to create a field with proper rewards for the agent not get stuck locally (parking areas far from the destination) and reach the target with the minimum steps. Fields 4 and 7 provide this environment. You can run each environment in the py file, and visualize the graph of a number of steps for each episode. We expect that the number of steps should converge after 250-300 episodes, so the agent learns the optimal steps in these episodes. 

[env]: https://github.com/ftmoztl/car-parking-with-reinforcement-learning/blob/main/Codes/environments.py
# Hyperparameter Tuning 
The Field_4 environment is used throughout the hyperparameter tuning process. So, the focus of this section is tuning the hyperparameters. The alpha and gamma values are tuning to reach high performances. These metrics should be considered;
* Minimum of average number of steps to reach the target,
* Maximum of average total rewards,
* High percentage of reaching the target parking place

You can run ['hyperparam-tuning.py'][hyper] notebook to tune alpha and gamma values. And you can check which values give the best results.

According to our experiment, the optimal value of alpha is chosen as 0.3, and the optimal value of gamma is chosen as 0.5. And between episodes 150-200 the learning completed and nearly converged. It gives faster convergence than according to the previous results.

[hyper]: https://github.com/ftmoztl/car-parking-with-reinforcement-learning/blob/main/Codes/hyperparam-tuning.py
# Visualization
The agent movements are visualized by using the ‘pillow’ package of Python. It’s adapted to the 20x20 field. A function is created to visualize roads, agents, parking lots, and target places. You can find in the ['visualization-traffic.ipynb'][viz] notebook.

[viz]: https://github.com/ftmoztl/car-parking-with-reinforcement-learning/blob/main/Codes/visualization-traffic.ipynb
# Flexible Environment
For real cases, of course, there will not be a fixed-size field for the agent. To play with the environment, target, and other constants, a flexible environment are designed. In this flexible environment, agents can learn and be tested for the field with high size. And The [‘learning-flexible-env.py’][flex] also includes the random solution to see how Q-learning is working effectively and the random solution is very slow.

[flex]: https://github.com/ftmoztl/car-parking-with-reinforcement-learning/blob/main/Codes/learning-flexible-env.py
# Development Environment
All development processes are done in a Python environment. The environment Python script and field classes are created to constitute environments for the agent and learning process. And also for visualization of the agent movement, the ‘pillow’ Python package is used.

To install the dependencies to run the notebook, you can use Anaconda. Once you have installed Anaconda, run:

`$ conda env create -f environment.yml`

# Related Studies
- Bogoslavskyi, Igor, et al. "Where to park? minimizing the expected time to find a parking space." 2015 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2015.
- Winston, Wayne L. Operations research: applications and algorithms. Cengage Learning, 2022.
- Houissa, Asma, et al. "A learning algorithm to minimize the expectation time of finding a parking place in urban area." 2017 IEEE Symposium on Computers and Communications (ISCC). IEEE, 2017.
- Ratli, Mustapha, et al. "Dynamic assignment problem of parking slots." 2019 International Conference on Industrial Engineering and Systems Management (IESM). IEEE, 2019.
- Klappenecker, Andreas, Hyunyoung Lee, and Jennifer L. Welch. "Finding available parking spaces made easy." Proceedings of the 6th International Workshop on Foundations of Mobile Computing. 2010.

# Contribution
If you want to contribute please, send your pull request. All contributions are welcome!

#
Please check that repository for updates, for opening issues or sending pull requests.
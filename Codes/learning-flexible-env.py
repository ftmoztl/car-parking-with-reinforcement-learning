import math
import matplotlib.pyplot as plt
import math
import numpy as np
import random
from random import sample
from itertools import chain

"""
This notebook is designed to create flexible roads. 
Imagine, you have a coordination system, you have roads on them. Your roads should have two directions; up&down,right&left
In this script, you should only change these two variables: size, x_coordinates, y_coordinates
Size gives the dimension of the coordinate system. 
x_coordinates gives the indexes of the vertical roads
y_coordinates gives the indexes of the horizontal roads
For example,  x_coordinates = [[5,6],[11,12]] means that 
you have 2 vertical roads, when x=5 agent can go down, x=6 agent can go up in two direction road
For the other road, if  x=11 the agent can go down, x=12 agent can go up in two direction road
'field_flexible_road' class is designed according to road indexes and directions.
'reinforcement_q' function is design to learning loop for the agent.
you can also indicate how many available parking spaces should be. "k" gives that.

Please be sure: 
--size should be an integer
--x_coordinates, y_coordinates should be 2-D lists, the nested list should have 2 elements, x, and y
--k should be an integer

-----> Press control + F, write "you can change" 
"""


class field_flexible_road:
    def __init__(self, size, start_position, target_position, parking_lot_coor, x_coordinates, y_coordinates):
        self.size = size
        self.parking = False  # true or false, park or not park, start with not park
        self.target_position = target_position  # there is a target position which has high reward
        self.position = start_position  # determine start position
        self.parking_lot_coor = parking_lot_coor  # there are other empty lots, keep them in a list
        self.x_coordinates = x_coordinates # it includes vertical road indexes
        self.y_coordinates = y_coordinates # it includes horizontal road indexes

    def get_number_of_states(self):
        return self.size * self.size * 2  # multiply by 2 to add status of parked or not

    def get_state(self):
        # state goes like (0,0,F), (0,0,T), (0,1,F), (0,1,T), (0,2,F)...
        state = self.position[0] * self.size * 2
        state = state + self.position[1] * 2

        # if parking is done, you'll be in the next state F-->T (*,*,T)
        if self.parking:
            state = state + 1
        return state

    def make_action(self, action):

        def calc_reward():
            distance = math.dist(self.position, self.target_position)

            # we want to maximize reward, minimize distance
            reward = -1 * (distance)

            return reward

        (x, y) = self.position
        if action == 0:  # down
            if y == self.size - 1: # penalize for out of canvas
                return -20, False
            elif x in [x[0] for x in self.x_coordinates]: # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            elif (x, y) in [(0,y[0]) for y in self.y_coordinates]: # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            else:
                return -20, False # penalize for out of road

        elif action == 1:  # up
            if y == 0: # penalize for out of canvas
                return -20, False
            elif x in [x[1] for x in self.x_coordinates]: # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            elif (x, y) in [(self.size - 1,y[1]) for y in self.y_coordinates]: # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            else:
                return -20, False # penalize for out of road

        elif action == 2:  # left
            if x == 0: # penalize for out of canvas
                return -20, False
            elif y in [y[0] for y in self.y_coordinates]: # go in the true direction
                self.position = (x - 1, y)
                return -1, False
            elif (x, y) in [(x[1],0) for x in self.x_coordinates]: # go in the true direction
                self.position = (x - 1, y)
                return -1, False
            else:
                return -20, False # penalize for out of road

        elif action == 3:  # right
            if x == self.size - 1: # penalize for out of canvas
                return -20, False
            elif y in [y[1] for y in self.y_coordinates]: # go in the true direction
                self.position = (x + 1, y)
                return -1, False
            elif (x, y) in [(x[0],self.size - 1) for x in self.x_coordinates]: # go in the true direction
                self.position = (x + 1, y)
                return -1, False
            else:
                return -20, False # penalize for out of road

        elif action == 4:  # park
            if [x, y] not in self.parking_lot_coor: # if it's not a parking lot
                return -20, False
            elif self.target_position == (x, y):
                reward = calc_reward()
                self.parking = True
                return reward + 20, True # yey it's target!!! #calculate -distance + 20 as a reward
            else:
                reward = calc_reward()
                self.parking = True
                return reward, True # no target position but it's a lot #finish the loop #calculate -distance as a reward


# learning...

# function to create roads from determined x and y coordinates
def random_start_target_parking(size, x_coordinates, y_coordinates):
    # flatten to use indexes
    road_x_coordinates = list(chain.from_iterable(x_coordinates))
    road_y_coordinates = list(chain.from_iterable(y_coordinates))

    road_list = []

    # add location in the roads
    for i in range(size):
        for el_x in road_x_coordinates:
            road_list.append([el_x, i])
        for el_y in road_y_coordinates:
            road_list.append([i, el_y])

    # remove intersections of horizontal and vertical from the list
    for el_x in road_x_coordinates:
        for el_y in road_y_coordinates:
            for k in range(2):
                road_list.remove([el_x, el_y])

    # return road list, it includes all possible location to park and move
    return road_list

# function to take a sample from road and put them as a starting loc, target loc, parking lots
def random_coord(list_of_possible_parking):
    random.seed(0)  # keep seed for the learning process, it's up to you
    loc_list = random.choices(list_of_possible_parking,
                              k=10) # you can change # k should be greater than or equal to 2; starting, target, parking lots
    start_position = tuple(loc_list[0])
    target_position = tuple(loc_list[1])
    parking_lot_coor = loc_list[1:]

    return start_position, target_position, parking_lot_coor

# function for q-learning algorithm
def reinforcement_q(alpha, gamma):
    # give constants
    size = 40  # size of the canvas/coordination system # you can change

    # determine the possible roads, it should be 2 lane road; up and down, left and right
    # these should be 2D lists
    x_coordinates = [[5, 6], [11, 12], [17, 18], [25, 26]] # you can change
    y_coordinates = [[7, 8], [12, 13], [17, 18], [35,36]] # you can change

    # create list of available parking positions according to road indexes
    available_parking_places = random_start_target_parking(size, x_coordinates, y_coordinates)

    # start agent from random starting position
    # give target location to park
    # give all empty parking space location #it should include the target
    start_position, target_position, parking_lot_coor = random_coord(available_parking_places)

    print("Starting position: ", start_position)
    print("Target parking position: ", target_position)
    print("All available parking lots: ", parking_lot_coor)

    # initialize environment
    field = field_flexible_road(size, start_position, target_position, parking_lot_coor, x_coordinates, y_coordinates)

    # create number of states according to size
    number_of_states = field.get_number_of_states()
    number_of_actions = 5  # it's certain # left, right, up, down, park

    # create empty q table
    q_table = np.zeros((number_of_states, number_of_actions))

    # determine hyperparameter
    alpha = alpha  # parameter to tune
    gamma = gamma  # parameter to tune
    epsilon = 1  # start epsilon from 1
    max_epsilon = 1
    min_epsilon = 0.01
    decay = 0.01  # use decay to balance exploration and exploitation

    # give number of episodes
    train_episodes = 1000

    # keep the metrics to evaluate learning process
    steps = []  # keep number of steps
    target_or_not = []  # keep info of if the agent finds the target or park another location
    end_locations = []  # keep end location to see if it's target place or not
    training_rewards = []  # keep rewards
    epsilons = []  # keep epsilon values to see exploration and exploitation percentages

    for episode in range(train_episodes):

        # initialize env in the learning loop
        field = field_flexible_road(size, start_position, target_position, parking_lot_coor, x_coordinates,
                                    y_coordinates)
        done = False  # to finish the episode

        step = 0
        total_training_rewards = 0

        while not done:  # if done is true, finish the episode
            state = field.get_state()  # start with learning state of the agent

            if random.uniform(0, 1) > epsilon:  # explore or exploit
                action = np.argmax(q_table[state])  # exploit
            else:
                action = random.randint(0, 4)  # explore

            reward, done = field.make_action(action)  # position can be change

            total_training_rewards += reward  # sum rewards

            new_state = field.get_state()  # enter new state according to new position
            new_state_max = np.max(
                q_table[new_state])  # learn which q value is max for the next state to calculate q value

            # update q table
            q_table[state, action] = (1 - alpha) * q_table[state, action] + alpha * (
                    reward + gamma * new_state_max - q_table[state, action])

            step = step + 1  # increase step value

            # to learn the parking location whether is the target location or not
            target_tf = False
            if field.position == field.target_position:
                target_tf = True

            end_location = field.position  # keep end location of this state to trace the

        # cut down on exploration by reducing the epsilon
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay * episode)

        # append all values of episodes to their list
        epsilons.append(epsilon)
        steps.append(step)
        target_or_not.append(target_tf)
        end_locations.append(end_location)
        training_rewards.append(total_training_rewards)

    return np.mean(steps), np.mean(training_rewards), steps, training_rewards, epsilons, target_or_not, \
        size, start_position, target_position, parking_lot_coor, x_coordinates, y_coordinates

print("----------------------Q LEARNING SOLUTION----------------------")
avg_steps, avg_rewards, steps, training_rewards, epsilons, target_or_not, \
    size, start_position, target_position, parking_lot_coor, x_coordinates, y_coordinates = reinforcement_q(alpha=0.3, gamma=0.5)

count = 0
for el in target_or_not:
    if el:
        count += 1


print(
    f"The agent has parked in the target parking place only {count} times. Percentage of hitting the target: {int(count / len(target_or_not) * 100)}%")
print(f"Avg Steps: {avg_steps}, Avg Rewards: {avg_rewards}")

# After the Q-learning loop

# Visualizing the steps over all episodes
plt.plot(steps)
plt.xlabel('Episode')
plt.ylabel('Number of Steps')
plt.title('Q-Learning Progress')
plt.show()

# Visualizing the training rewards over all episodes
plt.plot(training_rewards)
plt.xlabel('Episode')
plt.ylabel('Training total reward')
plt.title('Total rewards over all episodes in training')
plt.show()

# Visualizing the epsilons over all episodes
plt.plot(epsilons)
plt.xlabel('Episode')
plt.ylabel('Epsilon')
plt.title("Epsilon for episode")
plt.show()


def random_solution(size, start_position, target_position, parking_lot_coor, x_coordinates, y_coordinates):
    # give constants
    #size = 30  # size of the canvas/coordination system

    # determine the possible roads, it should be 2 lane road; up and down, left and right
    # these should be 2D lists
    #x_coordinates = [[5, 6], [11, 12], [17, 18]]
    #y_coordinates = [[7, 8], [12, 13], [17, 18]]

    # create list of available parking positions according to road indexes
    #available_parking_places = random_start_target_parking(size, x_coordinates, y_coordinates)

    # start agent from random starting position
    # give target location to park
    # give all empty parking space location #it should include the target
    #start_position, target_position, parking_lot_coor = random_coord(available_parking_places)

    print("Starting position: ", start_position)
    print("Target parking position: ", target_position)
    print("All available parking lots: ", parking_lot_coor)

    # initialize environment
    field = field_flexible_road(size, start_position, target_position, parking_lot_coor, x_coordinates, y_coordinates)

    # give number of episodes
    train_episodes = 1000

    # keep the metrics to evaluate learning process
    steps = []  # keep number of steps
    target_or_not = []  # keep info of if the agent finds the target or park another location
    end_locations = []  # keep end location to see if it's target place or not

    for episode in range(train_episodes):

        # initialize env in the learning loop
        field = field_flexible_road(size, start_position, target_position, parking_lot_coor, x_coordinates,
                                    y_coordinates)
        done = False  # to finish the episode

        step = 0

        while not done:  # if done is true, finish the episode

            action = random.randint(0, 4)  # explore
            reward, done = field.make_action(action)  # position can be change
            step = step + 1  # increase step value

            # to learn the parking location whether is the target location or not
            target_tf = False
            if field.position == field.target_position:
                target_tf = True

            end_location = field.position  # keep end location of this state to trace the

        # append all values of episodes to their list
        steps.append(step)
        target_or_not.append(target_tf)
        end_locations.append(end_location)

    return np.mean(steps), steps, target_or_not

print("------------------------RANDOM SOLUTION------------------------")

avg_steps, steps, target_or_not = random_solution(size, start_position, target_position, parking_lot_coor, x_coordinates, y_coordinates)

count = 0
for el in target_or_not:
    if el:
        count += 1

print(
    f"The agent has parked in the target parking place only {count} times. Percentage of hitting the target: {int(count / len(target_or_not) * 100)}%")
print(f"Avg Steps: {avg_steps}, Avg Rewards: No reward")

# Visualizing the steps over all episodes
plt.plot(steps)
plt.xlabel('Episode')
plt.ylabel('Number of Steps')
plt.title('Random Progress')
plt.show()
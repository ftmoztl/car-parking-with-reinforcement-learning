from environments import Field_1, Field_2, Field_3, Field_4, Field_5, Field_6, Field_7
import matplotlib.pyplot as plt
import math
import numpy as np
import random

# learning...

def reinforcement_q(alpha, gamma):
    # give constants
    size = 20 # size of the canvas/coordination system
    start_position = (19, 12) # start agent from this position
    target_position = (5, 5)  # give target location to park
    parking_lot_coor = [[12, 16], [9, 12], [14, 7], [5, 5]]  # give all empty parking space location #it should include the target

    # initialize environment
    field = Field_4(size, start_position, target_position, parking_lot_coor)

    # create number of states according to size
    number_of_states = field.get_number_of_states()
    number_of_actions = 5  # it's certain # left, right, up, down, park

    # create empty q table
    q_table = np.zeros((number_of_states, number_of_actions))

    # determine hyperparameter
    alpha = alpha # parameter to tune
    gamma = gamma # parameter to tune
    epsilon = 1 # start epsilon from 1
    max_epsilon = 1
    min_epsilon = 0.01
    decay = 0.01  # use decay to balance exploration and exploitation

    # give number of episodes
    train_episodes = 1000

    # keep the metrics to evaluate learning process
    steps = [] # keep number of steps
    target_or_not = [] # keep info of if the agent finds the target or park another location
    end_locations = [] # keep end location to see if it's target place or not
    training_rewards = [] # keep rewards
    epsilons = [] # keep epsilon values to see exploration and exploitation percentages

    for episode in range(train_episodes):

        # initialize env in the learning loop
        field = Field_4(size, start_position, target_position, parking_lot_coor)
        done = False # to finish the episode

        step = 0
        total_training_rewards = 0

        while not done:  # if done is true, finish the episode
            state = field.get_state() # start with learning state of the agent

            if random.uniform(0, 1) > epsilon:  # explore or exploit
                action = np.argmax(q_table[state])  # exploit
            else:
                action = random.randint(0, 4)  # explore

            reward, done = field.make_action(action)  # position can be change

            total_training_rewards += reward # sum rewards

            new_state = field.get_state()  # enter new state according to new position
            new_state_max = np.max(q_table[new_state]) # learn which q value is max for the next state to calculate q value

            # update q table
            q_table[state, action] = (1 - alpha) * q_table[state, action] + alpha * (
                        reward + gamma * new_state_max - q_table[state, action])

            step = step + 1 # increase step value

            # to learn the parking location whether is the target location or not
            target_tf = False
            if field.position == field.target_position:
                target_tf = True

            end_location = field.position # keep end location of this state to trace the

        # cut down on exploration by reducing the epsilon
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay * episode)

        # append all values of episodes to their list
        epsilons.append(epsilon)
        steps.append(step)
        target_or_not.append(target_tf)
        end_locations.append(end_location)
        training_rewards.append(total_training_rewards)

    return np.mean(steps), np.mean(training_rewards), steps, training_rewards, epsilons, target_or_not

avg_steps, avg_rewards, steps, training_rewards, epsilons, target_or_not = reinforcement_q(alpha=0.3, gamma=0.5)

count = 0
for el in target_or_not:
    if el:
        count+=1

print(f"The agent has parked in the target parking place only {count} times. Percentage of hitting the target: {int(count/len(target_or_not)*100)}%")
print(f"Avg Steps: {avg_steps}, Avg Rewards: {avg_rewards}")

# After the Q-learning loop

# Visualizing the steps over all episodes
plt.plot(steps)
plt.xlabel('Episode')
plt.ylabel('Number of Steps')
plt.title('Learning Progress')
plt.show()

# Visualizing the training rewards over all episodes
plt.plot(training_rewards)
plt.xlabel('Episode')
plt.ylabel('Training total reward')
plt.title('Total Rewards Over All Episodes')
plt.show()

# Visualizing the epsilons over all episodes
plt.plot(epsilons)
plt.xlabel('Episode')
plt.ylabel('Epsilon')
plt.title("Epsilon for Episode")
plt.show()
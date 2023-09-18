from environments import Field_1, Field_2, Field_3, Field_4, Field_5, Field_6, Field_7
from learning import reinforcement_q
import matplotlib.pyplot as plt
import math
import numpy as np
import random
import pandas as pd


# define the range of alpha and gamma values to explore
alpha_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
gamma_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

results_list = []  # dictionary to store the results

for alpha in alpha_values:
    for gamma in gamma_values:

        avg_steps, avg_rewards, steps, training_rewards, epsilons, target_or_not = reinforcement_q(alpha, gamma)

        count = 0
        for el in target_or_not:
            if el:
                count += 1

        results = {"alpha": alpha, "gamma": gamma, "avg_steps": avg_steps, "avg_rewards": avg_rewards,
                   "hitting_target": int(count / len(target_or_not) * 100)}
        results_list.append(results)

# print the results
for el in results_list:
    alpha = el["alpha"]
    gamma = el["gamma"]
    avg_step = el["avg_steps"]
    avg_rewards = el["avg_rewards"]
    hitting_target = el["hitting_target"]
    print(
        f"Alpha: {alpha}, Gamma: {gamma}, Avg Steps: {avg_step}, Avg Rewards: {avg_rewards}, Hitting Target: {hitting_target}%")

# create dataframe to sort and filter the result easily
df = pd.DataFrame(results_list)

# print good results
print(df[(df["avg_steps"] > 50) & (df["hitting_target"] > 90)])
# This py file includes every environment for the agent
# These environments have been tuned to find good reward policy
import math

"""
###POLICY 1 - FIELD 1######

--Calculate rewards with constants--
Put regular steps reward -1
Put out of the road and wrong direction reward -100
Put parking to the target space reward 100 and finish episode
Put parking to the other empty space reward 20 and not finish the episode
"""

class Field_1:
    def __init__(self, size, start_position, target_position, parking_lot_coor):
        self.size = size
        self.parking = False  # true or false, park or not park, starts with not park
        self.target_position = target_position  # there is a target position which has high reward
        self.position = start_position  # determine start position
        self.parking_lot_coor = parking_lot_coor  # there are other empty lots, keep them in a list

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
        (x, y) = self.position
        if action == 0:  # down
            if y == self.size - 1: # penalize for out of canvas
                return -100, False
            elif x == 5 or x == 11: # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            elif (x, y) == (0, 7) or (x, y) == (0, 12): # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            else:
                return -100, False  # penalize for out of road

        elif action == 1:  # up
            if y == 0: # penalize for out of canvas
                return -100, False
            elif x == 6 or x == 12: # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            elif (x, y) == (self.size - 1, 8) or (x, y) == (self.size - 1, 13): # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            else:
                return -100, False # penalize for out of road

        elif action == 2:  # left
            if x == 0: #penalize for out of canvas
                return -100, False
            elif y == 7 or y == 12:
                self.position = (x - 1, y) # go in the true direction
                return -1, False
            elif (x, y) == (6, 0) or (x, y) == (12, 0): # go in the true direction
                self.position = (x - 1, y)
                return -1, False
            else:
                return -100, False # penalize for out of road

        elif action == 3:  # right
            if x == self.size - 1: # penalize for out of canvas
                return -100, False
            elif y == 8 or y == 13:
                self.position = (x + 1, y) # go in the true direction
                return -1, False
            elif (x, y) == (5, self.size - 1) or (x, y) == (11, self.size - 1): # go in the true direction
                self.position = (x + 1, y)
                return -1, False
            else:
                return -100, False # penalize for out of road

        elif action == 4:  # park
            if [x, y] not in self.parking_lot_coor:  # if it's not a parking lot
                return -100, False
            elif self.target_position == (x, y):
                self.parking = True
                return 100, True  # yey it's target!!!
            else:
                self.parking = False  # no target position but it's a lot #not finish the loop
                return 20, False

"""
###POLICY 2 - FIELD 2######

--Calculate rewards with constants--
Put regular steps reward -1
Put out of the road and wrong direction reward -100
Put parking to the target space reward 100 and finish episode
Put parking to the other empty space reward 20 and finish the episode
"""

class Field_2:
    def __init__(self, size, start_position, target_position, parking_lot_coor):
        self.size = size
        self.parking = False  # true or false, park or not park, starts with not park
        self.target_position = target_position  # there is a target position which has high reward
        self.position = start_position  # determine start position
        self.parking_lot_coor = parking_lot_coor  # there are other empty lots, keep them in a list

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
        (x, y) = self.position
        if action == 0:  # down
            if y == self.size - 1: # penalize for out of canvas
                return -100, False
            elif x == 5 or x == 11: # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            elif (x, y) == (0, 7) or (x, y) == (0, 12): # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            else:
                return -100, False  # penalize for out of road

        elif action == 1:  # up
            if y == 0: # penalize for out of canvas
                return -100, False
            elif x == 6 or x == 12: # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            elif (x, y) == (self.size - 1, 8) or (x, y) == (self.size - 1, 13): # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            else:
                return -100, False # penalize for out of road

        elif action == 2:  # left
            if x == 0: #penalize for out of canvas
                return -100, False
            elif y == 7 or y == 12:
                self.position = (x - 1, y) # go in the true direction
                return -1, False
            elif (x, y) == (6, 0) or (x, y) == (12, 0): # go in the true direction
                self.position = (x - 1, y)
                return -1, False
            else:
                return -100, False # penalize for out of road

        elif action == 3:  # right
            if x == self.size - 1: # penalize for out of canvas
                return -100, False
            elif y == 8 or y == 13:
                self.position = (x + 1, y) # go in the true direction
                return -1, False
            elif (x, y) == (5, self.size - 1) or (x, y) == (11, self.size - 1): # go in the true direction
                self.position = (x + 1, y)
                return -1, False
            else:
                return -100, False # penalize for out of road

        elif action == 4:  # park
            if [x, y] not in self.parking_lot_coor:  # if it's not a parking lot
                return -100, False
            elif self.target_position == (x, y):
                self.parking = True
                return 100, True  # yey it's target!!!
            else:
                self.parking = True  # no target position but it's a lot #finish the loop
                return 20, True

"""
###POLICY 3 - FIELD 3######

--Calculate rewards with constants--
Put regular steps reward -1
Put out of the road and wrong direction reward -10
Put parking to the target space reward 100 and finish episode
Put parking to the other empty space reward 2 and finish the episode
"""

class Field_3:
    def __init__(self, size, start_position, target_position, parking_lot_coor):
        self.size = size
        self.parking = False  # true or false, park or not park, starts with not park
        self.target_position = target_position  # there is a target position which has high reward
        self.position = start_position  # determine start position
        self.parking_lot_coor = parking_lot_coor  # there are other empty lots, keep them in a list

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
        (x, y) = self.position
        if action == 0:  # down
            if y == self.size - 1: # penalize for out of canvas
                return -10, False
            elif x == 5 or x == 11: # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            elif (x, y) == (0, 7) or (x, y) == (0, 12): # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            else:
                return -10, False  # penalize for out of road

        elif action == 1:  # up
            if y == 0: # penalize for out of canvas
                return -10, False
            elif x == 6 or x == 12: # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            elif (x, y) == (self.size - 1, 8) or (x, y) == (self.size - 1, 13): # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            else:
                return -10, False # penalize for out of road

        elif action == 2:  # left
            if x == 0: #penalize for out of canvas
                return -10, False
            elif y == 7 or y == 12:
                self.position = (x - 1, y) # go in the true direction
                return -1, False
            elif (x, y) == (6, 0) or (x, y) == (12, 0): # go in the true direction
                self.position = (x - 1, y)
                return -1, False
            else:
                return -10, False # penalize for out of road

        elif action == 3:  # right
            if x == self.size - 1: # penalize for out of canvas
                return -10, False
            elif y == 8 or y == 13:
                self.position = (x + 1, y) # go in the true direction
                return -1, False
            elif (x, y) == (5, self.size - 1) or (x, y) == (11, self.size - 1): # go in the true direction
                self.position = (x + 1, y)
                return -1, False
            else:
                return -10, False # penalize for out of road

        elif action == 4:  # park
            if [x, y] not in self.parking_lot_coor:  # if it's not a parking lot
                return -10, False
            elif self.target_position == (x, y):
                self.parking = True
                return 100, True  # yey it's target!!!
            else:
                self.parking = True  # no target position but it's a lot #finish the loop
                return 2, True

"""
###POLICY 4 - FIELD 4######

--Calculate rewards with distance--
Put regular steps reward -1
Put out of the road and wrong direction reward -20
Put parking to the target space reward (minus distance + 20) and finish episode
Put parking to the other empty space reward (minus distance) and finish the episode
"""
class Field_4:
    def __init__(self, size, start_position, target_position, parking_lot_coor):
        self.size = size
        self.parking = False  # true or false, park or not park, start with not park
        self.target_position = target_position  # there is a target position which has high reward
        self.position = start_position  # determine start position
        self.parking_lot_coor = parking_lot_coor  # there are other empty lots, keep them in a list

    def get_number_of_states(self):
        return self.size * self.size * 2  # multiply by 2 to add status of parked or not

    def get_state(self):
        # print(self.position)
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
            elif x == 5 or x == 11: # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            elif (x, y) == (0, 7) or (x, y) == (0, 12): # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            else:
                return -20, False # penalize for out of road

        elif action == 1:  # up
            if y == 0: # penalize for out of canvas
                return -20, False
            elif x == 6 or x == 12: # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            elif (x, y) == (self.size - 1, 8) or (x, y) == (self.size - 1, 13): # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            else:
                return -20, False # penalize for out of road

        elif action == 2:  # left
            if x == 0: # penalize for out of canvas
                return -20, False
            elif y == 7 or y == 12: # go in the true direction
                self.position = (x - 1, y)
                return -1, False
            elif (x, y) == (6, 0) or (x, y) == (12, 0): # go in the true direction
                self.position = (x - 1, y)
                return -1, False
            else:
                return -20, False # penalize for out of road

        elif action == 3:  # right
            if x == self.size - 1: # penalize for out of canvas
                return -20, False
            elif y == 8 or y == 13: # go in the true direction
                self.position = (x + 1, y)
                return -1, False
            elif (x, y) == (5, self.size - 1) or (x, y) == (11, self.size - 1): # go in the true direction
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

"""
###POLICY 5 - FIELD 5######

--Calculate rewards with distance--
Put regular steps reward -20
Put out of the road and wrong direction reward -100
Put parking to the target space reward (minus distance + 20) and finish episode
Put parking to the other empty space reward (minus distance) and finish the episode
"""
class Field_5:
    def __init__(self, size, start_position, target_position, parking_lot_coor):
        self.size = size
        self.parking = False  # true or false, park or not park, start with not park
        self.target_position = target_position  # there is a target position which has high reward
        self.position = start_position  # determine start position
        self.parking_lot_coor = parking_lot_coor  # there are other empty lots, keep them in a list

    def get_number_of_states(self):
        return self.size * self.size * 2  # multiply by 2 to add status of parked or not

    def get_state(self):
        # print(self.position)
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
                return -100, False
            elif x == 5 or x == 11: # go in the true direction
                self.position = (x, y + 1)
                return -20, False
            elif (x, y) == (0, 7) or (x, y) == (0, 12): # go in the true direction
                self.position = (x, y + 1)
                return -20, False
            else:
                return -100, False # penalize for out of road

        elif action == 1:  # up
            if y == 0: # penalize for out of canvas
                return -100, False
            elif x == 6 or x == 12: # go in the true direction
                self.position = (x, y - 1)
                return -20, False
            elif (x, y) == (self.size - 1, 8) or (x, y) == (self.size - 1, 13): # go in the true direction
                self.position = (x, y - 1)
                return -20, False
            else:
                return -100, False # penalize for out of road

        elif action == 2:  # left
            if x == 0: # penalize for out of canvas
                return -100, False
            elif y == 7 or y == 12: # go in the true direction
                self.position = (x - 1, y)
                return -20, False
            elif (x, y) == (6, 0) or (x, y) == (12, 0): # go in the true direction
                self.position = (x - 1, y)
                return -20, False
            else:
                return -100, False # penalize for out of road

        elif action == 3:  # right
            if x == self.size - 1: # penalize for out of canvas
                return -100, False
            elif y == 8 or y == 13: # go in the true direction
                self.position = (x + 1, y)
                return -20, False
            elif (x, y) == (5, self.size - 1) or (x, y) == (11, self.size - 1): # go in the true direction
                self.position = (x + 1, y)
                return -20, False
            else:
                return -100, False # penalize for out of road

        elif action == 4:  # park
            if [x, y] not in self.parking_lot_coor: # if it's not a parking lot
                return -100, False
            elif self.target_position == (x, y):
                reward = calc_reward()
                self.parking = True
                return reward + 20, True # yey it's target!!! #calculate -distance + 20 as a reward
            else:
                reward = calc_reward()
                self.parking = True
                return reward, True # no target position but it's a lot #finish the loop #calculate -distance as a reward

"""
###POLICY 6 - FIELD 6######

--Calculate rewards with distance--
Put regular steps reward -10
Put out of the road and wrong direction reward -100
Put parking to the target space reward (minus distance + 20) and finish episode
Put parking to the other empty space reward (minus distance) and finish the episode
"""
class Field_6:
    def __init__(self, size, start_position, target_position, parking_lot_coor):
        self.size = size
        self.parking = False  # true or false, park or not park, start with not park
        self.target_position = target_position  # there is a target position which has high reward
        self.position = start_position  # determine start position
        self.parking_lot_coor = parking_lot_coor  # there are other empty lots, keep them in a list

    def get_number_of_states(self):
        return self.size * self.size * 2  # multiply by 2 to add status of parked or not

    def get_state(self):
        # print(self.position)
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
                return -100, False
            elif x == 5 or x == 11: # go in the true direction
                self.position = (x, y + 1)
                return -10, False
            elif (x, y) == (0, 7) or (x, y) == (0, 12): # go in the true direction
                self.position = (x, y + 1)
                return -10, False
            else:
                return -100, False # penalize for out of road

        elif action == 1:  # up
            if y == 0: # penalize for out of canvas
                return -100, False
            elif x == 6 or x == 12: # go in the true direction
                self.position = (x, y - 1)
                return -10, False
            elif (x, y) == (self.size - 1, 8) or (x, y) == (self.size - 1, 13): # go in the true direction
                self.position = (x, y - 1)
                return -10, False
            else:
                return -100, False # penalize for out of road

        elif action == 2:  # left
            if x == 0: # penalize for out of canvas
                return -100, False
            elif y == 7 or y == 12: # go in the true direction
                self.position = (x - 1, y)
                return -10, False
            elif (x, y) == (6, 0) or (x, y) == (12, 0): # go in the true direction
                self.position = (x - 1, y)
                return -10, False
            else:
                return -100, False # penalize for out of road

        elif action == 3:  # right
            if x == self.size - 1: # penalize for out of canvas
                return -100, False
            elif y == 8 or y == 13: # go in the true direction
                self.position = (x + 1, y)
                return -10, False
            elif (x, y) == (5, self.size - 1) or (x, y) == (11, self.size - 1): # go in the true direction
                self.position = (x + 1, y)
                return -10, False
            else:
                return -100, False # penalize for out of road

        elif action == 4:  # park
            if [x, y] not in self.parking_lot_coor: # if it's not a parking lot
                return -100, False
            elif self.target_position == (x, y):
                reward = calc_reward()
                self.parking = True
                return reward + 20, True # yey it's target!!! #calculate -distance + 20 as a reward
            else:
                reward = calc_reward()
                self.parking = True
                return reward, True # no target position but it's a lot #finish the loop #calculate -distance as a reward

"""
###POLICY 7 - FIELD 7######

--Calculate rewards with distance--
Put regular steps reward -5
Put out of the road and wrong direction reward -100
Put parking to the target space reward (minus distance + 20) and finish episode
Put parking to the other empty space reward (minus distance) and finish the episode
"""
class Field_7:
    def __init__(self, size, start_position, target_position, parking_lot_coor):
        self.size = size
        self.parking = False  # true or false, park or not park, start with not park
        self.target_position = target_position  # there is a target position which has high reward
        self.position = start_position  # determine start position
        self.parking_lot_coor = parking_lot_coor  # there are other empty lots, keep them in a list

    def get_number_of_states(self):
        return self.size * self.size * 2  # multiply by 2 to add status of parked or not

    def get_state(self):
        # print(self.position)
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
                return -100, False
            elif x == 5 or x == 11: # go in the true direction
                self.position = (x, y + 1)
                return -5, False
            elif (x, y) == (0, 7) or (x, y) == (0, 12): # go in the true direction
                self.position = (x, y + 1)
                return -5, False
            else:
                return -100, False # penalize for out of road

        elif action == 1:  # up
            if y == 0: # penalize for out of canvas
                return -100, False
            elif x == 6 or x == 12: # go in the true direction
                self.position = (x, y - 1)
                return -5, False
            elif (x, y) == (self.size - 1, 8) or (x, y) == (self.size - 1, 13): # go in the true direction
                self.position = (x, y - 1)
                return -5, False
            else:
                return -100, False # penalize for out of road

        elif action == 2:  # left
            if x == 0: # penalize for out of canvas
                return -100, False
            elif y == 7 or y == 12: # go in the true direction
                self.position = (x - 1, y)
                return -5, False
            elif (x, y) == (6, 0) or (x, y) == (12, 0): # go in the true direction
                self.position = (x - 1, y)
                return -5, False
            else:
                return -100, False # penalize for out of road

        elif action == 3:  # right
            if x == self.size - 1: # penalize for out of canvas
                return -100, False
            elif y == 8 or y == 13: # go in the true direction
                self.position = (x + 1, y)
                return -5, False
            elif (x, y) == (5, self.size - 1) or (x, y) == (11, self.size - 1): # go in the true direction
                self.position = (x + 1, y)
                return -5, False
            else:
                return -100, False # penalize for out of road

        elif action == 4:  # park
            if [x, y] not in self.parking_lot_coor: # if it's not a parking lot
                return -100, False
            elif self.target_position == (x, y):
                reward = calc_reward()
                self.parking = True
                return reward + 20, True # yey it's target!!! #calculate -distance + 20 as a reward
            else:
                reward = calc_reward()
                self.parking = True
                return reward, True # no target position but it's a lot #finish the loop #calculate -distance as a reward

"""
###POLICY 4 - FIELD 4 with Traffic######

--Calculate rewards with distance--
Put regular steps reward -1
Put steps in the traffic area reward -2
Put out of the road and wrong direction reward -20
Put parking to the target space reward (minus distance + 20) and finish episode
Put parking to the other empty space reward (minus distance) and finish the episode
"""

class Field_4_tr:
    def __init__(self, size, start_position, target_position, parking_lot_coor):
        self.size = size
        self.parking = False  # true or false, park or not park, start with not park
        self.target_position = target_position  # there is a target position which has high reward
        self.position = start_position  # determine start position
        self.parking_lot_coor = parking_lot_coor  # there are other empty lots, keep them in a list

    def get_number_of_states(self):
        return self.size * self.size * 2  # multiply by 2 to add status of parked or not

    def get_state(self):
        # print(self.position)
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
            elif x == 5 or x == 11: # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            elif (x, y) == (0, 7) or (x, y) == (0, 12): # go in the true direction
                self.position = (x, y + 1)
                return -1, False
            else:
                return -20, False # penalize for out of road

        elif action == 1:  # up
            if y == 0: # penalize for out of canvas
                return -20, False
            elif x == 6 or x == 12: # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            elif (x, y) == (self.size - 1, 8) or (x, y) == (self.size - 1, 13): # go in the true direction
                self.position = (x, y - 1)
                return -1, False
            else:
                return -20, False # penalize for out of road

        elif action == 2:  # left
            if x == 0: # penalize for out of canvas
                return -20, False
            elif y == 7: # go in the true direction
                if x in [x for x in range(7,11)]: #there is a TRAFFIC in this part of the road
                    self.position = (x - 1, y)
                    return -2, False # TRAFFIC
                else:
                    self.position = (x - 1, y)
                    return -1, False
            elif y == 12: # go in the true direction
                self.position = (x - 1, y)
                return -1, False
            elif (x, y) == (6, 0) or (x, y) == (12, 0): # go in the true direction
                self.position = (x - 1, y)
                return -1, False
            else:
                return -20, False # penalize for out of road

        elif action == 3:  # right
            if x == self.size - 1: # penalize for out of canvas
                return -20, False
            elif y == 8 or y == 13: # go in the true direction
                self.position = (x + 1, y)
                return -1, False
            elif (x, y) == (5, self.size - 1) or (x, y) == (11, self.size - 1): # go in the true direction
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


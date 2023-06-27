#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#define the shape of environment
environment_rows = 3
environment_columns = 3
states = 6
action_number = 8


# In[3]:


#initialization of Q_values
Q_values = np.zeros((environment_rows,environment_columns,action_number))
print(Q_values)


# In[4]:


#%% define actions
actions = ['N','NE','E','SE','S','SW','W','NW']


# In[5]:


#%% define terminal state
row = {'0':0,'1':0,'2':0,'3':1,'4':1,'5':1}
col = {'0':0,'1':1,'2':2,'3':0,'4':1,'5':2}
terminal_row =row[input(str('Input row_dst nodes;'))]
terminal_column =col[input(str('Input column_dst nodes;'))]

print(terminal_row)
print(terminal_column)


# In[6]:


#สร้างreward
rewards_matrix =np.zeros((states,states))
rewards_matrix[0,:] = np.array([-100,-2,-100,-1,-4,-100])
rewards_matrix[1,:] = np.array([-2,-100,-6,-100,-5,-2])
rewards_matrix[2,:] = np.array([-100,-6,-100,-100,-100,-3])
rewards_matrix[3,:] = np.array([-1,-100,-100,-100,-8,-100])
rewards_matrix[4,:] = np.array([-4,-5,-100,-8,-100,-1])
rewards_matrix[5,:] = np.array([-100,-2,-3,-100,-1,-100])
print(rewards_matrix)


# In[7]:


# checking for terminal state
def is_terminal_state(row_number,column_number):
    if((row_number == terminal_row and column_number == terminal_column) or       (row_number == 2 and column_number == 0) or        (row_number == 2 and column_number == 1) or        (row_number == 2 and column_number == 2)):
        return True
    else:
        return False


# In[8]:


#เลือกตำแหน่งเริม
def start_location():
    current_row_number = np.random.randint(environment_rows) #แถวปัจุบันจะให้หาจำนวนเต็มใน environment_rows
    current_column_number = np.random.randint(environment_columns) #
    while is_terminal_state(current_row_number,current_column_number):
        current_row_number = np.random.randint(environment_rows)
        current_column_number = np.random.randint(environment_columns)    
    return current_row_number,current_column_number


# In[9]:


# choosing next action
def next_action(row_number,column_number,epsilon):
    if(np.random.random() < epsilon):
        return np.argmax(Q_values[row_number,column_number])#หาตำแหน่งที่มากที่สุดในQ_value
    else:
        return np.random.randint(action_number) 


# In[10]:


# getting next location
def next_location(current_row_number,current_column_number,action_index):
    new_row_number = current_row_number
    new_column_number = current_column_number
    if actions[action_index] == 'N' and current_row_number > 0:
        new_row_number -= 1
    elif actions[action_index] == 'E' and current_column_number < environment_columns - 1:
        new_column_number += 1
    elif actions[action_index] == 'S' and current_row_number < environment_rows - 1:
        new_row_number += 1
    elif actions[action_index] == 'W' and current_column_number > 0:
        new_column_number -= 1
    elif actions[action_index] == 'NE' and current_row_number > 0        and current_column_number < environment_columns - 1:
            new_row_number -= 1
            new_column_number += 1
    elif actions[action_index] == 'SE' and current_row_number < environment_rows - 1        and current_column_number < environment_columns - 1:
            new_row_number += 1
            new_column_number += 1
    elif actions[action_index] == 'SW' and current_row_number < environment_rows - 1        and current_column_number > 0:
            new_row_number += 1
            new_column_number -= 1
    elif actions[action_index] == 'NW' and current_row_number > 0        and current_column_number > 0:
            new_row_number -= 1
            new_column_number -= 1
    return new_row_number,new_column_number 


# In[11]:


state_mapping = {(0, 0): '0', (0, 1): '1', (0, 2): '2', (1, 0): '3', (1, 1): '4', (1, 2): '5'}


# In[12]:


def shortest_path(start_row_number ,start_column_number):
    if is_terminal_state(start_row_number, start_column_number):
        return []
    else:
        current_row_number = start_row_number
        current_column_number = start_column_number
        shortest_pathh = []
        shortest_pathh.append(state_mapping[(current_row_number, current_column_number)])
        while not is_terminal_state(current_row_number, current_column_number):
            action_index = next_action(current_row_number, current_column_number, epsilon)
            current_row_number, current_column_number = next_location(current_row_number, current_column_number, action_index)
            shortest_pathh.append(state_mapping[(current_row_number, current_column_number)])
        return shortest_pathh
   


# In[13]:


# defining index from position
def take_reward_matrix_index(row_number,column_number):
    if(row_number == 0 and column_number == 0 ):
        return 0  
    elif(row_number == 0 and column_number == 1):
        return 1 
    elif(row_number == 0 and column_number == 2):
        return 2 
    elif(row_number == 1 and column_number == 0):
        return 3 
    elif(row_number == 1 and column_number == 1):
        return 4 
    elif(row_number == 1 and column_number == 2):
        return 5


# In[14]:


# choosing reward
def take_reward(current_row_number,current_column_number,next_row_number,next_column_number):
    if ((next_row_number == 2 and next_column_number ==0 ) or          (next_row_number == 2 and next_column_number == 1) or              (next_row_number == 2 and next_column_number == 2)):
        return -100
    else:
        return rewards_matrix[take_reward_matrix_index(current_row_number,current_column_number),take_reward_matrix_index(next_row_number,next_column_number)]


# In[15]:


import matplotlib.pyplot as plt

epsilon = 0.9
discount_factor = 0.9
learning_rate = 0.9
num_episodes = 100  # Total number of episodes
rewards_per_episode = []
actions_per_episode = []

for episode in range(num_episodes):
    # Reset total_reward for each episode
    total_reward = 0
    
    # Training phase
    row_number, column_number = start_location()
    actions_taken = []  # List to store actions taken in the current episode
    episode_reward = 0  # Accumulated reward for the current episode
    while not is_terminal_state(row_number, column_number):
        action_index = next_action(row_number, column_number, epsilon)
        actions_taken.append(action_index)  # Append the action taken
        old_row_number = row_number
        old_column_number = column_number
        row_number, column_number = next_location(old_row_number, old_column_number, action_index)
        reward = take_reward(old_row_number, old_column_number, row_number, column_number)
        episode_reward += reward
        old_Q_value = Q_values[old_row_number, old_column_number, action_index]
        temporal_difference = reward + (discount_factor * np.max(Q_values[row_number, column_number])) - old_Q_value
        new_Q_value = old_Q_value + (learning_rate * temporal_difference)
        Q_values[old_row_number, old_column_number, action_index] = new_Q_value
    total_reward += episode_reward
    rewards_per_episode.append(total_reward / (episode + 1))  # Calculate average reward per episode
    actions_per_episode.append(len(actions_taken))  # Append the number of actions taken in the episode
print('Training complete')

# Plot the graph
plt.figure(figsize=(10, 8))
plt.plot(range(num_episodes), rewards_per_episode, color='red')
plt.xlabel('Episode')
plt.ylabel('Average Reward')
plt.title('Average Reward per Episode')
plt.grid(True)  # Add grid lines
plt.show()


# In[16]:


print_mapping ={'0':shortest_path(0,0),
   '1':shortest_path(0,1),
   '2':shortest_path(0,2),
   '3':shortest_path(1,0),
   '4':shortest_path(1,1),
   '5':shortest_path(1,2)}
a = {(1,2):'5',(1,1):'4',(1,0):'3',(0,2):'2',(0,1):'1',(0,0):'0'}

dst = (a[terminal_row,terminal_column])
print("dst node:",dst)
print("Visited nodes =", print_mapping[input("Input src node:")] )


# ##### 

# In[ ]:





# In[ ]:





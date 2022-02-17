# NHL Team Goal Differential
# Source: Rangers


# Gives user direction
input_string = input('Enter NHL Team Goal Differential Value seperated by SPACE ')
print("\n")
user_list = input_string.split()


# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

# Calculating the sum of list elements
print("Total Goals = ", sum(user_list))


# Counter
wins = 0
totalgoals = 0

# Goal Differential Iterations taken from the useres input
for gd in [user_list] :

	# Counter in use
	wins = i + 1


# Displays the users information
print('Games Won: ', wins)
print('Total Goals: ', sum(user_list))
print('Average Goal Differential: ', sum(user_list) / wins)
input('Press ENTER to exit')

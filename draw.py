import matplotlib.pyplot as plt

# Reading data from the uploaded file
file_path = 'data.txt'

# Re-reading and parsing the file with added checks
iters = []
losses = []
times = []

with open(file_path, 'r') as file:
    for line in file:
        # Check if the line is correctly formatted
        if ':' in line and 'iter' in line and 'loss' in line and 'time' in line:
            parts = line.split(':')
            iter_part = parts[0].split(' ')
            iter_value = int(iter_part[1])
            iters.append(iter_value)

            metrics = parts[1].split(',')
            loss_value = float(metrics[0].split(' ')[2])
            losses.append(loss_value)

            time_value = float(metrics[1].split(' ')[2].replace('ms', ''))
            times.append(time_value)

# Plotting the data again
fig, ax1 = plt.subplots()

# Plotting loss on the left y-axis
color = 'tab:red'
ax1.set_xlabel('iter')
ax1.set_ylabel('loss', color=color)
ax1.plot(iters, losses, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Instantiating a second y-axis to plot time
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('time (ms)', color=color)
ax2.plot(iters, times, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # To fit everything nicely
plt.show()


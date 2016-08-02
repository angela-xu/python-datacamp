import numpy as np
import matplotlib.pyplot as plt

run = 1000
walk = 100
all_walks = []
np.random.seed(926)

for i in range(run):
    random_walk = [0]

    for i in range(walk):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)        
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step += 1
        else:
            step += np.random.randint(1, 7)
        if np.random.rand() < 0.001:
            step = 0

        random_walk.append(step)

    all_walks.append(random_walk)

all_walks_np = np.array(all_walks)
all_walks_np_t = np.transpose(all_walks_np)
a = plt.plot(all_walks_np_t)
plt.xlabel('Walk')
plt.ylabel('Step')
plt.title('Random Walk Process - 1000 Simulations')
plt.show(a)
plt.clf()
b = plt.hist(all_walks_np_t[-1])
plt.xlabel('End Step')
plt.ylabel('Frequency')
plt.title('Random Walk Result - 1000 Simulations')
plt.show(b)
plt.clf()

prob = sum(all_walks_np_t[-1])/run
print('Probability is ' + str(round(prob, 2)) + '%')

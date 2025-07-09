from math import exp
import matplotlib.pyplot as plt

# 1.Set up
iterations = 100
initial_temp = 10
iters = list(range(iterations))
tempuratures = [initial_temp / (i + 1) for i in iters]

# 2.Different cost differences
deltas = [0.01,0.1,1.0]

# 3.Compute  and plot Metrapolis criterion 
for d in deltas:
    acceptance_probs = [exp(-d / t) for t in tempuratures]
    plt.plot(iters,acceptance_probs,label=f'∆E = {d:2f}')


# 4.Final plot
plt.title('Metrapolis Acceptance Probability')
plt.xlabel('Iteration')
plt.ylabel('P(accept worse move)')
plt.legend()
plt.grid(True)
plt.show()



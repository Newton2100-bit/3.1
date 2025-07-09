import matplotlib.pyplot as plt

# 1.Total number of iterations
iterations = 100
initial_temp = 10

# 2.Compute tempurature schedule
iters = list(range(iterations))
tempuratures = [initial_temp / (i + 1) for i in iters]

# 3.Plot
plt.plot(iters,tempuratures,color='orange')
plt.title('Tempurature Decay over Iterations')
plt.xlabel("Iterations")
plt.ylabel("Tempurature")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]
y2 = [5, 10, 15, 20, 25]

plt.plot(x, y, label='Line 1')
plt.plot(x, y2, label='Line 2')  # Changed label to 'Line 2' to avoid duplication

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Labeled plot with positioned legend')

# Corrected the legend parameters
plt.legend(loc='upper left', fontsize=12, frameon=False)
plt.show()

import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 15, 7]

# plt.plot(x, y)
# plt.xlabel('X-axis label')
# plt.ylabel('Y-axis label')
# plt.title('Simple Line Plot')
# plt.show()


plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data Points')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Customized Line Plot')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D']
y = [10, 20, 15, 25]

plt.bar(x, y, color='blue')
plt.title("Bar Plot")
plt.xlabel("Category")
plt.ylabel("Values")

plt.show()

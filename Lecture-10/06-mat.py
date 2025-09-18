import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [10,20,15,25,30,28]

plt.plot(x,y, marker='o' , linestyle='-' , color='b')

x = [1, 2, 3, 4, 5, 6]
y = [30,10,25,25,34,40]

plt.plot(x,y, marker='o' , linestyle='-' , color='r')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.grid(True)
plt.show()
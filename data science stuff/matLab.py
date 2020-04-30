import matplotlib.pyplot as plt
import numpy as np
# Part 1
x = np.linspace(0, 5, 11)
y = x ** 2

print(x)
plt.plot(x,y,'b')
plt.show()

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.plot(x, y, 'b')
plt.show()

# subplot divides the current figure into rectangular panes that are numbered rowwise. Each pane contains an axes object. Subsequent plots are output to the current pane
# this will show 3 graphs with the respective data
plt.subplot(1, 3, 1)
plt.xlabel("X Axis")
plt.plot(x,y,'r')
plt.ylabel("Y Axis")
plt.subplot(1,3,3)
plt.plot(x,y,'b')
plt.subplot(1,3,2)
plt.plot(y,x,'r')
plt.show()

# Have different customized graphs
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y,color='red', lw=3, linestyle='--', marker='o', markersize='20', markerfacecolor="yellow", markeredgewidth=3, markeredgecolor='black')
plt.show()

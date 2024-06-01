import matplotlib.pyplot as plt
import numpy as np

# #1 plots
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x,y)
# #use scatter function to draw scatter points.
# #2 plots
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# #color map as cmap
# col=([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
# plt.scatter(x, y)
# plt.colorbar() #it's show color bar
# plt.show()

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
#alpha is used for transperency 
plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()
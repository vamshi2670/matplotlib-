import matplotlib.pyplot as plt
import numpy as np

#bar() function use to draw bar

# x=np.array(['A','B','C','D'])
# y=np.array([10,20,30,50])
# plt.bar(x,y)
# plt.show()

#horzontal bar
# x=np.array(['A','B','C','D'])
# y=np.array([10,60,30,50])
# plt.barh(x,y)
# plt.show()

#color and width

# x=np.array(['A','B','C','D'])
# y=np.array([10,40,2,50])
# plt.bar(x,y,color='red',width=0.4)
# plt.show()

#height

x=np.array(['A','B','C','D'])
y=np.array([10,40,30,50])
plt.bar(x,y,height=0.1)
plt.show()
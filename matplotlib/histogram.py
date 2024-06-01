import matplotlib.pyplot as plt
import numpy as np

#hist() function 
# x=np.random.normal(120,53,290)
# plt.hist(x)
# plt.show()

#pie

# x=np.array([30,45,20,80,100])
# plt.pie(x)
# plt.show()

#lables in pie
# x=np.array([30,45,20,80])
# label=['apple','bannana','oranges','grapes']
# plt.pie(x,labels=label)
# plt.show()

#startangle is defalut 0 degrees.change it's
# x=np.array([30,45,20,80])
# label=['apple','bannana','oranges','grapes']
# plt.pie(x,labels=label,startangle=70)
# plt.show()

#Pull the "Apples" wedge 0.2 from the center of the pie
# x=np.array([30,45,20,80])
# label=['apple','bannana','oranges','grapes']
# plt.pie(x,labels=label,startangle=70,explode=[0.2,0,0,0])
# plt.show()

#To add a list of explanation for each wedge, use the legend() function

x=np.array([30,45,20,80])
label=['apple','bannana','oranges','grapes']
plt.pie(x,labels=label,startangle=70,colors=['r','b','g','y'])
plt.legend(title='fruites')
plt.show()
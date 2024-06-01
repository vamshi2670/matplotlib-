import matplotlib.pyplot as plt
import numpy as np
#create label
#use xlabel(),ylabel() functions to set a label for the x- and y-axis.

# x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.plot(x,y)
# plt.xlabel(" average ")
# plt.ylabel("calories burn")
# plt.show()

#create title
#You can use the loc parameter in title() to position the title.
# 'left', 'right', and 'center'. Default value is 'center'.

# x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.plot(x,y)
# plt.xlabel(" average ")
# plt.ylabel("calories burn")
# plt.title("calories data",loc='right')
# plt.show()

#set font styles to x and y-label and title
#use fontdict=" "
# x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.plot(x,y)
# font1={'family':'arial','color':'yellow','size':20}
# font2={'family':'serif','color':'red','size':20}
# font3={'family':'arial','color':'green','size':20}
# plt.title("calories data",fontdict=font3)
# plt.xlabel(" average ",fontdict=font1)
# plt.ylabel("calories burn",fontdict=font2)
# plt.show()

                            #Grid

# x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.plot(x,y)
# plt.xlabel(" average ")
# plt.ylabel("calories burn")
# plt.title("calories data")
# plt.grid()  #only for x or y grid lines give axis="x" parameter in grid
# plt.show()    

                        #sub plot
#syntax subplot :plt.subplot(row,column,no.of.plot)
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)  # horzontal is (2,1,1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)    #horzontal is (2,1,2)
plt.plot(x,y)
plt.title("INCOME")

#whole title
plt.suptitle("MY SHOP")
plt.show()
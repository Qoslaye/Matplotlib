import matplotlib.pyplot as plt 

x = [1,2,3,4,5] 
y = [10,15,20,25,30]

plt.subplot(1,2,1)
plt.plot(x,y)
plt.grid(True)


plt.subplot(1,2,2)
plt.plot(x,[i**2 for i in y])
plt.grid(True)


# plt.plot(x, y)
# # customaziation the grid 
# plt.grid(color='gray' , linestyle='--', linewidth=0.5 )
plt.show()

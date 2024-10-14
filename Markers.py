import matplotlib.pyplot as plt 
# import numpy as np 

# ypoints = np.array([3,8,1,10])
# plt.plot(ypoints, marker='o') 
# plt.show()

x = [1,2,3,4,5,6]
y = [10,15,20,25,30,20]

plt.plot(x , y , marker='o' , label='Circle')
plt.plot(x , y , marker='s' , label='Square')
plt.plot(x , y , marker='^', label='Triangle')
plt.plot(x , y , marker='*' , label='Star')
plt.xlabel("x-axis label ")
plt.ylabel("y-axis label ")
plt.title("Basic marker types") 
plt.legend()
plt.show()
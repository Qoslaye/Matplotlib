import matplotlib.pyplot as plt 

x = [1,2,3,4,5] 
y = [10,15,25,30,20]

# plt.plot(x,y) 
# plt.show()

plt.plot(x,y , marker='o', linestyle='--' , color='green' , label='My Line')
plt.xlabel('X-axis label ')
plt.ylabel('Y-axis label')
plt.title('Customized line plot ')
plt.legend()
plt.show()
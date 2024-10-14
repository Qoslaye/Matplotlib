import matplotlib.pyplot as plt 

x=[1,2,3,4,5]
y=[10,15,25,30,20]
y2 = [5,10,15,20,25]

plt.plot(x,y, label='Line 1')
plt.plot(x,y,y2 , linestyle='--' , color='green' , label='line 2')
plt.xlabel('x-axis' )
plt.ylabel('y-axis') 
plt.title('Multiple Line on single plot') 
plt.legend()
plt.show()
import matplotlib.pyplot as plt 

x = [2,4,5,7,8] 
y =[10,15,20,25,30] 

# Customaziation the scatter
plt.scatter(x,y , color='red' , marker='o' , s=100 , edgecolors='black')
plt.title('Customized Scatter plot')
plt.xlabel('x-axis label')    
plt.ylabel('y-axis label') 
plt.show()
import matplotlib.pyplot as plt 

catogories = ['Categories A', 'Categories B','Categories C', 'Categories D']
values = [30,45,20,60]

plt.bar(catogories,values , color=['orange', 'pink' , 'skyblue' , 'gray'] , edgecolor='black') 
plt.title('Horizontal Bar Plot') 
plt.xlabel('Values')    
plt.ylabel('Categories') 

plt.show()
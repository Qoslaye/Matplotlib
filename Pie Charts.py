import matplotlib.pyplot as plt 
import numpy as np


y = np.array([35,25,25,15]) 
mylabels = ["apple" , "banana" , "orange" , "dates"]
plt.pie(y, labels=mylabels)
plt.legend() 
plt.show()
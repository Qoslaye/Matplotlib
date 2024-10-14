import matplotlib.pyplot as plt


# import numpy as np

# x = np.random.normal(170,10,250) 
# plt.hist(x)
# plt.show()


# Histogram in real world example

exam_score = [65,75,80,86,90,95,98,92,100]
plt.hist(exam_score, bins=10 , color='green', edgecolor='black')
plt.title('Exam score distribution') 
plt.xlabel('exam scores') 
plt.ylabel('Frequency') 
plt.show()  


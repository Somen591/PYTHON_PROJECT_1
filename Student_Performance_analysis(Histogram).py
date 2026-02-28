import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = [45, 62, 55, 85, 98, 78, 55, 42, 62, 35, 45, 95, 78, 74, 56, 84, 59]
scores_np = np.array(scores)

total_students = np.size(scores)
print(total_students)

print("average scores are : ", np.mean(scores_np) )
print("highest score is : ", np.max(scores_np) )
print("lowest score is : ", np.min(scores_np) )
print("standard subdeviation of students score is :", np.std(scores_np))

low=0
average=0
top=0

for score in scores:
    if score <50:
        low +=1
    elif score <75:
        average +=1
    else:
        top +=1
low_std=low
mid_std=average
top_std=top


print('\n',"those are count of students by categories : ", '\n', "number of below level students are ",low_std,'\n',"number of midium level students are ",mid_std,'\n',"number of top level students are ",top_std)
print("low level students needs most guidance\n mid level students needs more guidance \n top students needs consistancy")
plt.hist(scores,bins=5,edgecolor='black')
plt.title('student score graph')
plt.xlabel('scores')
plt.ylabel('students')
plt.show()

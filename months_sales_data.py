import numpy as np
import matplotlib.pyplot as plt
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

sales = [
    12000, 15000, 18000, 22000, 20000, 24000,
    26000, 23000, 21000, 25000, 27000, 30000
]
print("total sales of this year is :",np.sum(sales))
print("average sales of the year :",np.mean(sales))
print("highest sales of the year :",np.max(sales))
print("lowest sales of the year :",np.min(sales))
max_month = months[np.argmax(sales)]
print("Best performing month:", max_month)
plt.pie(sales,labels=months,autopct='%1.1f%%',)
plt.xlabel("months")
plt.ylabel("sales")
plt.title("month wise yearly sales")
plt.show()

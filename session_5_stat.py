"""
Tasks
1.
Given a list of delivery times (in minutes) for 20 Zomato orders, calculate the 25th, 50th, and 75th percentiles using Python's
numpy.percentile function.
2.
Create a Python script that takes an array of IPL player scores and divides them into quartiles using numpy.quantile. Print the
values for Q1, Q2 (median), and Q3.
3.
Given a list of daily step counts from your fitness app for one month, calculate the Interquartile Range (IQR) in Python and
 explain what it tells you about your activity consistency.<br><br><em><strong>Hint:</strong> IQR = Q3 - Q1</em>
4.
Write a Python function to detect outliers in a list of Swiggy order amounts using the IQR method (any value below Q1 - 1.5*IQR
 or above Q3 + 1.5*IQR). Print the outlier values.
5.
Using matplotlib, create a boxplot of your weekly screen time (in hours) for the past 8 weeks. Label the axes and highlight any
outliers"""

# Task 1 

"""import numpy as np

delivery_times= [12,56,46,89,23,45,56,89,56,87,41,23,58,25,54,24,27,57,59,53]

p25 =np.percentile(delivery_times , 25)
p50 =np.percentile(delivery_times , 50)
p75 =np.percentile(delivery_times , 75)

print("25 percentile:", p25)
print("50 percentile:", p50)
print("75 percentile:", p75)"""

#Task 2 . calculate the Q1 , Q2, Q3

"""import numpy as np

scores =[12, 45, 67, 23, 89, 34, 56, 78, 10, 50, 62, 30]

Q1 = np.quantile(scores , 0.25)
Q2 = np.quantile(scores , 0.50)
Q3 = np.quantile(scores , 0.75)


print("Q1 (25th percentile):", Q1)
print("Q2 (Median):", Q2)
print("Q3 (75th percentile):", Q3)"""

# Task 3 . calculate the IQR
"""import numpy as np

steps = [
        6200, 7000, 7500, 6800, 8000, 7200, 6900, 7600, 8100, 7400,
        6500, 7800, 7300, 7100, 8200, 6700, 7700, 7400, 6900, 8500,
        7200, 7900, 6600, 7500, 7300, 8000, 7100, 7600, 6800, 9000
]

Q1 = np.percentile(steps , 25)
Q3 = np.percentile(steps , 75)

IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:",IQR , "steps" )"""

# Task 4 . calculate the quantile
"""
import numpy as np

def detect_outliers(amounts):
    Q1 = np.percentile(amounts , 25)
    Q3 = np.percentile(amounts , 75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5*IQR
    upper_bound = Q3 - 1.5*IQR
    outliers =[]

    for amount in amounts :
        if amount < lower_bound or amount > upper_bound :
            outliers.append(amount)

    print("Q1" ,Q1)
    print("Q3" , Q3)
    print("IQR" , IQR)
    print("lower_bound", lower_bound)
    print("upper_bound", upper_bound)
    print("outliers" , outliers)

order_amounts = [
    180, 220, 250, 275, 300, 320, 350, 375,
    400, 420, 450, 500, 550, 600, 2500
]

detect_outliers(order_amounts)"""

# Task 5 


import matplotlib.pyplot as plt

screen_time = [20, 22, 24, 23, 25, 26, 24, 45]


plt.boxplot(
    screen_time,
    patch_artist=True,
    flierprops=dict(
        marker='o',
        markerfacecolor='red',
        markersize=8
    )
)
plt.title("Weekly Screen Time Analysis")
plt.xlabel("Screen Time")
plt.ylabel("Hours")

plt.show()




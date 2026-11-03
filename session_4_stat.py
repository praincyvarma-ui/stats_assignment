"""1.Given the daily step counts of a user for the last 7 days as [6500, 7200, 8000, 6000, 9000, 7500, 8200], calculate the range
  of steps and explain what this tells you about the user's activity pattern."""

"""given data = [6500, 7200, 8000, 6000, 9000, 7500, 8200]

range = maximum value - minimum value

range = 9000 - 6000 = 3000 steps 

explaination: The difference between the highest and lowest daily step counts is 3,000 steps. This indicates that the user's
daily activity varies from day to day."""

"""2.For a list of 5 food delivery order amounts on Zomato: [250, 400, 350, 300, 500], write code to compute the variance and 
standard deviation of the order amounts."""

"""import statistics

orders = [250,400,350,300,500]

variance = statistics.variance(orders)
standard_dev = statistics.stdev(orders)

print("variance", variance)
print("standard_deviation",round(standard_dev,2))"""

"""
3.
You have the monthly mobile data usage (in GB) for a user over 6 months: [3.2, 2.8, 3.5, 3.0, 2.9, 3.1]. Calculate the 
coefficient of variation (CV) and interpret whether the user's data usage is consistent or highly variable.<br><br><em><strong>
Hint:</strong> CV = (Standard Deviation / Mean) 100%</em>
4.
Suppose you are analyzing the number of likes on 10 recent Instagram posts: [120, 150, 130, 110, 170, 140, 135, 160, 125, 155].
Compute the standard deviation and compare it with the mean to comment on the consistency of engagement.
5.
Use ChatGPT or any AI tool to generate a small dataset (at least 8 values) representing daily UPI transaction amounts for a week.
Then, calculate the variance and standard deviation of the generated data, and briefly interpret what the results mean for 
spending stability."""

#Task - 3: Monthly mobile data usage (GB) for 6 months and calculate the cv :

"""data_usage = [3.2, 2.8, 3.5, 3.0, 2.9, 3.1]

mean =   total observations
       number of observations

     = 18.5
        6
     = 3.08333

variance  calculate:

calculate tabel:
X          X- mean        (X - mean)2
3.2        0.1167          0.0136
2.8       -0.2833          0.0803
3.5        0.4167          0.1736
3.0       -0.0833          0.0069
2.9       -0.1833          0.0336
3.1        0.0167          0.0003
Total                      0.3083

standard deviation= 
                  SD = (X - mean)2
                           n-1
                     = 0.3083
                         5

                     = 0.06167
                     = 0.2483

cv calculate:

coefficient of variance = standard deviation / mean * 100 
                         
                        =0.2483 / 3.08333 * 100      

                        = 8.0534%"""

"""interpreter = The coefficient of variation is 8.0534%, which indicates that the user's monthly mobile data usage is highly 
consistent and has very little variation. The user consumes almost the same amount of mobile data every month"""

# Task - 4  mean and  standard deviation 
 
"""Instagram posts: [120, 150, 130, 110, 170, 140, 135, 160, 125, 155]
 
 mean =   total post
        number of post

       = 1395
          10
     = 139.5 likes

standard deviation:

 X       X - mean       (X - mean)2
120       -19.5          380.25
150        10.5          110.25
130        -9.5          90.25
110        -29.5         870.25
170        30.5          930.25
140        0.5           0.25
135        -4.5          20.25
160        20.5          420.25
125        -14.5         210.25
155        15.5          240.25
Total                    327.25                                                                                                                                                                                                                                                                     

     SD = (X - mean)2
            n-1
        = 327.25
           9
        = 363.611
        = 19.07%

Compare Mean and Standard Deviation

 Mean = 139.5 likes

 Standard Deviation = 19.07 likes

Standard deviation is relatively small compared to the mean.

For additional comparison:

         cv = standard deviation/ mean*100
             13.67
"""

# Task - 5 

"""Let's generate 8 UPI transaction amounts for one week. Some days may have more than one transaction.
AI-generated sample dataset
Transaction	UPI Amount (₹)
1	250   
2	400
3	350
4	300
5	500
6	450
7	250
8	500
Total	3,000

Number of observations (n) = 8
Step 2: Calculate Mean
Formula:

Mean=total amount/ number of amount

=250+400+350+300+500+450+250+500/8
=3000/8
Mean=₹375

Step 3: Calculate Variance
Formula:
Variance=(X - mean)2/n-1

Calculation table:
X 	  X - 375	(X -375)²
250	-125	   15,625
400	 25	   625
350	-25	   625
300	-75	   5,625
500	 125	   15,625
450	 75	   5,625
250	-125	   15,625
500	 125	   15,625
Total		      75,000

Variance=75000/7

Variance=10714.29

Standard Deviation
Formula:

SD=sqrt(Variance)

SD=sqrt(103.51)

SD=₹103.51


Interpretation :
The average UPI transaction amount is ₹375, the variance is 10714.29, and the standard deviation is 103.51. This indicates
that the transaction amounts vary around the average spending amount. The user has moderate variation in daily spending,
which means spending is not completely stable but is also not extremely variable."""
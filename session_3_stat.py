#Task - 1 calculate mean
import numpy as np 

steps = np.array([5000,6000,7500,8000,6500,9000,7000])

mean_steps = np.mean(steps)
print("daily steps counts:", steps)
print("mean steps:", mean_steps)

# Task - 2 write a function to find 

import numpy as np

def find_median(delivery_times):
    return np.median(delivery_times)

times = [20,30,40,50,60,70,80,90,100]

median_time = find_median(times)

print("delivery times:", times)
print("median delivery time:", median_time, "minutes")

# Task-3 find mode

from collections import Counter

genres = [ "music","vlog","music","tech","music","vlog","tech","music","comedy","vlog","music","comedy"]

genre_count = Counter(genres)
mode_genre = genre_count.most_common(1)[0][0]

print("genre frequency:", genre_count)
print("most watched genre:", mode_genre)

# Task-4 calculate mean and median of UPI  transactions

import numpy as np

transactions = np.array([100,120,105,110,5000,115,108])

mean_amount = np.mean(transactions)
median_amount = np.median(transactions)

print("UPI transactions:", transactions)
print("mean UPI transactions:", mean_amount)
print("median UPI transactions:",median_amount)
import statistics
def mean_mode_median(list1):
    return statistics.mean(list1),statistics.mode(list1),statistics.median(list1)

# print(mean_mode_median([4,2,4,5.3]))
a,b,c=(mean_mode_median([7,2,4,1,4]))
print(f"mean is {a}\n mode is {b}\n median is {c}")


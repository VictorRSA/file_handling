#Author:Victor NKuna
#Created:06-November-2020
#Email:victor.nkuna


from matplotlib import  pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import pandas as pd

from random import*
import numpy as np

from scipy import*

def main():

    print("**********Weelcome to numpy program to calculate basic exploratory statistics*********")
    print()
    print("Challenge 1")

    # ask = input("Do you want want to generate random numbers to find the mean,std.dev,and variance of the said data:\n")
    # if ask =="Yes" or ask =="yes":
    N=20
    random_num  = np.arange(0,20)

    average_mean = np.mean(random_num)
    std_dev = np.std(random_num)

    variation = np.var(random_num)

    print("The mean is:",average_mean,"and the standard deviation is:",std_dev,"  and lastly the variance of the data is:",variation)

    print()
    print("Challenge 2")

    print()
    print("***************The following program compute the histogram of the generated data in task/challenge 1***************")

    print()

    # nums: [0.5 ,0.7 ,1.0, 1.2 ,1.3 ,2.1]
    # bins = [0,1,2,3]
    plt.title("Histogram of nums against bins")
    nums=[0.5 ,0.7 ,1.0, 1.2 ,1.3 ,2.1]
    bins = [0,1,2,3]

    plt.xlabel("nums")
    plt.ylabel("bins")
    plt.style.use("ggplot")
    plt.hist(nums,bins=4)
    plt.show()
main()

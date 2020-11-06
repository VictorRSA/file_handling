# #created on:05 -November-2020
# #Creator: Victor Nkuna
# #E-mail:victornkuna37@yahoo.com
#
import numpy as np
import pandas as pd
from random import*
from matplotlib import  pyplot as plt


class_one_2020_lifechoices = ["Females","Males"]

data=[8,12]

#creating the plot

fig = plt.figure(figsize=(10,7))
plt.pie(data,labels=class_one_2020_lifechoices)
plt.show()

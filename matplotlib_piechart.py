#created on:03 -November-2020
#Creater: Victor Nkuna
# #E-mail:victornkuna37@gmail.com

import numpy as np
import pandas as pd
from random import*
from matplotlib import  pyplot as plt

#pie chart where the slices will be orded and plotted counter-clockwise

labels = ["Frogs","Hogs","Dogs","Logs"]

sizes = [15,30,45,10]
explode = (0,0.1,0,0)  #only explore the 2nd slice (i.e. Hogs)

fig,ax1 = plt.subplots()

ax1.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%",shadow=True,startangle=90)

ax1.axis("equal") #equal aspect ratio ensures that the pie is drawn as a circle

plt.show()

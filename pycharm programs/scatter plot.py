#created on:03 -November-2020
#Creater: Victor Nkuna
# #E-mail:victor.nkuna@yahoo.com
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt
import numpy as np
from random import*
N=50

X=np.random.rand(N)
Y=np.random.rand(N)
colors =np.random.rand(N)

area = np.pi *(15*np.random.rand(N))**2 #O-15
plt.scatter(X,Y,s=area,c=colors,alpha=0.5)
plt.show()

print()
print()
# X=np.linspace(-np.pi,np.pi,256,endpoint=True)
# C,S =np.cos(X),np.sin(X)
#
# plt.plot(X,C,color="blue",linewidth=2.5,linestyles="solid")
# plt.show()

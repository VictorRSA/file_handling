
#created on:03 -November-2020
#Creater: Victor Nkuna
# #E-ma
from matplotlib import pyplot as plt
from random import*
import numpy as np
#
# girls_ages =[19,21,19,17]
# girls_names =["SKyla","Nadine","Zoe","Lelethu"]
#
# plt.xlabel("Names of Girls")
# plt.ylabel("Ages of girls")
#
# plt.title("Ba graph")
#
# np.plot(girls_ages,girls_names)
#
# plt.show()
X=np.linspace(-np.pi,np.pi,256,endpoint=True)
C,S =np.cos(X),np.sin(X)

plt.plot(X,C,color="blue",linewidth=2.5)
plt.show()

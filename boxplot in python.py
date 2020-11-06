
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from random import*
# n=50
# rand_om = np.random.rand(n)
# colors = np.random.rand(n)
#
# area = np.pi *(15*np.random.rand(n))**2 #O-15

# x=[5,7,6,7,2,17,2,9,4,11,12,9,6]
# y=[99,86,87,88,111,86,]

a=[1.3,3.4,2.3,9.8]
b=[3.5,4.9,1.3,2.2]
c=[9.7,1.5,4.3,0.9,11.2]

data =[a,b,c]

plt.subplot(121)
plt.boxplot(data)
plt.xlabel("Colleges")
plt.ylabel("Scores")
plt.title("Boxplot for colleges")

plt.show()

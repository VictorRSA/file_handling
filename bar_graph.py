import matplotlib.pyplot as plt
cities=['East London', 'Cape Town', 'Kimberley', 'Durban']
rainfall= [140,  200, 120, 157]
x_pos = [i for i, _ in enumerate(cities)] #labels on the x-axis
# twentyfivep=np.percentile(Testmarks, 25)
#labeling and visuals
plt.bar(x_pos, rainfall, color='green')
plt.xlabel("cities")
plt.ylabel("Rainfall in (mm)")
plt.title("Rainfall for the 4 main cities in SA")
plt.xticks(x_pos, cities)
plt.show()

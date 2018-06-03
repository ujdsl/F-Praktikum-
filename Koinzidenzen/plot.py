import numpy as np
import matplotlib.pyplot as plt

filename = "data_511keV.dat"
title = "Winkelkorrelation der Elektron-Positron-Annihilation"
xaxis = "Winkel/°"
yaxis = "Anzahl der Zerfälle"


savetitle = title.replace(" ", "_")

data = np.loadtxt(filename)
distance_data = data[:,0]
angle_data = []
for element in distance_data:
    angle_data.append(np.arcsin(element/635)/2/np.pi*360)    
count_data=data[:,1]
plt.plot(angle_data, count_data)

plt.grid(True)
plt.xlabel(xaxis)
plt.ylabel(yaxis)
plt.title(title)
plt.savefig(savetitle + ".pdf", dpi=300)


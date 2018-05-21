import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
filename = ""
title = "Kernradienbestimmung und Bestimmung des Nukleonenradius"
xaxis = r"Dritte Wurzel Massenzahl $A^{1/3}$"
yaxis = r"Kernradius $R/fm$"


savetitle = title.replace(" ", "_")

#data = np.loadtxt(filename)

masses = [112.4, 27, 207, 55.8, 63.5]
density = [8.65, 2.69, 11.3, 7.87, 8.92]
counts = [10785, 13459, 10714, 7434, 6990]
z0 = 23713
d = 5
n_a = 6.022140857 * 10 ** 23

# calculating the number density:
number_density = []
for i in range(len(masses)):
    number_density.append(density[i] / masses[i] * n_a)

# calculating the errors:
counts_error = []
for count in counts:
    counts_error.append(np.sqrt(count))
z0_error = np.sqrt(z0)
d_error = 0.1

radii = []
for i in range(len(number_density)):
    radii.append(np.sqrt(np.log(z0/counts[i]) / (2*np.pi*d*number_density[i])) * 10**13)

radii_error = []
for i in range(len(radii)):
    radii_error.append(2*radii[i] * (1/(2*d) * d_error 
                                   + 1/(2*z0*np.log(z0/counts[i]) * z0_error
                                   + 1/(2*counts[i]*np.log(z0/counts[i])) * counts_error[i])))  

masses_third_root = []
for mass in masses:
    masses_third_root.append(mass ** (1/3))

plt.errorbar(masses_third_root, radii, yerr=radii_error, ls = "", marker = "o", ms = 3, label = r"Kernradien - Berechnung: $R=\sqrt{\frac{ln(\frac{Z}{Z_0})}{2\pi d N}}$")

# Linear fit:
fit, cov = np.polyfit(masses_third_root, radii, 1, cov=True)
fit_error = np.sqrt(np.diag(cov))
p = np.poly1d(fit)

x = np.linspace(0, 6, 100)


plt.plot(x, p(x), label="Linearer Fit:\n $r_0=$" + str(round(fit[0], 2)) + "$\pm$" + str(round(fit_error[0], 2)) + "$fm$" 
                         + "\n $\lambda_{dB}=$" + str(round(fit[1], 2)) + "$\pm$" + str(round(fit_error[1], 2)) + "$fm$")
print(fit)
print(fit_error)


plt.grid(True)
plt.xlabel(xaxis)
plt.ylabel(yaxis)
plt.title(title, fontsize=14)
plt.legend()
plt.savefig(savetitle + ".pdf", dpi=300)


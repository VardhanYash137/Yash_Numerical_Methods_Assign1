#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h,c,k 

T_cmb = 2.725  

def black_body_spectrum(frequency, temperature):
    return (2 * h *c* frequency**3 ) * (1 / (np.exp((h *c* frequency*100) / (k * temperature)) - 1))*10**26


data=np.loadtxt("CMB monopole spectrum.txt")
frequency=data[:,0]
cmb_flux=data[:,1]
frequency_si = 100*c*data[:,0]    # converting 1/wavelength to frequency in SI unit


# Calculating black body spectrum using Planck's law
bb_spectrum = black_body_spectrum(frequency, T_cmb)


# Plotting the black body spectrum
plt.plot( frequency_si, bb_spectrum, label='Black Body Spectrum (T = 2.725 K)', linestyle = "--", linewidth = 2 )

# Superimpose the CMB flux
plt.plot( frequency_si, cmb_flux, label = 'CMB Flux',linestyle = "dotted", linewidth = 3 )

# Find the wavelength at which the black body spectrum peaks

peak_wavelength_index = np.argmax(bb_spectrum)   # using numpy function argmax()

peak_wavelength = c/frequency_si[peak_wavelength_index] 

print(f"The wavelength at which the black body spectrum peaks is approximately {peak_wavelength:.2e} meters.")

# Add labels and legend

plt.xlabel('Frequency (Hz)')
plt.ylabel('Spectral Radiance (MJy/sr)')
plt.legend()
plt.grid()


# Save the plot to a PDF file
plt.savefig('cmb_spectrum_plot.pdf')

# Show the plot
plt.show()


# In[ ]:





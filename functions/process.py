import numpy as np  
import matplotlib.pyplot as plt  
from numpy.fft import fft, fftshift  
from dictionary import lunar_mission_data

data = np.array(lunar_mission_data['rimfax']['reflection_amplitude']['surface']) #sample with surface data
def noise_filter(data):
    """
        noise filtering with Blackman-Harris Window Function for signal processing and spectral analysis.
    """
    
    window = np.blackman(len(data)) 
  
    plt.figure() 
    
    A = fft(window, 2048) / 25.5
    mag = np.abs(fftshift(A)) 
    freq = np.linspace(-0.5, 0.5, len(A)) 
    response = 20 * np.log10(mag) 
    response = np.clip(response, -100, 100) 
    
    plt.plot(freq, response) 
    plt.title("Frequency response of Blackman window") 
    plt.ylabel("Magnitude [dB]") 
    plt.xlabel("Normalized frequency [cycles per sample]") 
    plt.axis('tight') 
    plt.show()

noise_filter(data)










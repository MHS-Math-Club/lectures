import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter

n = 1000
speed = 0.3
aa = [0]
for i in range(1, n):
    
    t1 = aa[-1] - i
    t2 = aa[-1] + i
    if (t1 > 0) * (t1 not in aa):
        aa.append(t1)
    else:
        aa.append(t2)

def add_to_plot(i):
    # Arc centre and radius.
    c, r = (aa[i+1] + aa[i]) / 2, abs(aa[i+1] - aa[i]) / 2
    x = np.linspace(-r, r, 1000)
    y = np.sqrt(r**2 - x**2) * (-1)**i
    color = plt.colormaps['Spectral'](i/n)
    ax.plot(x+c, y, c=color, lw=1)

# Equal aspect ratio Figure with black background and no axes.
fig, ax = plt.subplots(facecolor='k')
ax.axis('equal')
ax.axis('off')

# Colour the lines sequentially from a Matplotlib colormap.
cm = plt.colormaps['Spectral']

for i in range(0, 66-2):
    add_to_plot(i)

plt.savefig('recaman.png', dpi=300)

def animate(i):
    # Arc centre and radius.
    c, r = (aa[i+1] + aa[i]) / 2, abs(aa[i+1] - aa[i]) / 2
    x = np.linspace(-r, r, 1000)
    y = np.sqrt(r**2 - x**2) * (-1)**i
    color = plt.colormaps['Spectral'](i/n)
    ax.plot(x+c, y, c=color, lw=1)
    
    # Clear the previous text
    for txt in ax.texts:
        txt.set_visible(False)
    # Display the current value of the Recaman sequence
    ax.text(0.05, 0.95, f'Value: {aa[i]}', transform=ax.transAxes, fontsize=12, verticalalignment='top', color='white')

# Equal aspect ratio Figure with black background and no axes.
fig, ax = plt.subplots(facecolor='k')
ax.axis('equal')
ax.axis('off')

ani = animation.FuncAnimation(fig, animate, frames=n-2, interval=50)

# Ensure output directory exists
output_dir = os.path.join(os.path.dirname(__file__), '../../output')
output_dir = r'C:\Users\Dell\Desktop\saddle\recaman\output'
os.makedirs(output_dir, exist_ok=True)

ani.save(os.path.join(output_dir, 'recman.mp4'), writer='ffmpeg', fps=1/speed, dpi=200)

from scipy.io import wavfile
from IPython.display import Audio

def get_piano_freq(n):
    return 2**((n-49)/12) * 440

# # Major Scale
# freqs = np.array([65.41, 73.42, 82.41, 87.31, 98, 110, 123.47, 
#                   130.81, 146.83, 164.81, 174.61, 196, 220, 246.94, 
#                   261.63, 293.66, 329.63, 349.23, 392, 440, 493.88, 523.25, 
#                   587.33, 659.25, 698.46, 783.99, 880, 987.77, 1046.5])

# # Whole Tone Scale
# freqs = np.array([65.41, 73.42, 82.41, 92.5, 103.83, 116.54, 130.81, 
#                   146.83, 164.81, 185, 207.65, 233.08, 261.63, 293.66, 
#                   329.63, 369.99, 415.3, 466.16, 523.25, 587.33, 659.25, 
#                   739.99, 830.61, 932.33, 1046.5])

# # Diminished Scale
# freqs = np.array([get_piano_freq(n) for n in range(40, 80)])


# Pentatonic
freqs = np.array([65.41, 73.42, 82.41, 98, 110, 130.81, 
                  146.83, 164.81, 196, 220, 261.63, 293.66, 329.63,
                  392, 440, 523.25, 587.33, 659.25, 783.99])

# Minor Blues
freqs = np.array([65.41, 77.78, 87.31, 92.5, 98, 116.54, 130.81, 155.56, 
                  174.61, 185, 196, 233.06, 261.63, 311.13, 349.23,
                  369.99, 392, 466.16, 523.25, 622.25, 698.46, 783.99])

# Chromatic
freqs = np.array([get_piano_freq(n) for n in range(40)])
max_freq = 600

sr = 2*4096   # sample rate corresponding to one sec
ns = speed  # length of tone in sec
dd = []
for i in range(n):
    f1 = freqs[aa[i]%len(freqs)]
    x1 = np.linspace(0, ns*2*np.pi*f1, int(ns*sr))
    signal = np.sum(np.array([(1/(1.7)**i) * np.sin(i*x1) for i in range(10)]), axis=0)
    dd.append(signal)
dd = np.array(dd).ravel()
wavfile.write('recaman_chrom.wav', sr, dd.astype('float32'))
Audio('recaman_chrom.wav')



print("created the recman at " + output_dir)


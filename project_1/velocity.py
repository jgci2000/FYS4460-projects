import numpy as np
import matplotlib.pyplot as plt
import os
import imageio
from ase.io import read

file_name = "first_md_sim/dump.lammpstrj"
traj = read(file_name, format="lammps-dump-text", index=":")
print("File read!")
 
n = len(traj)
n_bins = 30
v_min = 0
v_max = 8

v_T = traj[n-1].get_velocities()
v_mod_T = np.sqrt(v_T[:, 0]**2 + v_T[:, 1]**2 + v_T[:, 2]**2)
h_T, bins = np.histogram(v_T[:, 0], bins=n_bins, range=(v_min, v_max))
h_T2 = h_T * h_T

filenames = list()

print("Starting making the gif")
for i, frame in enumerate(traj):
    plt.figure("Distribution of Velocities")
    
    v_t = frame.get_velocities()
    print(v_t[0, 0], v_t[0, 1], v_t[0, 2])
    
    v_mod_t = np.sqrt(v_t[:, 0]**2 + v_t[:, 1]**2 + v_t[:, 2]**2)
    h_t, _ = np.histogram(v_t[:, 0], bins=n_bins, range=(v_min, v_max))
   
    h_norm = np.zeros_like(h_T)
    h_norm[h_T2 != 0] = h_t[h_T2 != 0] * h_T[h_T2 != 0] / h_T2[h_T2 != 0]
    
    # plt.plot(np.linspace(0, 6, 1000), maxwell_velocity(np.linspace(0, 6, 1000), T), '-r', label="Maxwell-Boltzmann Distribution")
    plt.plot(bins[:-1], h_t, '-r', label="Histogram")
    plt.plot(bins[:-1], h_T, '-r', label="Histogram")
    plt.xlabel(r"$v$")
    plt.ylabel(r"$P(v)$")
    plt.xlim(v_min, v_max)
    plt.ylim(0, 0.8)
    plt.legend()

    # create file name and append it to a list
    filename = f'{i}.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.close()
    
    if i > 30:
        exit()

    print(f"{i+1}/{n}", end="\r")

# build gif
with imageio.get_writer('velocity.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
print("Gif done!")
print("Removing files")        
# Remove files
for filename in set(filenames):
    os.remove(filename)

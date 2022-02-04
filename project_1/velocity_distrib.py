import numpy as np
import matplotlib.pyplot as plt
import os
import imageio

file_name = "first_md_sim/dump.lammpstrj"

# frames = [1000, 2000, 3000, 4000, 5000]
frames = [10 * f for f in range(0, 500)]
count = 0

with open(file_name, "r") as file:
    for _ in range(3):
        file.readline()
    
    N = int(file.readline().strip())
    v_x = np.zeros((N, len(frames)))
    v_y = np.zeros((N, len(frames)))
    v_z = np.zeros((N, len(frames)))
    
    for _ in range(5):
        file.readline()
    
    for i in range(N):
        line = file.readline().strip().split()
        v_x[i, 0] = float(line[5])
        v_y[i, 0] = float(line[6])
        v_z[i, 0] = float(line[7])
    
    for line in file:
        try:
            if line.strip() == "ITEM: TIMESTEP" and int(file.readline()) in frames:
                count += 1
                
                for _ in range(7):
                    file.readline()
                    
                for i in range(N):
                    line = file.readline().strip().split()
                    v_x[i, count] = float(line[5])
                    v_y[i, count] = float(line[6])
                    v_z[i, count] = float(line[7])
        except:
            continue

# T = 300
# def maxwell_velocity(v, T):
#     return 4 * np.pi * (1 / (2 * np.pi * T))**(3/2) * v**2 * np.exp(- v**2 / (2 * T))

filenames = list()
for i in range(len(frames)):
    plt.figure("Distribution of Velocities")
    n_bins = 30

    # v
    plt.hist(np.sqrt(v_x[:, i]**2 + v_y[:, i]**2 + v_z[:, i]**2), density=True, bins=n_bins)
    # plt.plot(np.linspace(0, 6, 1000), maxwell_velocity(np.linspace(0, 6, 1000), T), '-r', label="Maxwell-Boltzmann Distribution")
    plt.xlabel(r"$v$")
    plt.ylabel(r"$P(v)$")
    plt.xlim(0, 6)
    plt.ylim(0, 0.8)
    # plt.legend()

    # create file name and append it to a list
    filename = f'{i}.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.close()
    
    print(f"{i+1}/{len(frames)}", end="\r")

# build gif
with imageio.get_writer('velocity.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
        
# Remove files
for filename in set(filenames):
    os.remove(filename)


filenames = list()
for i in range(len(frames)):
    plt.figure("Distribution of Velocities", figsize=(6, 10))
    n_bins = 30

    # vx
    plt.subplot(3, 1, 1)
    plt.hist(v_x[:, i], density=True, bins=n_bins)
    plt.xlabel(r"$v_x$")
    plt.ylabel(r"$P(v_x)$")
    plt.xlim(-5, 5)
    plt.ylim(0, 0.3)

    # vy
    plt.subplot(3, 1, 2)
    plt.hist(v_y[:, i], density=True, bins=n_bins)
    plt.xlabel(r"$v_y$")
    plt.ylabel(r"$P(v_y)$")
    plt.xlim(-5, 5)
    plt.ylim(0, 0.3)

    # vz
    plt.subplot(3, 1, 3)
    plt.hist(v_z[:, i], density=True, bins=n_bins)
    plt.xlabel(r"$v_z$")
    plt.ylabel(r"$P(v_z)$")
    plt.xlim(-5, 5)
    plt.ylim(0, 0.3)

    # create file name and append it to a list
    filename = f'{i}.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.close()
    
    print(f"{i+1}/{len(frames)}", end="\r")

# build gif
with imageio.get_writer('velocity_component.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
        
# Remove files
for filename in set(filenames):
    os.remove(filename)


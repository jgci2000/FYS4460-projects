import numpy as np
import matplotlib.pyplot as plt
import lammps_logfile as lf
import subprocess

T_vals = np.linspace(0, 25, 25)
n_measure = 101

T = np.zeros((len(T_vals), n_measure))
E = np.zeros((len(T_vals), n_measure))
t = np.zeros((len(T_vals), n_measure))
P = np.zeros((len(T_vals), n_measure))

for i, T_in in enumerate(T_vals):
    p_name = "lmp_serial -in in.simple_md -v T %.10f -v i %i" % (T_in, i+1)
    lammps = subprocess.Popen(p_name.split(" "))
    lammps.wait()
    
    file = lf.File("log.lammps")
    t[i, :] = file.get("Time")
    T[i, :] = file.get("Temp")
    E[i, :] = file.get("TotEng")
    P[i, :] = file.get("Press")
    
    print(f"done {i+1}/{len(T_vals)}")

plt.figure("P vs T")
plt.plot(np.mean(T[:, :-10], axis=1), np.mean(P[:, :-10], axis=1), 'o-b')
plt.xlabel(r"$T$")
plt.ylabel(r"$P$")
plt.show()

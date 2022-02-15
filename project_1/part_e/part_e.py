import numpy as np
import matplotlib.pyplot as plt
import lammps_logfile as lf
import subprocess

n_T = 10
n_a = 10
T_vals = np.linspace(0, 25, n_T)
a_vals = np.linspace(0.001, 1, n_a)
n_measure = 51

# P = np.zeros((n_T, n_a))
# T = np.zeros((n_T, n_a))
# rho = np.zeros((n_T, n_a))

for i, T_in in enumerate(T_vals):
    for j, a_in in enumerate(a_vals):
        # T_tmp = np.zeros(n_measure)
        # P_tmp = np.zeros(n_measure)
        # rho_tmp = np.zeros(n_measure)
        
        p_name = "lmp_serial -in in.myfirstmd -v T %.10f -v a %.10f" % (T_in, a_in)
        # print(p_name)
        lammps = subprocess.Popen(p_name.split(" "))
        lammps.wait()
        
        # file = lf.File("log.lammps")
        # T_tmp = file.get("Temp")
        # rho_tmp = file.get("Density")
        # P_tmp = file.get("Press")
        
        # P[i, j] = np.mean(P_tmp[:-10])
        # T[i, j] = np.mean(T_tmp[:-10])
        # rho[i, j] = np.mean(rho_tmp[:-10])
        
#     print(f"done T:{i+1}/{len(T_vals)}")

# plt.figure("density vs T & P")
# plt.contourf(T, rho, P)
# plt.colorbar()
# plt.xlabel(r"$T$")
# plt.ylabel(r"$\rho$")
# # plt.show()
# plt.savefig("desity_T_P_diagram.pdf")

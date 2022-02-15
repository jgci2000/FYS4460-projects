import numpy as np
import matplotlib.pyplot as plt
import lammps_logfile as lf
import subprocess

dt_vals = np.power(10.0, np.array([-1.8, -2, -3, -4, -5, -6]))
# n_measure = 1001

# T = np.zeros((len(dt_vals), n_measure))
# E = np.zeros((len(dt_vals), n_measure))
# t = np.zeros((len(dt_vals), n_measure))

for i, dt in enumerate(dt_vals):
    p_name = "lmp_serial -in in.simple_md -v dt %.10f -v exp %i" % (dt, int(- np.log10(dt)))
    lammps = subprocess.Popen(p_name.split(" "))
    lammps.wait()
    
    # file = lf.File("log.lammps")
    # t[i, :] = file.get("Time")
    # T[i, :] = file.get("Temp")
    # E[i, :] = file.get("TotEng")
    
#     plt.figure("T vs t")
    
#     plt.plot(t[i, :], T[i, :], label=f"dt={int(np.log10(dt))}")
#     plt.xlabel(r"$t$")
#     plt.ylabel(r"$T$")
#     plt.legend()
    
#     print(f"done {i+1}/{len(dt_vals)}")

# plt.figure("T vs dt")

# plt.errorbar(np.log10(dt_vals), np.mean(T, axis=1), yerr=np.std(T, axis=1))
# plt.xlabel(r"$dt$")
# plt.ylabel(r"$\langle T \rangle$")

# plt.show()


    
    



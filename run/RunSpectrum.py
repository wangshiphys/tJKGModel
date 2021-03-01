import logging
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from Spectrum import SpectrumSolver
from kpoints import KPoints

num1 = 4
num2 = 6
eta = 0.05
excitation = "Sm"
direction = sys.argv[1]
alpha = float(sys.argv[2])
beta = float(sys.argv[3])

log_file_name = "Spectrum_num1={0}_num2={1}_direction={2}_alpha={3:.4f}" \
                "_beta={4:.4f}.log".format(num1, num2, direction, alpha, beta)
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    level=logging.INFO-5, filename=log_file_name,
)
logging.info("Program start running")

step = 0.005
omegas = np.arange(-0.1, 5.0, step)
M_INV, cell_bs, ids = KPoints(direction)
kpoints_num = len(ids)
kpoints = np.array([np.dot(np.dot(M_INV, [i, j]), cell_bs) for i, j in ids])

solver = SpectrumSolver(num1=num1, num2=num2, direction=direction)
spectrum = solver.ExcitationSpectrum(
    kpoints, omegas, excitation=excitation, eta=eta, alpha=alpha, beta=beta,
)

data_path = "data/QuantumSpinModel/Spectrum/"
Path(data_path).mkdir(exist_ok=True, parents=True)
template = "Spectrum_num1={0}_num2={1}_direction={2}" \
           "_alpha={3:.4f}_beta={4:.4f}_excitation={5}.npz"
data_name = template.format(num1, num2, direction, alpha, beta, excitation)

np.savez_compressed(
    data_path + data_name,
    size=[num1, num2], direction=[direction], eta=eta,
    parameters=[alpha, beta], excitation=[excitation],
    kpoint_ids=ids, kpoints=kpoints, omegas=omegas, spectrum=spectrum,
)

fig, ax = plt.subplots()
cs = ax.contourf(range(kpoints_num), omegas, spectrum, cmap="hot", levels=500)
fig.colorbar(cs, ax=ax)

ax.set_xticks(range(kpoints_num))
ax.set_xticklabels(["({0},{1})".format(i, j) for i, j in ids], rotation=45)
ax.grid(True, ls="dashed", color="gray")

fig.set_size_inches(8, 4)
plt.tight_layout()
fig.savefig(data_path + data_name.replace("npz", "png"), dpi=100)
plt.close("all")

logging.info("Program stop running")

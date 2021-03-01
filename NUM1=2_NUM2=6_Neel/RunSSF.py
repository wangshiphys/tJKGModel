import matplotlib.pyplot as plt
import numpy as np
from HamiltonianPy import TRIANGLE_CELL_KS

from StructureFactor import QuantumSpinStructureFactor
from utilities import TriangularLattice

ES_DATA_PATH = "data/QuantumSpinModel/ES/"
ES_DATA_NAME_TEMP = "ES_Triangle12_alpha={0:.4f}_beta={1:.4f}.npz"

step = 0.01
ratios = np.arange(-0.7, 0.7 + step, step)
kpoints = np.matmul(
    np.stack(np.meshgrid(ratios, ratios, indexing="ij"), axis=-1),
    4 * np.pi * np.identity(2) / np.sqrt(3)
)
BZBoundary = TRIANGLE_CELL_KS[[*range(6), 0]]

alpha = 0.50
beta = 1.50
points = TriangularLattice().cluster.points
es_data_name = ES_DATA_NAME_TEMP.format(alpha, beta)

with np.load(ES_DATA_PATH + es_data_name) as ld:
    gs_ket = ld["vectors"][:, 0]

factors = QuantumSpinStructureFactor(kpoints, points, gs_ket)
assert np.all(np.abs(factors.imag) < 1E-12)
factors = factors.real

fig, ax = plt.subplots()
im = ax.pcolormesh(
    kpoints[:, :, 0], kpoints[:, :, 1], factors, zorder=0,
    cmap="magma", shading="gouraud",
)
fig.colorbar(im, ax=ax)
ax.plot(
    BZBoundary[:, 0], BZBoundary[:, 1], zorder=1,
    lw=3, ls="dashed", color="tab:blue", alpha=1.0,
)
title = r"$\alpha={0:.4f}\pi,\beta={1:.4f}\pi$".format(alpha, beta)
ax.set_title(title, fontsize="xx-large")

ticks = np.array([-1, 0, 1])
ax.set_xticks(ticks * np.pi)
ax.set_yticks(ticks * np.pi)
ax.set_xticklabels(["{0}".format(tick) for tick in ticks])
ax.set_yticklabels(["{0}".format(tick) for tick in ticks])
ax.set_xlabel(r"$k_x/\pi$", fontsize="x-large")
ax.set_ylabel(r"$k_y/\pi$", fontsize="x-large")
ax.grid(True, ls="dashed", color="gray")
ax.set_aspect("equal")

plt.get_current_fig_manager().window.showMaximized()
plt.tight_layout()
plt.show()
plt.close("all")

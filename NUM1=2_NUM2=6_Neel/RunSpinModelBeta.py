import logging
import sys

import matplotlib.pyplot as plt
import numpy as np

from SpinModel import JKGModelEDSolver
from utilities import derivation

logging.basicConfig(
    stream=sys.stdout, level=logging.INFO, format="%(asctime)s - %(message)s"
)

beta = 0.0
a = np.arange(-0.05, 0.4, 5E-3)
b = np.arange(0.4, 0.72, 1E-3)
c = np.arange(0.72, 0.83, 1E-1)
d = np.arange(0.83, 1.001, 1E-3)
alphas = np.concatenate([a, b, c, d])

# beta = 0.5
# alphas = np.arange(0, 1.001, 0.001)

# beta = 1.5
# alphas = np.arange(0, 1.001, 0.001)

solver = JKGModelEDSolver()
for alpha in alphas:
    solver.EigenStates(alpha=alpha, beta=beta)

gses = []
params = []
es_path = "data/QuantumSpinModel/ES/"
es_name_temp = "ES_Triangle12_alpha={0:.4f}_beta={1:.4f}.npz"
for alpha in alphas:
    es_full_name = es_path + es_name_temp.format(alpha, beta)
    with np.load(es_full_name) as ld:
        gses.append(ld["values"][0])
        params.append(ld["parameters"][0])
gses = np.array(gses, dtype=np.float64)
params = np.array(params, dtype=np.float64)
d2params, d2gses = derivation(params, gses, nth=2)
# np.savez(
#     "data/GEs_Triangle12_beta={0:.4f}.npz".format(beta),
#     params=params, gses=gses, d2params=d2params, d2gses=d2gses,
# )

color_gses = "tab:blue"
color_d2gses = "tab:orange"
fig, ax_gses = plt.subplots()
ax_d2gses = ax_gses.twinx()
ax_gses.plot(params, gses, color=color_gses)
ax_d2gses.plot(d2params, -d2gses / (np.pi ** 2), color=color_d2gses)

ax_gses.set_xlim(params[0], params[-1])
ax_gses.set_title(r"$\beta={0:.4f}\pi$".format(beta), fontsize="xx-large")
ax_gses.set_xlabel(r"$\alpha/\pi$", fontsize="xx-large")
ax_gses.set_ylabel("E", rotation=0, fontsize="xx-large", color=color_gses)
ax_gses.tick_params("y", colors=color_gses)
ax_gses.grid(ls="dashed", axis="x", color="gray")
ax_gses.grid(ls="dashed", axis="y", color=color_gses)

ax_d2gses.set_ylabel(
    r"$E^{''}$", rotation=0, fontsize="xx-large", color=color_d2gses
)
ax_d2gses.tick_params("y", colors=color_d2gses)
plt.get_current_fig_manager().window.showMaximized()
plt.show()
plt.close("all")

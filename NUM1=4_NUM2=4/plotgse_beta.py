import matplotlib.pyplot as plt
import numpy as np

from utilities import derivation

root = "data/GE/"
name_temp = "GE_num1=4_num2=4_direction=xy_alpha={0:.4f}_beta={1:.4f}.npz"

step = 0.001
beta = 0.0
alphas = np.arange(0, 1 + step, step)

gses = []
params = []
for alpha in alphas:
    full_name = root + name_temp.format(alpha, beta)
    try:
        with np.load(full_name) as ld:
            gses.append(ld["values"][0])
            params.append(ld["parameters"][0])
    except FileNotFoundError:
        pass

gses = np.array(gses, dtype=np.float64)
params = np.array(params, dtype=np.float64)
d2params, d2gses = derivation(params, gses, nth=2)

color_gses = "tab:blue"
color_d2gses = "tab:orange"
fig, ax_gses = plt.subplots()
ax_d2gses = ax_gses.twinx()
ax_gses.plot(params, gses, color=color_gses)
ax_d2gses.plot(d2params, -d2gses / (np.pi ** 2), color=color_d2gses)

ax_gses.set_xlim(params[0], params[-1])
ax_gses.set_title(r"$\beta={0:.3f}\pi$".format(beta), fontsize="xx-large")
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
plt.tight_layout()
plt.show()
plt.close("all")

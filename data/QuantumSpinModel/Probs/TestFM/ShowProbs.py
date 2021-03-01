import matplotlib.pyplot as plt
import numpy as np


beta = 1.30
alpha = 0.30
direction = "avg"
ps_name_temp = "PS_num1=4_num2=6_direction={0}_alpha={1:.4f}_beta={2:.4f}.npz"
ps_data_name = "data/" + ps_name_temp.format(direction, alpha, beta)
with np.load(ps_data_name) as ld:
    phis = ld["phis"]
    thetas = ld["thetas"]
    probabilities = ld["probabilities"]

fig, ax = plt.subplots()
cs = ax.pcolormesh(
    phis / np.pi, thetas / np.pi, probabilities,
    zorder=0, cmap="magma", shading="gouraud",
)
colorbar = fig.colorbar(cs, ax=ax)

ax.grid(True, ls="dashed", color="gray")
ax.set_yticks([0.0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0])
ax.set_xticks([0.0, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00])
title = r"$\alpha={0:.2f}\pi,\beta={1:.2f}\pi,direction={2}$".format(
    alpha, beta, direction
)
ax.set_title(title, fontsize="xx-large")
plt.get_current_fig_manager().window.showMaximized()
plt.tight_layout()
plt.show()
plt.close("all")

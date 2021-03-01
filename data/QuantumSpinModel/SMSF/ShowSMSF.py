import matplotlib.pyplot as plt
import numpy as np


alpha = 0.30
beta =  1.30
direction = "avg"
SF_NAME_TEMP = "SF_num1=4_num2=6_direction={0}_alpha={1:.4f}_beta={2:.4f}.npz"

sf_data_name = "data/" + SF_NAME_TEMP.format(direction, alpha, beta)
with np.load(sf_data_name) as ld:
    kpoints = ld["kpoints"]
    factors = ld["factors"]
    BZBoundary = ld["BZBoundary"]

fig, ax = plt.subplots(num=sf_data_name[:-4])
im = ax.pcolormesh(
    kpoints[:, :, 0], kpoints[:, :, 1], factors, zorder=0,
    cmap="magma", shading="gouraud",
)
fig.colorbar(im, ax=ax)
ax.plot(
    BZBoundary[:, 0], BZBoundary[:, 1], zorder=1,
    lw=3, ls="dashed", color="tab:blue", alpha=1.0,
)

title = r"$\alpha={0:.4f}\pi,\beta={1:.4f}\pi$, direction={2}".format(
    alpha, beta, direction
)
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

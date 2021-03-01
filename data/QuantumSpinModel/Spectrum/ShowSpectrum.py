import matplotlib.pyplot as plt
import numpy as np

beta = 0.10
alpha = 0.05
direction = "xy"
title = r"$\alpha={0:.2f}\pi, \beta={1:.2f}\pi$".format(alpha, beta)
spectrum_data_name = "data/Spectrum_num1=4_num2=6_direction={0}_alpha={1:.4f}" \
            "_beta={2:.4f}_excitation=Sm.npz".format(direction, alpha, beta)

with np.load(spectrum_data_name) as ld:
    omegas = ld["omegas"]
    ids = ld["kpoint_ids"]
    spectrum = ld["spectrum"]
kpoint_num = ids.shape[0]

fig, ax = plt.subplots()
im = ax.pcolormesh(
    range(kpoint_num + 1), omegas, spectrum,
    cmap="hot", edgecolors="face",
    # vmin=0, vmax=2,
)
ax.set_ylim(0, 5)
im.set_edgecolor("face")
fig.colorbar(im, ax=ax, pad=0.01)
ax.set_title(title, fontsize="xx-large")
ax.set_xticks(np.arange(kpoint_num) + 0.5)
ax.grid(axis="both", ls="dashed", color="gray")
xtick_labels = ["({0},{1})".format(i, j) for i, j in ids]
ax.set_xticklabels(xtick_labels, fontsize="xx-large", rotation=45)

plt.get_current_fig_manager().window.showMaximized()
plt.tight_layout()
plt.show()
plt.close("all")

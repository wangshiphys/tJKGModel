import matplotlib.pyplot as plt
import numpy as np

from utilities import derivation

root = "data/GE/"
name_temp = "GE_num1=4_num2=4_direction=xy_alpha={0:.4f}_beta={1:.4f}.npz"

alpha = 0.30
a = np.arange(0, 0.8, 0.005)
b = np.arange(0.8, 2, 0.01)
betas = np.concatenate([a, b])

# alpha = 0.50
# betas = np.arange(0, 2.001, 0.001)

# alpha = 0.75
# a = np.arange(0, 0.6, 0.005)
# b = np.arange(0.6, 0.86, 0.04)
# c = np.arange(0.86, 2.005, 0.005)
# betas = np.concatenate([a, b, c])

gses = []
params = []
for beta in betas:
    full_name = root + name_temp.format(alpha, beta)
    try:
        with np.load(full_name) as ld:
            gses.append(ld["values"][0])
            params.append(ld["parameters"][1])
    except FileNotFoundError:
        pass
gses = np.array(gses, dtype=np.float64) / (4 * 4)
params = np.array(params, dtype=np.float64)
d2params, d2gses = derivation(params, gses, nth=2)
# np.savez(
#     "data/GEs_num1=4_num2=4_alpha={0:.3f}.npz".format(alpha),
#     gses=gses, params=params, d2gses=d2gses, d2params=d2params,
# )

font_size = 16
line_width = 10
color_gses = "tab:blue"
color_d2gses = "tab:red"
fig, ax_gses = plt.subplots()
ax_d2gses = ax_gses.twinx()
ax_gses.plot(params, gses, lw=4, color=color_gses)
ax_d2gses.plot(d2params, -d2gses / (np.pi ** 2), lw=4, color=color_d2gses)

ax_gses.set_xlim(params[0], params[-1])
ax_gses.set_xlabel(r"$\beta/\pi$", fontsize=font_size+5)
ax_gses.set_ylabel(
    "$E$", y=0.4, rotation=0, fontsize=font_size+5, color=color_gses
)
ax_d2gses.set_ylabel(
    r"-$\frac{d^2E}{d\beta^2}$", y=0.65,
    rotation=0, fontsize=font_size+5, color=color_d2gses
)
ax_gses.tick_params("x", colors="black", labelsize=font_size)
ax_gses.tick_params("y", colors=color_gses, labelsize=font_size)
ax_d2gses.tick_params("y", colors=color_d2gses, labelsize=font_size)
ax_d2gses.tick_params("y", colors=color_d2gses)
plt.tight_layout()
plt.show()
plt.close("all")

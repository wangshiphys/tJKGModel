import matplotlib.pyplot as plt
import numpy as np

from FontSize import *

line_width = 4
color_gses = "tab:blue"
color_d2gses = "tab:red"


names = [
    "data/GEs_Triangle12_alpha=0.0500.npz",
    "data/GEs_Triangle12_alpha=0.2000.npz",
    "data/GEs_Triangle12_alpha=0.7500.npz",
    "data/GEs_Triangle12_beta=0.0000.npz",
    "data/GEs_Triangle12_beta=0.5000.npz",
    "data/GEs_Triangle12_beta=1.5000.npz",
]
container = []
for name in names:
    with np.load(name) as ld:
        gses = ld["gses"]
        d2gses = ld["d2gses"]
        params = ld["params"]
        d2params = ld["d2params"]
    container.append((params, gses, d2params, d2gses))

fig, axes_gses = plt.subplots(2, 3)

axes_d2gses = []
axes_gses = axes_gses.reshape((-1,))
sub_fig_tags = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)"]
for index in range(len(names)):
    ax_gses = axes_gses[index]
    sub_fig_tag = sub_fig_tags[index]
    params, gses, d2params, d2gses = container[index]

    ax_d2gses = ax_gses.twinx()
    axes_d2gses.append(ax_d2gses)

    ax_gses.plot(params, gses, lw=line_width, color=color_gses)
    ax_d2gses.plot(
        d2params, -d2gses / (np.pi ** 2), lw=line_width, color=color_d2gses
    )
    ax_gses.text(
        0.76, 0.98, sub_fig_tag,
        ha="center", va="top", fontsize=XXLARGE+10, transform=ax_gses.transAxes
    )
    if index < 3:
        ax_gses.set_xlabel(r"$\beta/\pi$", fontsize=XXLARGE)
    else:
        ax_gses.set_xlabel(r"$\alpha/\pi$", fontsize=XXLARGE)
    ax_gses.tick_params("x", labelsize=XLARGE, length=8, color="black")
    ax_gses.tick_params("y", labelsize=XLARGE, length=8, colors=color_gses)
    ax_d2gses.tick_params("y", labelsize=XLARGE, length=8, colors=color_d2gses)

axes_gses[0].set_xlim(-0.5, 1.5)
axes_gses[0].set_ylim(-6.1, -4.4)
axes_d2gses[0].set_ylim(-3, 19)
axes_gses[0].set_xticks([-0.5, 0.0, 0.5, 1.0, 1.5])
axes_gses[0].set_xticklabels(["-0.5", "0.0", "0.5", "1.0", "1.5"])
axes_gses[0].set_yticks([-6.0, -5.5, -5.0, -4.5])
axes_gses[0].set_yticklabels(["-6.0", "-5.5", "-5.0", "-4.5"])
axes_d2gses[0].set_yticks([0, 5, 10, 15])
axes_d2gses[0].set_yticklabels(["0", "5", "10", "15"])

axes_gses[1].set_xlim(0, 2.1)
axes_gses[1].set_ylim(-9.5, -3.0)
axes_d2gses[1].set_ylim(-7, 39)
axes_gses[1].set_xticks([0.0, 0.5, 1.0, 1.5, 2.0])
axes_gses[1].set_xticklabels(["0.0", "0.5", "1.0", "1.5", "2.0"])
axes_gses[1].set_yticks([-9, -7, -5,])
axes_gses[1].set_yticklabels(["-9", "-7", "-5"])
axes_d2gses[1].set_yticks([0, 10, 20, 30])
axes_d2gses[1].set_yticklabels(["0", "1", "2", "3"])
axes_d2gses[1].text(
    1, 1, r"$\times 10$", ha="left", va="bottom",
    color=color_d2gses, fontsize=LARGE, transform=axes_d2gses[1].transAxes
)

axes_gses[2].set_xlim(0, 2)
axes_gses[2].set_ylim(-12.0, -4.0)
axes_d2gses[2].set_ylim(-20, 330)
axes_gses[2].set_xticks([0.0, 0.5, 1.0, 1.5, 2.0])
axes_gses[2].set_xticklabels(["0.0", "0.5", "1.0", "1.5", "2.0"])
axes_gses[2].set_yticks([-10, -8, -6])
axes_gses[2].set_yticklabels(["-10", "-8", "-6"])
axes_d2gses[2].set_yticks([0, 100, 200, 300])
axes_d2gses[2].set_yticklabels(["0", "1", "2", "3"])
axes_d2gses[2].text(
    1, 1, r"$\times 10^2$", ha="left", va="bottom",
    color=color_d2gses, fontsize=LARGE, transform=axes_d2gses[2].transAxes
)

axes_gses[3].set_xlim(-0.05, 1.00)
axes_gses[3].set_ylim(-8.0, -3.0)
axes_d2gses[3].set_ylim(-5, 55)
axes_gses[3].set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
axes_gses[3].set_xticklabels(["0.0", "0.25", "0.5", "0.75", "1.0"])
axes_gses[3].set_yticks([-7, -6, -5, -4])
axes_gses[3].set_yticklabels(["-7", "-6", "-5", "-4"])
axes_d2gses[3].set_yticks([0, 20, 40])
axes_d2gses[3].set_yticklabels(["0", "2", "4"])
axes_d2gses[3].text(
    1, 1, r"$\times 10$", ha="left", va="bottom",
    color=color_d2gses, fontsize=LARGE, transform=axes_d2gses[3].transAxes
)

axes_gses[4].set_xlim(0.2, 0.8)
axes_gses[4].set_ylim(-7.6, -5.3)
axes_d2gses[4].set_ylim(-30, 290)
axes_gses[4].set_xticks([0.2, 0.4, 0.6, 0.8])
axes_gses[4].set_xticklabels(["0.2", "0.4", "0.6", "0.8"])
axes_gses[4].set_yticks([-7, -6])
axes_gses[4].set_yticklabels(["-7", "-6"])
axes_d2gses[4].set_yticks([0, 100, 200])
axes_d2gses[4].set_yticklabels(["0", "1", "2"])
axes_d2gses[4].text(
    1, 1, r"$\times 10^2$", ha="left", va="bottom",
    color=color_d2gses, fontsize=LARGE, transform=axes_d2gses[4].transAxes
)

axes_gses[5].set_xlim(0.2, 0.8)
axes_gses[5].set_ylim(-11.5, -8)
axes_d2gses[5].set_ylim(-150, 3500)
axes_gses[5].set_xticks([0.2, 0.4, 0.6, 0.8])
axes_gses[5].set_xticklabels(["0.2", "0.4", "0.6", "0.8"])
axes_gses[5].set_yticks([-11, -10, -9, -8])
axes_gses[5].set_yticklabels(["-11", "-10", "-9", "-8"])
axes_d2gses[5].set_yticks([0, 1000, 2000, 3000])
axes_d2gses[5].set_yticklabels(["0", "1", "2", "3"])
axes_d2gses[5].text(
    1, 1, r"$\times 10^3$", ha="left", va="bottom",
    color=color_d2gses, fontsize=LARGE, transform=axes_d2gses[5].transAxes
)

axes_gses[0].set_ylabel(
    "$E$", y=0.42, rotation=0, fontsize=XXLARGE, color=color_gses,
)
axes_gses[3].set_ylabel(
    "$E$", y=0.44, rotation=0, fontsize=XXLARGE, color=color_gses
)
axes_d2gses[2].set_ylabel(
    r"-$\frac{\partial^2E}{\partial \beta^2}$", y=0.60,
    color=color_d2gses, fontsize=XXLARGE, rotation=0, labelpad=12
)
axes_d2gses[5].set_ylabel(
    r"-$\frac{\partial^2E}{\partial \alpha^2}$", y=0.55,
    color=color_d2gses, fontsize=XXLARGE, rotation=0, labelpad=12
)

# top=0.949,
# bottom=0.111,
# left=0.059,
# right=0.949,
# hspace=0.35,
# wspace=0.25

plt.show()
print(fig.get_size_inches())
fig.savefig("fig/SecondDerivatives26.pdf", transparent=True)
plt.close("all")

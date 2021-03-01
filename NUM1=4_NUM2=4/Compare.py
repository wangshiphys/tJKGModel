import matplotlib.pyplot as plt
import numpy as np

XLARGE = 24
XXLARGE = 26
line_width = 4
color_gses = "tab:blue"
color_d2gses = "tab:red"

names = [
    "data/Ges_num1=4_num2=6_alpha=0.300.npz",
    "data/Ges_num1=4_num2=6_alpha=0.500.npz",
    "data/Ges_num1=4_num2=6_alpha=0.750.npz",
    "data/Ges_num1=4_num2=4_alpha=0.300.npz",
    "data/Ges_num1=4_num2=4_alpha=0.500.npz",
    "data/Ges_num1=4_num2=4_alpha=0.750.npz",
]

container = []
for name in names:
    with np.load(name) as ld:
        gses = ld["gses"]
        d2gses = ld["d2gses"]
        params = ld["params"]
        d2params = ld["d2params"]
    container.append((params, gses, d2params, d2gses))

fig, axes_gses = plt.subplots(2, 3, sharex="all", sharey="all")
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
    ax_gses.set_xlim(0, 2)
    ax_gses.set_ylim(-0.98, -0.22)
    ax_gses.set_yticks([-0.9, -0.7, -0.5, -0.3])
    ax_gses.set_xticks([0.0, 0.5, 1.0, 1.5, 2.0])
    ax_gses.set_yticklabels(["-0.9", "-0.7", "-0.5", "-0.3"])
    ax_gses.set_xticklabels(["0.0", "0.5", "1.0", "1.5", "2.0"])
    ax_gses.text(
        0.02, 0.98, sub_fig_tag,
        ha="left", va="top", fontsize=XXLARGE+10, transform=ax_gses.transAxes
    )
    if index > 2:
        ax_gses.set_xlabel(r"$\beta/\pi$", fontsize=XXLARGE)
    ax_gses.tick_params("x", labelsize=XLARGE, length=8, color="black")
    ax_gses.tick_params("y", labelsize=XLARGE, length=8, colors=color_gses)
    ax_d2gses.tick_params("y", labelsize=XLARGE, length=8, colors=color_d2gses)

arrowprops = {
    "width": 3,
    "headlength": 15,
    "headwidth": 9,
    "color": "black",
}
axes_d2gses[1].annotate(
    "", (0.234, 0.2), (0.234, 1.2), arrowprops=arrowprops, zorder=1
)
axes_d2gses[1].annotate(
    "", (1.9, 4.5), (1.9, 5.5), arrowprops=arrowprops, zorder=1
)

axes_d2gses[0].set_ylim(-0.9, 3.5)
axes_d2gses[1].set_ylim(-0.9, 7)
axes_d2gses[2].set_ylim(-0.9, 13)
axes_d2gses[3].set_ylim(-0.9, 3.5)
axes_d2gses[4].set_ylim(-0.9, 3.2)
axes_d2gses[5].set_ylim(-0.9, 13)

axes_gses[0].set_ylabel(
    "$E$", y=0.45, rotation=0, fontsize=XXLARGE, color=color_gses,
)
axes_gses[3].set_ylabel(
    "$E$", y=0.45, rotation=0, fontsize=XXLARGE, color=color_gses,
)
axes_d2gses[2].set_ylabel(
    r"-$\frac{\partial^2E}{\partial \beta^2}$", y=0.52,
    color=color_d2gses, fontsize=XXLARGE, rotation=0, labelpad=12
)
axes_d2gses[5].set_ylabel(
    r"-$\frac{\partial^2E}{\partial \beta^2}$", y=0.55,
    color=color_d2gses, fontsize=XXLARGE, rotation=0, labelpad=12
)
plt.get_current_fig_manager().window.showMaximized()
plt.show()
fig.savefig("fig/Compare.pdf", transpaent=True)
plt.close("all")

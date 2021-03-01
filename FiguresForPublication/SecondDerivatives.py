import matplotlib.pyplot as plt
import numpy as np

from FontSize import *

line_width = 4
color_gses = "tab:blue"
color_d2gses = "tab:red"


def derivation(xs, ys, nth=1):
    """
    Calculate the nth derivatives of `ys` versus `xs` discretely.

    The derivatives are calculated using the following formula:
        dy / dx = (ys[i+1] - ys[i]) / (xs[i+1] - xs[i])

    Parameters
    ----------
    xs : 1-D array
        The independent variables.
        `xs` is assumed to be sorted in ascending order and there are no
        identical values in `xs`.
    ys : 1-D array
        The dependent variables.
        `ys` should be of the same length as `xs`.
    nth : int, optional
        The nth derivatives.
        Default: 1.

    Returns
    -------
    xs : 1-D array
        The independent variables.
    ys : 1-D array
        The nth derivatives corresponding to the returned `xs`.
    """

    assert isinstance(nth, int) and nth >= 0
    assert isinstance(xs, np.ndarray) and xs.ndim == 1
    assert isinstance(ys, np.ndarray) and ys.shape == xs.shape

    for i in range(nth):
        ys = (ys[1:] - ys[:-1]) / (xs[1:] - xs[:-1])
        xs = (xs[1:] + xs[:-1]) / 2
    return xs, ys


names = [
    "data/GEs_numx=4_numy=6_alpha=0.0500.npz",
    "data/GEs_numx=4_numy=6_alpha=0.3000.npz",
    # "data/GEs_numx=4_numy=6_alpha=0.5000.npz",
    "data/GEs_numx=4_numy=6_alpha=0.7500.npz",
    "data/GEs_numx=4_numy=6_beta=0.0000.npz",
    "data/GEs_numx=4_numy=6_beta=0.5000.npz",
    # "data/GEs_numx=4_numy=6_beta=0.7500.npz",
    "data/GEs_numx=4_numy=6_beta=1.5000.npz",
]
container = []
for name in names:
    with np.load(name) as ld:
        gses = ld["gses"]
        params = ld["params"]
    d2params, d2gses = derivation(params, gses, nth=2)
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
    ax_d2gses.plot(d2params, -d2gses / (np.pi ** 2), lw=line_width, color=color_d2gses)
    ax_gses.text(
        0.80, 0.98, sub_fig_tag,
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
axes_gses[0].set_ylim(-11.5, -8.5)
axes_d2gses[0].set_ylim(-3, 15)
axes_gses[0].set_xticks([-0.5, 0.0, 0.5, 1.0, 1.5])
axes_gses[0].set_xticklabels(["-0.5", "0.0", "0.5", "1.0", "1.5"])
axes_gses[0].set_yticks([-12, -11, -10, -9])
axes_gses[0].set_yticklabels(["-12", "-11", "-10", "-9"])
axes_d2gses[0].set_yticks([0, 4, 8, 12])
axes_d2gses[0].set_yticklabels(["0", "4", "8", "12"])

axes_gses[1].set_xlim(0, 2)
axes_gses[1].set_ylim(-20.0, -6.0)
axes_d2gses[1].set_ylim(-18, 100)
axes_gses[1].set_xticks([0.0, 0.5, 1.0, 1.5, 2.0])
axes_gses[1].set_xticklabels(["0.0", "0.5", "1.0", "1.5", "2.0"])
axes_gses[1].set_yticks([-20, -15, -10])
axes_gses[1].set_yticklabels(["-20", "-15", "-10"])
axes_d2gses[1].set_yticks([0, 30, 60, 90])
axes_d2gses[1].set_yticklabels(["0", "3", "6", "9"])
axes_d2gses[1].text(
    1, 1, r"$\times 10$", ha="left", va="bottom",
    color=color_d2gses, fontsize=LARGE, transform=axes_d2gses[1].transAxes
)

axes_gses[2].set_xlim(0, 2)
axes_gses[2].set_ylim(-23.0, -9.0)
axes_d2gses[2].set_ylim(-20, 320)
axes_gses[2].set_xticks([0.0, 0.5, 1.0, 1.5, 2.0])
axes_gses[2].set_xticklabels(["0.0", "0.5", "1.0", "1.5", "2.0"])
axes_gses[2].set_yticks([-20, -15, -10])
axes_gses[2].set_yticklabels(["-20", "-15", "-10"])
axes_d2gses[2].set_yticks([0, 100, 200, 300])
axes_d2gses[2].set_yticklabels(["0", "1", "2", "3"])
axes_d2gses[2].text(
    1, 1, r"$\times 10^2$", ha="left", va="bottom",
    color=color_d2gses, fontsize=LARGE, transform=axes_d2gses[2].transAxes
)

axes_gses[3].set_xlim(0, 1)
axes_gses[3].set_ylim(-15, -7.0)
axes_d2gses[3].set_ylim(-12, 90)
axes_gses[3].set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
axes_gses[3].set_xticklabels(["0.0", "0.25", "0.5", "0.75", "1.0"])
axes_gses[3].set_yticks([-14, -12, -10, -8])
axes_gses[3].set_yticklabels(["-14", "-12", "-10", "-8"])
axes_d2gses[3].set_yticks([0, 40, 80])
axes_d2gses[3].set_yticklabels(["0", "4", "8"])
axes_d2gses[3].text(
    1, 1, r"$\times 10$", ha="left", va="bottom",
    color=color_d2gses, fontsize=LARGE, transform=axes_d2gses[3].transAxes
)

# axes_gses[4].set_xlim(0.25, 0.75)
# axes_gses[4].set_xlim(-0.05, 1.05)
axes_gses[4].set_xlim(0.2, 0.8)
axes_gses[4].set_ylim(-14.2, -10)
axes_d2gses[4].set_ylim(-20, 280)
axes_gses[4].set_xticks([0.2, 0.4, 0.6, 0.8])
axes_gses[4].set_xticklabels(["0.2", "0.4", "0.6", "0.8"])
axes_gses[4].set_yticks([-14, -13, -12, -11])
axes_gses[4].set_yticklabels(["-14", "-13", "-12", "-11"])
axes_d2gses[4].set_yticks([0, 100, 200])
axes_d2gses[4].set_yticklabels(["0", "1", "2"])
axes_d2gses[4].text(
    1, 1, r"$\times 10^2$", ha="left", va="bottom",
    color=color_d2gses, fontsize=LARGE, transform=axes_d2gses[4].transAxes
)

# axes_gses[5].set_xlim(0.25, 0.75)
# axes_gses[5].set_xlim(0, 1)
axes_gses[5].set_xlim(0.2, 0.8)
axes_gses[5].set_ylim(-22.5, -16.5)
axes_d2gses[5].set_ylim(-300, 4400)
axes_gses[5].set_xticks([0.2, 0.4, 0.6, 0.8])
axes_gses[5].set_xticklabels(["0.2", "0.4", "0.6", "0.8"])
axes_gses[5].set_yticks([-22, -20, -18])
axes_gses[5].set_yticklabels(["-22", "-20", "-18"])
axes_d2gses[5].set_yticks([0, 1000, 2000, 3000, 4000])
axes_d2gses[5].set_yticklabels(["0", "1", "2", "3", "4"])
axes_d2gses[5].text(
    1, 1, r"$\times 10^3$", ha="left", va="bottom",
    color=color_d2gses, fontsize=LARGE, transform=axes_d2gses[5].transAxes
)

axes_gses[0].set_ylabel(
    "$E$", y=0.36, rotation=0, fontsize=XXLARGE, color=color_gses,
)
axes_gses[3].set_ylabel(
    "$E$", y=0.45, rotation=0, fontsize=XXLARGE, color=color_gses
)
axes_d2gses[2].set_ylabel(
    r"-$\frac{\partial^2E}{\partial \beta^2}$", y=0.60,
    color=color_d2gses, fontsize=XXLARGE, rotation=0, labelpad=22
)
axes_d2gses[5].set_ylabel(
    r"-$\frac{\partial^2E}{\partial \alpha^2}$", y=0.60,
    color=color_d2gses, fontsize=XXLARGE, rotation=0, labelpad=22
)

# top = 0.949,
# bottom = 0.111,
# left = 0.054,
# right = 0.949,
# hspace = 0.35,
# wspace = 0.25

plt.show()
print(fig.get_size_inches())
fig.savefig("figures/SecondDerivatives.pdf", transparent=True)
plt.close("all")

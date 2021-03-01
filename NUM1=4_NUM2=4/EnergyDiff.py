import matplotlib.pyplot as plt
import numpy as np

root44 =  "data/GE/"
root46 = "../data/QuantumSpinModel/GE/"
name_temp44 = "GE_num1=4_num2=4_direction=xy_alpha={0:.4f}_beta={1:.4f}.npz"
name_temp46 = "GE_numx=4_numy=6_alpha={0:.4f}_beta={1:.4f}.npz"

font_size = 25
line_width = 10
alphas = [0.30, 0.50, 0.75]
betas = np.arange(0, 2, 0.01)
sub_fig_tags = ["(a)", "(b)", "(c)"]
fig, axes = plt.subplots(1, 3, sharex="all", sharey="all")
for index in range(3):
    gses44 = []
    gses46 = []
    ax = axes[index]
    alpha = alphas[index]
    sub_fig_tag = sub_fig_tags[index]
    for beta in betas:
        full_name44 = root44 + name_temp44.format(alpha, beta)
        full_name46 = root46 + name_temp46.format(alpha, beta)
        with np.load(full_name44) as ld:
            gses44.append(ld["values"][0] / (4 * 4))
        with np.load(full_name46) as ld:
            gses46.append(ld["gse"][0] / (4 * 6))

    gses44 = np.array(gses44)
    gses46 = np.array(gses46)
    diff = gses44 - gses46
    line1, = ax.plot(betas, gses44, ls="solid", lw=line_width, zorder=2)
    line2, = ax.plot(betas, gses46,  ls="dashed", lw=2*line_width/3, zorder=3)
    line3, = ax.plot(betas, diff, ls="solid", lw=line_width, zorder=0)
    ax.axhline(0, ls="dashed", color="black", lw=line_width/3, zorder=1)
    # ax.grid(axis="y", ls="dashed", color="gray", lw=line_width/3, zorder=1)
    ax.legend(
        [line1, line2, line3],
        [
            r"$E_{4 \times 4}$", r"$E_{4 \times 6}$",
            r"$E_{4 \times 4} - E_{4 \times 6}$"
        ],
        loc="center", bbox_to_anchor=(0.5, 0.78), fontsize=font_size+2,
    )
    ax.set_title(r"$\alpha = {0}\pi$".format(alpha), fontsize=font_size+6)
    ax.set_xlim(0.0, 2.0)
    ax.set_xlabel(r"$\beta / \pi$", fontsize=font_size+2)
    ax.set_xticks([0.0, 0.5, 1.0, 1.5, 2.0])
    ax.tick_params(labelsize=font_size, length=10)
    ax.text(
        0.02, 1.00, sub_fig_tag, ha="left", va="bottom",
        transform=ax.transAxes, fontsize=font_size+6
    )

for beta in [0.25, 0.62, 0.94, 1.87]:
    axes[0].axvline(beta, lw=2, ls="dashed", color="gray", zorder=0)
axes[0].text(
    0.125, -0.67, "STC", va="center", ha="center", fontsize=font_size-2
)
axes[0].text(
    0.435, -0.67, "MS", va="center", ha="center", fontsize=font_size-2
)
axes[0].text(
    0.78, -0.67, "STA", va="center", ha="center", fontsize=font_size-2
)
axes[0].text(
    1.375, -0.67, "FM-B", va="center", ha="center", fontsize=font_size-2
)

for beta in [0.234, 0.64, 1.00, 1.816, 1.900]:
    axes[1].axvline(beta, lw=2, ls="dashed", color="gray", zorder=0)
axes[1].text(
    0.117, -0.67, "STB", va="center", ha="center", fontsize=font_size-2
)
axes[1].text(
    0.437, -0.67, r"120$^\circ$" + "\n" + r"N$\mathsf{\acute e}$el",
    va="center", ha="center", fontsize=font_size-2
)
axes[1].text(
    0.820, -0.67, "STA", va="center", ha="center", fontsize=font_size-2
)
axes[1].text(
    1.40, -0.67, "FM-A", va="center", ha="center", fontsize=font_size-2
)
axes[1].annotate(
    r"Dual N$\mathsf{\acute e}$el", (1.87, -0.70), (1.75, -0.85),
    ha="right", va="center", fontsize=font_size-2,
    arrowprops={
        "arrowstyle": "->", "connectionstyle": "arc3,rad=0.3", "lw":2,
    },
)

for beta in [0.87, 1.89]:
    axes[2].axvline(beta, lw=2, ls="dashed", color="gray", zorder=0)
axes[2].text(
    0.435, -0.67, "STA", va="center", ha="center", fontsize=font_size-2
)
axes[2].text(
    1.38, -0.67, "FM-C", va="center", ha="center", fontsize=font_size-2
)
axes[0].set_ylabel("E", y=0.45, fontsize=font_size+2, rotation=0)
plt.get_current_fig_manager().window.showMaximized()
plt.tight_layout()
plt.show()
fig.savefig("fig/EnergyDiff.pdf", transparent=True)
plt.close("all")

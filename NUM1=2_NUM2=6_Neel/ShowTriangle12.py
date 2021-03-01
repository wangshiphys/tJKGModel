import HamiltonianPy as HP
import matplotlib.pyplot as plt
import numpy as np

from FontSize import *

points = np.array(
    [
        [0.0, 0.0], [1.0, 0.0], [2.0, 0.0],
        [3.0, 0.0], [4.0, 0.0], [5.0, 0.0],
        [0.5, np.sqrt(3) / 2], [1.5, np.sqrt(3) / 2],
        [2.5, np.sqrt(3) / 2], [3.5, np.sqrt(3) / 2],
        [4.5, np.sqrt(3) / 2], [5.5, np.sqrt(3) / 2],
    ], dtype=np.float64
)
vectors = np.array([[6.0, 0.0], [3.0, np.sqrt(3)]], dtype=np.float64)
cell = HP.Lattice(points, vectors)
intra, inter = cell.bonds(nth=1)

ids = [(0, 0), (1, 0), (0, 1), (1, 1)]
points_collection = np.concatenate(
    [np.dot([i, j], vectors) + points for i, j in ids]
)

font_size = 15
line_width = 4
marker_size = 30
colors = plt.get_cmap("tab10")(range(4))
fig, ax = plt.subplots()
for index, point in enumerate(points_collection):
    cell_index = index % 12
    color = colors[index//12]
    ax.plot(
        point[0], point[1], marker="o", ms=marker_size, color=color,
        clip_on=False, zorder=1
    )
    # ax.text(
    #     point[0], point[1],
    #     str(index),
    #     # str(cell_index),
    #     ha="center", va="center", fontsize=font_size, zorder=2
    # )

for bond in intra:
    p0, p1 = bond.endpoints
    for i, j in ids:
        x0, y0 = p0 + np.dot([i, j], vectors)
        x1, y1 = p1 + np.dot([i, j], vectors)
        ax.plot(
            [x0, x1], [y0, y1], ls="solid", lw=line_width,
            color="gray", zorder=0
        )

inter = [
    [8, 24], [9, 24], [9, 25], [10, 25], [10, 26], [11, 26], [11, 27],
    [18, 27], [18, 28], [19, 28], [19, 29], [20, 29], [20, 36], [21, 36],
    [21, 37], [22, 37], [22, 38], [23, 38], [23, 39],
    [5, 12], [11, 12], [11, 18], [29, 36], [35, 36], [35, 42],
]
for ij in inter:
    (x0, y0), (x1, y1) = points_collection[ij]
    ax.plot(
        [x0, x1], [y0, y1], ls="dashed", lw=line_width,
        color="gray", zorder=0
    )

arrowprops = {
    "width": 5,
    "headlength": 30,
    "headwidth": 15,
    "color": "black",
}
ax.annotate("", vectors[0], (0, 0), arrowprops=arrowprops, zorder=2)
ax.annotate("", vectors[1], (0, 0), arrowprops=arrowprops, zorder=2)
ax.text(
    3, -0.35, r"$\mathbf{a}_1$", fontsize=XXLARGE+10, ha="center", va="center"
)
ax.text(
    1.4, 1.2, r"$\mathbf{a}_2$", fontsize=XXLARGE+10, ha="center", va="center",
    rotation=30,
)
ax.text(
    0.02, 1.00, "(g)",
    ha="center", va="top", fontsize=XXLARGE+10, transform=ax.transAxes
)
ax.set_axis_off()
ax.set_aspect("equal")
# plt.get_current_fig_manager().window.showMaximized()
fig.set_size_inches(19, 4.5)
plt.tight_layout()
plt.show()
print(fig.get_size_inches())
fig.savefig("fig/Triangle12Cluster.pdf", transparent=True)
plt.close("all")

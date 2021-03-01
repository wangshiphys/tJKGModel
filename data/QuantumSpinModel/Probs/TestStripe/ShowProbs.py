import matplotlib.pyplot as plt
import numpy as np

alpha = 0.70
beta  = 0.66
J = np.sin(alpha * np.pi) * np.sin(beta * np.pi)
K = np.sin(alpha * np.pi) * np.cos(beta * np.pi)
G = np.cos(alpha * np.pi)

tmp = -(G + 2 * K - np.sqrt(9 * G * G - 4 * K * G + 4 * K * K)) / 4
sy = sz = np.sqrt(G * G / (4 * tmp * (tmp + G) + 3 * G * G))
sx = sy * (2 * tmp + G) / G

# sx = 0
# sy = 1
# sz = -1
phi0 = np.arctan2(sy, sx) / np.pi
theta0 = np.arctan2(np.sqrt(sx * sx + sy * sy), sz) / np.pi
phi1 = 1 + phi0
theta1 = 1 - theta0

direction = "avg"
config = "StripeX"
ps_name_temp = "PS_num1=4_num2=6_direction={0}" \
               "_config={1}_alpha={2:.4f}_beta={3:.4f}.npz"

ps_data_name = "data/" + ps_name_temp.format(direction, config, alpha, beta)
with np.load(ps_data_name) as ld:
    phis = ld["phis"]
    thetas = ld["thetas"]
    probabilities = ld["probabilities"]

fig, ax = plt.subplots()
cs = ax.pcolormesh(
    phis / np.pi, thetas / np.pi, probabilities,
    zorder=0, cmap="magma", shading="gouraud",
)
colorbar = fig.colorbar(cs, ax=ax, pad=0.02, format="%.2f")
colorbar.ax.tick_params(axis="y", labelsize=35)
ax.plot(
    phi0, theta0,
    zorder=3, ls="", marker="o", ms=20,
    color="tab:green", alpha=0.9
)
ax.plot(
    phi1, theta1,
    zorder=3, ls="", marker="o", ms=20,
    color="tab:green", alpha=0.9
)

ax.grid(True, ls="dashed", color="gray")

ax.set_xlabel(r"$\phi/\pi$", fontsize=35)
ax.set_ylabel(r"$\theta/\pi$", fontsize=35, rotation=0, labelpad=25)
ax.set_yticks([0.0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0])
ax.set_xticks([0.0, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00])
ax.tick_params(labelsize=35)
ax.set_title(
    r"$\alpha={0:.2f}\pi,\beta={1:.2f}\pi$".format(alpha, beta), fontsize=50
)
# title = r"$\alpha={0:.2f}\pi,\beta={1:.2f}\pi,direction={2},config={3}$".format(
#     alpha, beta, direction, config,
# )
# ax.set_title(title, fontsize="xx-large")
plt.get_current_fig_manager().window.showMaximized()
# plt.tight_layout()
plt.show()
# fig.savefig("alpha={0:.4f}_beta={1:.4f}.png".format(alpha, beta),
#             transparent=True)
plt.close("all")

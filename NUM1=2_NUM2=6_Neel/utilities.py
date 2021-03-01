import matplotlib.pyplot as plt
import numpy as np

from HamiltonianPy import Lattice


class TriangularLattice:
    DEFAULT_MODEL_PARAMETERS = {
        "alpha": 0.5, "beta": 1.5,
        "J": -1.0, "K": 0.0, "G": 0.0, "GP": 0.0,
    }

    def __init__(self):
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
        cluster = Lattice(points, vectors)
        intra, inter = cluster.bonds(nth=1)
        x_bonds = []
        y_bonds = []
        z_bonds = []
        for bond in intra + inter:
            p0, p1 = bond.endpoints
            index0 = cluster.getIndex(site=p0, fold=True)
            index1 = cluster.getIndex(site=p1, fold=True)
            bond_index = (index0, index1)

            azimuth = bond.getAzimuth(ndigits=0)
            if azimuth in (-180, 0, 180):
                x_bonds.append(bond_index)
            elif azimuth in (-120, 60):
                z_bonds.append(bond_index)
            elif azimuth in (-60, 120):
                y_bonds.append(bond_index)
            else:
                raise RuntimeError("Invalid bond azimuth: {0}".format(azimuth))

        self._identity = "Triangle12"
        self._cluster = cluster
        self._x_bonds = tuple(x_bonds)
        self._y_bonds = tuple(y_bonds)
        self._z_bonds = tuple(z_bonds)

    @property
    def identity(self):
        return self._identity

    @property
    def site_num(self):
        return self._cluster.point_num

    @property
    def cluster(self):
        return self._cluster

    @property
    def x_bonds(self):
        """
        The `x_bonds` attribute.
        """

        return self._x_bonds

    @property
    def y_bonds(self):
        """
        The `y_bonds` attribute.
        """

        return self._y_bonds

    @property
    def z_bonds(self):
        """
        The `z_bonds` attribute.
        """

        return self._z_bonds

    @property
    def x_bond_num(self):
        """
        The number of x-type bonds.
        """

        return len(self._x_bonds)

    @property
    def y_bond_num(self):
        """
        The number of y-type bonds.
        """

        return len(self._y_bonds)

    @property
    def z_bond_num(self):
        """
        The number of z-type bonds.
        """

        return len(self._z_bonds)

    @property
    def all_bonds(self):
        """
        The `all_bonds` attribute.
        """

        return self._x_bonds, self._y_bonds, self._z_bonds

    def ShowNNBonds(self, lw=2.0, ms=6.0):
        """
        Show nearest neighbor bonds.

        Parameters
        ----------
        lw : float, optional
            The line width of the bond.
            Default: 2.0.
        ms : float, optional
            The size of the point.
            Default: 6.0.
        """

        fig, ax = plt.subplots(num="NNBonds")
        intra, inter = self._cluster.bonds(nth=1)
        for ls, bonds in [("solid", intra), ("dashed", inter)]:
            for bond in bonds:
                (x0, y0), (x1, y1) = bond.endpoints
                azimuth = bond.getAzimuth(ndigits=0)
                if azimuth in (-180, 0, 180):
                    color = "tab:red"
                elif azimuth in (-120, 60):
                    color = "tab:green"
                elif azimuth in (-60, 120):
                    color = "tab:blue"
                else:
                    raise RuntimeError(
                        "Invalid bond azimuth: {0}".format(azimuth)
                    )
                ax.plot([x0, x1], [y0, y1], ls=ls, lw=lw, color=color)

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                dR = np.dot([i, j], self._cluster.vectors)
                points = self._cluster.points + dR
                ax.plot(points[:, 0], points[:, 1], ls="", marker="o", ms=ms)

        ax.set_axis_off()
        ax.set_aspect("equal")
        try:
            plt.get_current_fig_manager().window.showMaximized()
        except Exception:
            pass
        plt.show()
        plt.close("all")


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


if __name__ == "__main__":
    lattice = TriangularLattice()
    lattice.ShowNNBonds()

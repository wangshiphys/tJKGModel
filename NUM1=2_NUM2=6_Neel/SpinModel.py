import logging
from pathlib import Path
from time import time

import HamiltonianPy as HP
import numpy as np
from scipy.sparse import load_npz, save_npz
from scipy.sparse.linalg import eigsh

from utilities import TriangularLattice

logging.getLogger(__name__).addHandler(logging.NullHandler())

class JKGModelEDSolver(TriangularLattice):
    def _TermMatrix(self):
        directory = Path("tmp/")
        file_HJ = directory / "TRIANGLE12_HJ.npz"
        file_HK = directory / "TRIANGLE12_HK.npz"
        file_HG = directory / "TRIANGLE12_HG.npz"

        logger = logging.getLogger(__name__).getChild(
            ".".join([self.__class__.__name__, "TermMatrix"])
        )
        if file_HJ.exists() and file_HK.exists() and file_HG.exists():
            t0 = time()
            HJ = load_npz(file_HJ)
            HK = load_npz(file_HK)
            HG = load_npz(file_HG)
            t1 = time()
            logger.info("Load HJ, HK, HG, dt=%.3fs", t1 - t0)
        else:
            site_num = self.site_num
            configs = (("x", "y", "z"), ("y", "z", "x"), ("z", "x", "y"))

            HJ = HK = HG = 0.0
            msg = "%s-bond: %2d/%2d, dt=%.3fs"
            m_func = HP.SpinInteraction.matrix_function
            for (gamma, alpha, beta), bonds in zip(configs, self.all_bonds):
                bond_num = len(bonds)
                for count, (index0, index1) in enumerate(bonds, start=1):
                    t0 = time()
                    SKM = m_func([(index0, gamma), (index1, gamma)], site_num)
                    HK += SKM
                    HJ += SKM
                    HJ += m_func([(index0, alpha), (index1, alpha)], site_num)
                    HJ += m_func([(index0, beta), (index1, beta)], site_num)
                    HG += m_func([(index0, alpha), (index1, beta)], site_num)
                    HG += m_func([(index0, beta), (index1, alpha)], site_num)
                    t1 = time()
                    logger.info(msg, gamma, count, bond_num, t1 - t0)
            directory.mkdir(parents=True, exist_ok=True)
            save_npz(file_HJ, HJ, compressed=True)
            save_npz(file_HK, HK, compressed=True)
            save_npz(file_HG, HG, compressed=True)
        return HJ, HK, HG

    def EigenStates(
            self, es_path="data/QuantumSpinModel/ES/",
            k=1, v0=None, tol=0.0, **model_params,
    ):
        actual_model_params = dict(self.DEFAULT_MODEL_PARAMETERS)
        actual_model_params.update(model_params)
        alpha = actual_model_params["alpha"]
        beta = actual_model_params["beta"]
        J = np.sin(alpha * np.pi) * np.sin(beta * np.pi)
        K = np.sin(alpha * np.pi) * np.cos(beta * np.pi)
        G = np.cos(alpha * np.pi)

        HJ, HK, HG = self._TermMatrix()
        HM = J * HJ + K * HK + G * HG

        es_path = Path(es_path)
        es_name_temp = "ES_" + self.identity + "_alpha={0:.4f}_beta={1:.4f}.npz"
        es_full_name = es_path / es_name_temp.format(alpha, beta)

        logger = logging.getLogger(__name__).getChild(
            ".".join([self.__class__.__name__, "GS"])
        )
        if es_full_name.exists():
            with np.load(es_full_name) as ld:
                values = ld["values"]
                vectors = ld["vectors"]
            logger.info("Load ES data from %s", es_full_name)
        else:
            t0 = time()
            values, vectors = eigsh(HM, k=k, which="SA", v0=v0, tol=tol)
            t1 = time()
            msg = "ES for alpha=%.4f, beta=%.4f, dt=%.3fs"
            logger.info(msg, alpha, beta, t1 - t0)

            es_path.mkdir(exist_ok=True, parents=True)
            np.savez_compressed(
                es_full_name, parameters=[alpha, beta],
                values=values, vectors=vectors,
            )
            logger.info("Save ES data to %s", es_full_name)
        return values, vectors, HM

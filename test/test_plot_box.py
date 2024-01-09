import numpy as np
import pytest

from hplot import plot_box


def test_plot_box():
    d1 = np.random.randn(100)
    d2 = d1 * 0.8 + 0.5
    data = [{"label": "a", "y": d1}, {"label": "b", "y": d2}]

    plot_box(data, fname="figure/plot_box_example.png", display=False, width=0.2, linewidth=0.1)


if __name__ == "__main__":
    test_plot_box()

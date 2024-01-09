import numpy as np
import pytest

from hplot import plot_heatmap


def test_plot_sns():
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2
    plot_heatmap(
        x=x,
        y=y,
        z=Z,
        fname="figure/plot_heatmap_example.png",
        display=False,
        cmap="BrBG",
        vmin=0,
        vmax=200,
        center=None,
        levels=[10],
        level_colors=["red"],
    )


if __name__ == "__main__":
    test_plot_sns()

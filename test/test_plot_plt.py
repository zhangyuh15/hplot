import numpy as np
import pytest

from hplot import plot_plt


def test_plot_plt():
    x = np.linspace(-2, 2, 200)
    y1 = np.sin(2 * 3.14 * x)
    y2 = np.cos(2 * 3.14 * x)

    data = [dict(x=x, y=y1), dict(x=x, y=y2)]

    plot_plt(
        data,
        "figure/plot_plt_example.png",
        xlabel="x",
        ylabel="y",
        legend=["sin", "cos"],
        legend_loc="lower right",
        xlim=[-3, +3],
        ylim=[-2, +2],
        xticks=[-2, +2],
        xtick_labels=["xstart", "xend"],
        yticks=[-1, +1],
        ytick_labels=["ystart", "yend"],
        display=False,
    )


if __name__ == "__main__":
    test_plot_plt()

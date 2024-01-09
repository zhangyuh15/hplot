import numpy as np
import pytest

from hplot import plot_sns


def test_plot_sns():
    x = np.linspace(-2, 2, 500)
    y1 = 0.7 * np.sin(2 * 3.14 * x) + 0.3 * np.sin(2 * 3.14 * x) * np.random.randn(*x.shape)
    y2 = 0.7 * np.sin(2 * 3.14 * x) + 0.3 * np.sin(2 * 3.14 * x) * np.random.randn(*x.shape)
    y3 = 0.7 * np.sin(2 * 3.14 * x) + 0.3 * np.sin(2 * 3.14 * x) * np.random.randn(*x.shape)
    data = [dict(x=[x, x, x], y=[y1, y2, y3], label="sin")]
    x = np.linspace(-2, 2, 500)
    y1 = 0.7 * np.cos(2 * 3.14 * x) + 0.3 * np.cos(2 * 3.14 * x) * np.random.randn(*x.shape)
    y2 = 0.7 * np.cos(2 * 3.14 * x) + 0.3 * np.cos(2 * 3.14 * x) * np.random.randn(*x.shape)
    y3 = 0.7 * np.cos(2 * 3.14 * x) + 0.3 * np.cos(2 * 3.14 * x) * np.random.randn(*x.shape)
    y = np.stack([y1, y2, y3])
    data.append(dict(x=[x, x, x], y=[y1, y2, y3], label="cos"))
    plot_sns(
        data,
        "figure/plot_sns_example.png",
        xlabel="x",
        ylabel="y",
        legend=["SIN-FUNC", "COS-FUNC"],
        legend_loc="lower right",
        legend_frameon=True,
        xlim=[-3, +3],
        ylim=[-2, +2],
        xticks=[-2, +2],
        xtick_labels=["xstart", "xend"],
        yticks=[-1, +1],
        ytick_labels=["ystart", "yend"],
        display=False,
    )


if __name__ == "__main__":
    test_plot_sns()

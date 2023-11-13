import os

import numpy as np

from hplot import plot_box, plot_plt, plot_sns

os.makedirs("figure", exist_ok=True)


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
    display=True,
)

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
    display=True,
)

d1 = np.random.randn(100)
d2 = d1 * 0.8 + 0.5
data = [{"label": "a", "y": d1}, {"label": "b", "y": d2}]

plot_box(data, fname="figure/plot_box_example.png", display=True, width=0.2, linewidth=0.1)

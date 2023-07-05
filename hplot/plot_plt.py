import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from itertools import cycle
from matplotlib import rcParams

from hplot.utils import cm2inch
from hplot.config import default_cfg


class PloterPlt:
    def __init__(
        self,
        data,
        fname=None,
        *,
        xlabel=None,
        ylabel=None,
        legend=None,
        legend_loc="best",
        color_list=None,
        xlim=None,
        ylim=None,
        xticks=None,
        yticks=None,
        xtick_labels=None,
        ytick_labels=None,
        usetex=False,
        ncol=1,
        display=True,
        fig_size=None,
        dpi=None,
        pad=None,
        tick_size=None,
        tick_label_font=None,
        legend_font_dict=None,
        label_font_dict=None,
        **kwargs,
    ):
        self.data = data
        self.fname = fname
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.legend = legend
        self.legend_loc = legend_loc
        self.color_list = color_list
        self.xlim = xlim
        self.ylim = ylim
        self.xticks = xticks
        self.yticks = yticks
        self.xtick_labels = xtick_labels
        self.ytick_labels = ytick_labels
        self.usetex = usetex
        self.ncol = ncol
        self.display = display
        self.fig_size = fig_size
        self.dpi = dpi
        self.pad = pad
        self.tick_size = tick_size
        self.tick_label_font = tick_label_font
        self.legend_font_dict = legend_font_dict
        self.label_font_dict = label_font_dict

        self.num_data = None
        self.fig = None
        self.ax = None

        self.__preprocess()

    def __preprocess(self):
        rcParams.update({"mathtext.fontset": "stix"})
        assert isinstance(self.data, (dict, list, tuple))

        if isinstance(self.data, dict):
            self.data = [self.data]
        self.num_data = len(self.data)

        if self.fig_size is None:
            self.fig_size = default_cfg.fig_size
        if self.dpi is None:
            self.dpi = default_cfg.dpi
        if self.pad is None:
            self.pad = default_cfg.pad
        if self.tick_size is None:
            self.tick_size = default_cfg.tick_size
        if self.tick_label_font is None:
            self.tick_label_font = default_cfg.tick_label_font
        if self.legend_font_dict is None:
            self.legend_font_dict = default_cfg.legend_font
        if self.label_font_dict is None:
            self.label_font_dict = default_cfg.label_font

        # use tex to render fonts, tex install required
        if self.usetex:
            from matplotlib import rc

            rc("font", **{"family": "serif", "serif": ["Times New Roman"]})
            rc("text", usetex=True)

        # color list
        if (self.color_list is None) or len(self.color_list) < self.num_data:
            tableau_colors = cycle(mcolors.TABLEAU_COLORS)
            self.color_list = [next(tableau_colors) for _ in range(self.num_data)]

    def plot(self):
        self.fig, self.ax = plt.subplots(figsize=cm2inch(*self.fig_size), dpi=self.dpi)

        # plot figure
        for i, d in enumerate(self.data):
            plt.plot(d["x"], d["y"], color=self.color_list[i])

        # legend
        plt.tick_params(labelsize=self.tick_size)
        labels = self.ax.get_xticklabels() + self.ax.get_yticklabels()
        [label.set_fontname(self.tick_label_font) for label in labels]

        if self.legend is not None:
            plt.legend(self.legend, loc=self.legend_loc, ncol=self.ncol, prop=self.legend_font_dict)

        #  label
        plt.xlabel(self.xlabel, self.label_font_dict)
        plt.ylabel(self.ylabel, self.label_font_dict)

        if self.xlim is not None:
            plt.xlim(self.xlim)
        if self.ylim is not None:
            plt.ylim(self.ylim)
        if self.xticks is not None and self.xtick_labels is not None:
            plt.xticks(self.xticks, self.xtick_labels)
        if self.yticks is not None and self.ytick_labels is not None:
            plt.yticks(self.yticks, self.ytick_labels)

    def save(self):
        plt.tight_layout(pad=self.pad)
        if self.fname is None:
            pass
        else:
            plt.savefig(self.fname)

    def show(self):
        plt.tight_layout(pad=self.pad)
        plt.show()

    def close(self):
        plt.close()


def plot_plt(
    data,
    fname=None,
    *,
    xlabel=None,
    ylabel=None,
    legend=None,
    legend_loc="best",
    xlim=None,
    ylim=None,
    xticks=None,
    yticks=None,
    xtick_labels=None,
    ytick_labels=None,
    display=True,
    fig_size=None,
    dpi=None,
    **kwargs,
):
    """
    plot a curve using matplotlib.pyplot
    :param data: list[dict]:
        data used to plot figures,
        example: [dict(x=x1, y=y1), dict(x=x2, y=y2)]
    :param fname: str,
        the figure will be saved here,
        example: "./path_to_file/figure.png"
    :param xlabel: str
    :param ylabel: str
    :param legend: list[str]
    :param legend_loc: "best", "upper right", "upper left", "lower left", "lower right", "right", "center left",
        "center right", "lower center", "upper center", "center"
    :param xlim:
    :param ylim:
    :param xticks:
    :param yticks:
    :param xtick_labels:
    :param ytick_labels:
    :param display:
    :param fig_size:
    :param dpi:
    :param kwargs:
    :return:
    """
    ploter = PloterPlt(
        data,
        fname,
        xlabel=xlabel,
        ylabel=ylabel,
        legend=legend,
        legend_loc=legend_loc,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=yticks,
        xtick_labels=xtick_labels,
        ytick_labels=ytick_labels,
        display=display,
        fig_size=fig_size,
        dpi=dpi,
        **kwargs,
    )
    ploter.plot()
    if fname is not None:
        ploter.save()
    if display:
        ploter.show()

    ploter.close()


if __name__ == "__main__":
    import numpy as np

    x = np.linspace(-2, 2, 200)
    y1 = np.sin(2 * 3.14 * x)
    y2 = np.cos(2 * 3.14 * x)

    data = [dict(x=x, y=y1), dict(x=x, y=y2)]

    plot_plt(
        data,
        "plot_plt_example.png",
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

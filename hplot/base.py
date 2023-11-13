from abc import ABCMeta, abstractmethod
import os
import matplotlib.pyplot as plt
from hplot.config import hConfig

class Base(metaclass=ABCMeta):
    def __init__(self, **kwargs):

        self._kwargs = kwargs
        self.fname = None
        self.fig = None
        self.ax = None
        self.pad = None
        self.display = None
        self.process_args()

    def process_args(self):
        self.pad = self._kwargs.get("pad", None)
        if self.pad is None:
            self.pad = hConfig.pad

    @abstractmethod
    def plot(self):
        pass

    def save(self):
        plt.tight_layout(pad=self.pad)
        if self.fname is None:
            pass
        else:
            dir_path = os.path.dirname(self.fname)
            os.makedirs(dir_path, exist_ok=True)
            plt.savefig(self.fname)

    def show(self):
        self.fig.set_tight_layout(True)
        plt.tight_layout(pad=self.pad)
        plt.show()

    def close(self):
        plt.close()

    def run(self):
        self.plot()
        if self.fname is not None:
            self.save()
        if self.display:
            self.show()
        self.close()
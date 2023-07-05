from glob import glob
import pandas as pd


def load_saved_data(file_template, label=""):
    output_list = []
    for file_path in glob(file_template):
        one_data = pd.read_csv(file_path).values
        x = one_data[:, 0]
        y = one_data[:, 1]
        output_list.append(
            dict(x=x, y=y, label=label)
        )
        break
    return output_list
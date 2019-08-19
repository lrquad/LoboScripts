import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from matplotlib import rcParams
import matplotlib.patches as patches
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 20
rcParams['axes.edgecolor'] = (0.0, 0.0, 0.0)
rcParams['axes.linewidth'] = 2
hfont = {'fontname': 'Times New Roman'}

folderpath = "./testdata/"


def loadData(path, logscale=True, min=1e-16):
    data = np.array(np.loadtxt(path, delimiter=',', unpack=True))
    data[data < min] = min
    data = np.log10(data)
    return data


def loadlabel(path):
    data = np.array(np.loadtxt(path, delimiter=' ', unpack=True))
    return data


if __name__ == "__main__":
    data = loadData(folderpath+"ttmath_error.csv")
    labels = loadlabel(folderpath+"h_list.csv")

    num_lines = data.shape[0]
    num_x = data.shape[1]

    y_max = np.max(data)
    y_min = np.min(data)

    

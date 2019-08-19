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

def format_e(n):
    a = '%E' % n
    return a.split('E')[0].rstrip('0').rstrip('.') + '.0E' + a.split('E')[1]

def loadData(path, logscale=True, min=1e-16):
    data = np.array(np.loadtxt(path, delimiter=',', unpack=True))
    data[data < min] = min
    data = np.log10(data)
    return data


def loadlabel(path):
    data = np.array(np.loadtxt(path, delimiter=' ', unpack=True))
    return data

def init(ax,xlabel_list,y_min,y_max,num_x,x_labels_num = 16,y_labels_num=18):
    ax.set_xlim(0, num_x)
    print(y_min,y_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel("Perturbation size",**hfont)
    ax.set_ylabel("Relative error ", **hfont)
    
    y_labels_tuples = ()
    ax.yaxis.set_major_locator(plt.MaxNLocator(y_labels_num))
    x_labels_tuples = ()
    ax.xaxis.set_major_locator(plt.MaxNLocator(x_labels_num+1))

    for i in range(0,y_labels_num):
        y_value = i/(y_labels_num-1)*(y_max-y_min)+y_min
        y_value = format_e(10**int(y_value))
        y_labels_tuples = y_labels_tuples+(y_value,)
    ax.set_yticklabels(y_labels_tuples,size = 10)

    for i in range(0,x_labels_num):
        index = int(i/(x_labels_num-1)*(num_x-1))
        x_labels_tuples = x_labels_tuples + (format_e(xlabel_list[index]),)
    ax.set_xticklabels(x_labels_tuples,size = 15)

    plt.xticks(rotation=45)

    return

def plotData(data, labels,names):
    num_lines = data.shape[0]
    num_x = data.shape[1]

    y_max = np.max(data)
    y_min = np.min(data)

    fig, ax = plt.subplots()
    init(ax,labels,y_min,y_max,num_x,x_labels_num=16,y_labels_num=18)

    fig.set_figheight(8)
    fig.set_figwidth(8)
    plt.grid(True)

    ydata = np.arange(num_x)

    for i in range(num_lines):
        print(ydata.tolist())
        print(data[i,:].tolist())
        plt.plot(ydata.tolist(),data[i,:].tolist(),'-', animated=False,antialiased=True,markersize=5,color =  '#FF5C5C',label = names[i],linewidth = 6)
    
    #ln, = plt.plot(ydata.tolist(),data[0,:].tolist(),'-', animated=True,antialiased=True,markersize=5,color =  '#FF5C5C',label = "te",linewidth = 6)
    
    plt.subplots_adjust(bottom=0.22)
    plt.show()

    return

if __name__ == "__main__":
    data = loadData(folderpath+"ttmath_error.csv")
    labels = loadlabel(folderpath+"h_list.csv")
    plotData(data, labels,["ttmath","FD","CD","CFD"])

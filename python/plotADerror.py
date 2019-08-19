import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from matplotlib import rcParams
import matplotlib.patches as patches
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 20
rcParams['axes.edgecolor']= (0.0,0.0,0.0)
rcParams['axes.linewidth']= 2
hfont = {'fontname':'Times New Roman'}

folderpath = "/media/ranluo/New Volume/DEMO/Siggraph2019/AD_test_results/"

errors = np.array(np.loadtxt(folderpath+"ttmath_error.csv", delimiter=',',unpack=True))
xlabel_list = np.array(np.loadtxt(folderpath+"h_list.csv", delimiter=',',unpack=True))

errors = np.log10(errors+1e-16)
y_max = np.max(errors)
y_min = np.min(errors)

num = int(errors.shape[0]/2)

xlabel_list_num = int(xlabel_list.shape[0])

#num = 150

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(8)
plt.grid(True)

#fig.set_figheight(8)
#fig.set_figwidth(32)



xdata = []
ydata = []

ln, = plt.plot([],[],'-', animated=True,antialiased=True,markersize=5,color =  '#FF5C5C',label = 'Relative error',linewidth = 6)

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=60, metadata=dict(artist='me'), bitrate=1800)

#patch = patches.Rectangle((0, 0), 500, y_max/2, fc='y',color = 'Teal',alpha = 0.1,linestyle='dashed',hatch='/')
#patch_text = plt.text(100, y_max/4,'Training range',rotation=0,size = 10)

def format_e(n):
    a = '%E' % n
    return a.split('E')[0].rstrip('0').rstrip('.') + '.0E' + a.split('E')[1]

def init():
    ax.set_xlim(0, num)
    print(y_min,y_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel("Perturbation size",**hfont)
    ax.set_ylabel("Relative error ", **hfont)

    y_labels_tuples = ()
    y_labels_num = 18
    ax.yaxis.set_major_locator(plt.MaxNLocator(y_labels_num))

    for i in range(0,y_labels_num):
        y_value = i/(y_labels_num-1)*(y_max-y_min)+y_min
        y_value = format_e(10**int(y_value))
        y_labels_tuples = y_labels_tuples+(y_value,)
    print(y_labels_tuples)
    ax.set_yticklabels(y_labels_tuples,size = 10)
    
    x_labels_tuples = ()
    x_labels_num =16
    ax.xaxis.set_major_locator(plt.MaxNLocator(x_labels_num+1))
    for i in range(0,x_labels_num):
        index = int(i/(x_labels_num-1)*(xlabel_list_num-1))
        x_labels_tuples = x_labels_tuples + (format_e(xlabel_list[index]),)

    print(x_labels_tuples)
    ax.set_xticklabels(x_labels_tuples,size = 15)
    
    plt.xticks(rotation=45)

    #ax.spines['right'].set_visible(False)
    #ax.spines['top'].set_visible(False)

    #ax.add_patch(patch)

    #mylegend = ax.legend(loc='upper left', fancybox=True, framealpha=0.5)
    
    return ln,

def update(frame):
    # if frame%20!=0:
    #     return ln,ln2,ln3

    if(frame < num):
        xdata.append(frame)
        ydata.append(errors[(frame)])
        ln.set_data(xdata,ydata)

    #hln = ax.vlines(500, 0, y_max/2, colors='r', linestyles='dashed', label='')

    #mylegend = ax.legend(loc='upper left', fancybox=True, framealpha=0.5)
    #plt.plot(xdata,ydata,'ro', animated=True)
    return ln,

ani = FuncAnimation(fig, update,num-1,interval=20,init_func=init,repeat=False,
                   blit=True)

plt.subplots_adjust(bottom=0.22)

# ani.save('D:/DEMO/Siggraph2019/demo_PPT/videos/cr_errors.mp4', writer=writer)
# exportPDF.figExportPDF(fig,'D:/Data/AdobePremiere/bending_prediction/scale_error.svg')

plt.show()
fig.savefig(folderpath+'errors.png')

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np

data = []

fn = input()
cc = 1

with open('../outputs/' + fn, 'r') as f:
    for line in f:
        for i in line.split():
            if i == '#' :
                fig, ax = plt.subplots()
                ax.plot(data, linewidth=0.1)
                plt.savefig('result_' + fn + '-' + str(cc) + '.png')
                cc+=1
                data = []
            else:
                data.append(int(i))

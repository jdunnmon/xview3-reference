import matplotlib.pylab as plt
import numpy as np

def plot_perf_vs_size(szs, prf, ttl, save_loc=None):
    sizes = list(szs[0:-1])
    precs = [prf[ky][0] for ky in sizes]
    recs = [prf[ky][1] for ky in sizes]
    f1s = [prf[ky][2] for ky in sizes]

    fig = plt.figure(figsize=(10,5))
    N = len(sizes)
    ind = np.arange(N) 
    width = 0.25

    xvals = sizes
    bar1 = plt.bar(ind, precs, width)

    yvals = [10, 20, 30]
    bar2 = plt.bar(ind+width, recs, width)

    zvals = [11, 12, 13]
    bar3 = plt.bar(ind+width*2, f1s, width)

    plt.ylabel('Model Performance')
    plt.xlabel("Vessel Size Range (m)")

    plt.ylim((0.0,1.05))

    plt.xticks(ind+width,[f'{szs[s]}-{szs[s+1]}' for s in range(len(sizes))], rotation=45)
    plt.legend( (bar1, bar2, bar3), ('Precision','Recall','F1'), ncol=3, loc="upper left" )
    plt.tight_layout()
    if save_loc is not None:
        plt.savefig(f'{save_loc}/Performance-Vs-Size-{ttl}.jpg')
        

def plot_size_hist(szs, nums, ttl, save_loc=None):
    sizes = list(szs[0:-1])
    fig = plt.figure(figsize=(10,5))
    ind = np.arange(len(nums))
    plt.bar(ind,nums.values())
    plt.xticks(ind,[f'{szs[s]}-{szs[s+1]}' for s in range(len(sizes))], rotation=45)
    plt.xlabel("Vessel Size Range (m)")
    plt.ylabel('Number of Vessels')
    plt.tight_layout()
    if save_loc is not None:
        plt.savefig(f'{save_loc}/Size-Hist-{ttl}.jpg')
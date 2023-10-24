import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.collections import PolyCollection


if __name__ == '__main__':
    plot = {
        "utemezo": [[0.0, 0.5], [4.0, 4.5], [8.0, 8.5], [12.0, 12.5], [16.0, 16.5], [20.0, 20.5], [24.0, 24.5], [28.0, 28.5], [32.0, 32.5], [36.0, 36.5], [40.0, 40.5], [44.0, 44.5], [48.0, 48.5], [52.0, 52.5], [56.0, 56.5], [60.0, 60.5], [64.0, 64.5], [68.0, 68.5], [72.0, 72.5], [76.0, 76.5], [80.0, 80.5], [84.0, 84.5], [88.0, 88.5], [92.0, 92.5], [96.0, 96.5], [100.0, 100.5], [104.0, 104.5], [108.0, 108.5], [112.0, 112.5], [116.0, 116.5], [120.0, 120.5], [124.0, 124.5]],
        " task1 ": [[20.5, 24.5], [46.1, 50.1], [50.1, 54.1], [78.1, 82.1], [82.1, 86.1], [110.1, 114.1], [114.1, 118.1]],
        " task2 ": [[16.5, 20.5], [24.5, 26.5], [54.1, 60.1], [86.1, 92.1], [118.1, 124.1]],
        " task3 ": [[8.5, 16.5], [70.1, 78.1]],
        " task4 ": [[6.5, 8.5], [60.1, 70.1], [92.1, 110.1]],
        " ures  ": [[0.0, 6.5], [26.5, 46.1], [124.1, 128]]
    }

    cats = {"utemezo": 1, " task1 ": 2, " task2 ": 3, " task3 ": 4, " task4 ": 5, " ures  ": 6}
    colormapping = {"utemezo": "C0", " task1 ": "C1", " task2 ": "C2", " task3 ": "C6", " task4 ": "C4", " ures  ": "C5"}

    print("--------------------------------------")
    verts = []
    colors = []
    for name in plot.keys():
        print(name)
        for d in plot[name]:
            print(f"{d[0]}, {d[1]}")
            v = [(d[0], cats[name] - .4),
                 (d[0], cats[name] + .4),
                 (d[1], cats[name] + .4),
                 (d[1], cats[name] - .4),
                 (d[0], cats[name] - .4)]
            verts.append(v)
            colors.append(colormapping[name])
    print("--------------------------------------")

    for task in [
        [" task1 ", 181, 1280, 160],
        [" task2 ", 122, 1280, 320],
        [" task3 ", 43, 1280, 640],
        [" task4 ", 4, 1280, 1280],
    ]:
        for t in range(task[1], task[2], task[3]):
            v = [((t-1)/10, cats[task[0]] - .4),
                 ((t-1)/10, cats[task[0]] + .4),
                 ((t+1)/10, cats[task[0]] + .4),
                 ((t+1)/10, cats[task[0]] - .4),
                 ((t-1)/10, cats[task[0]] - .4)]
            verts.append(v)
            colors.append("C3")

    bars = PolyCollection(verts, facecolors=colors)

    fig, ax = plt.subplots()
    ax.add_collection(bars)
    ax.autoscale()
    plt.grid(color='black', linestyle='-', linewidth=0.5, axis="x")

    ax.set_yticks([1, 2, 3, 4, 5, 6, 7])
    ax.set_yticklabels(["utemezo", "task1", "task2", "task3", "task4", "ures"])
    plt.show()
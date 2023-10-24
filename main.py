import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.collections import PolyCollection
class Task:
    def __init__(self, name, T, C, f0, max_iter):
        self.name = name
        self.T = T
        self.C = C
        self.f0 = f0
        self.computes = {}
        for i in range(f0, max_iter, T):
            self.computes.update({i: C})

        print(self.computes)

    def active(self, time) -> bool:
        if time < self.f0:
            return False
        current_start = self.f0 + ((time - self.f0) // self.T) * self.T
        return self.computes[current_start] > 0

    def work(self, time) -> bool:
        current_start = self.f0 + ((time - self.f0) // self.T) * self.T
        self.computes[current_start] -= 1
        return self.computes[current_start] > 0


if __name__ == '__main__':
    max_iter = 1280
    utemezes = 0
    tasks = [
        Task(" task1 ", 160, 40, 181, max_iter),
        Task(" task2 ", 320, 60, 122, max_iter),
        Task(" task3 ", 640, 80, 43, max_iter),
        Task(" task4 ", 1280, 300, 4, max_iter)
    ]

    futas = {
        "utem 10": ['| ' if i % 10 == 0 else '  ' for i in range(max_iter)],
        "utemezo": ['|.' if i % 40 == 0 else ' .' for i in range(max_iter)],
        " task1 ": ['|.' if i % 160 == 181 else ' .' for i in range(max_iter)],
        " task2 ": ['|.' if i % 320 == 122 else ' .' for i in range(max_iter)],
        " task3 ": ['|.' if i % 640 == 43 else ' .' for i in range(max_iter)],
        " task4 ": ['|.' if i % 1280 == 4 else ' .' for i in range(max_iter)],
        " ures  ": [' .' for i in range(max_iter)]
    }

    plot = {
        "utemezo": [],
        " task1 ": [],
        " task2 ": [],
        " task3 ": [],
        " task4 ": [],
        " ures  ": []
    }

    valtas = True
    actual_task = None
    ready_tasks = []
    for t in range(0, max_iter, 1):
        if t % 40 == 0:
            utemezes = 5
            plot["utemezo"].append([t, t+5])
            ready_tasks = []
            for task in tasks:
                if task.active(t):
                    ready_tasks.append(task)
            if len(ready_tasks) > 0:
                valtas = True
                ready_tasks.sort(key=lambda x: x.T)

        if actual_task is not None:
            if valtas:
                plot[actual_task.name].append([t, t])
                valtas = False
            futas[actual_task.name][t] = ' 0'
            plot[actual_task.name][-1][1] = t
            if not actual_task.work(t):
                ready_tasks[ready_tasks.index(actual_task)] = None
                actual_task = None
                valtas = True
        else:
            if valtas:
                plot[" ures  "].append([t, t])
                valtas = False
            futas[" ures  "][t] = ' 0'
            plot[" ures  "][-1][1] = t

        if utemezes > 0:
            utemezes -= 1
            if utemezes == 0:
                if len(ready_tasks) == 0:
                    actual_task = None
                elif ready_tasks[0] is None and len(ready_tasks) > 1:
                    actual_task = ready_tasks[1]
                else:
                    actual_task = ready_tasks[0]
                valtas = True

    for f in futas.keys():
        print(f, end="::")
        for ff in futas[f]:
            print(ff, end="")
        print()

    cats = {"utemezo": 1, " task1 ": 2, " task2 ": 3, " task3 ": 4, " task4 ": 5, " ures  ": 6}
    colormapping = {"utemezo": "C0", " task1 ": "C1", " task2 ": "C2", " task3 ": "C6", " task4 ": "C4", " ures  ": "C5"}

    a = 0
    b = []
    while a < len(plot[" ures  "]) - 2:
        if plot[" ures  "][a][1] + 1 == plot[" ures  "][a+1][0]:
            if len(b) == 0:
                b = [plot[" ures  "][a][0], plot[" ures  "][a+1][1]]
            else:
                b[1] = plot[" ures  "][a+1][1]
        else:
            print(f"{b[0]/10}, {b[1]/10}")
            b = []
        a += 1
    print(f"{b[0]/10}, {b[1]/10}" if len(b) > 0 else f"{plot[' ures  '][-1][0]/10}, {plot[' ures  '][-1][1]/10}")

    print("--------------------------------------")
    verts = []
    colors = []
    for name in plot.keys():
        print(name)
        for d in plot[name]:
            print(f"[{d[0] / 10}, {d[1] / 10 + 0.1}]", end=", ")
            v = [(d[0], cats[name] - .4),
                 (d[0], cats[name] + .4),
                 (d[1], cats[name] + .4),
                 (d[1], cats[name] - .4),
                 (d[0], cats[name] - .4)]
            verts.append(v)
            colors.append(colormapping[name])
        print()
    print("--------------------------------------")

    for task in tasks:
        print(task.computes)
        for t in range(task.f0, max_iter, task.T):
            v = [(t-1, cats[task.name] - .4),
                 (t-1, cats[task.name] + .4),
                 (t+1, cats[task.name] + .4),
                 (t+1, cats[task.name] - .4),
                 (t-1, cats[task.name] - .4)]
            verts.append(v)
            colors.append("C3")

    bars = PolyCollection(verts, facecolors=colors)

    fig, ax = plt.subplots()
    ax.add_collection(bars)
    ax.autoscale()
    plt.grid(color='black', linestyle='-', linewidth=0.5, axis="x")

    ax.set_yticks([1, 2, 3, 4, 5, 6])
    ax.set_yticklabels(["utemezo", "task1", "task2", "task3", "task4", "ures"])
    plt.show()
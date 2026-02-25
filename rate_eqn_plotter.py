import numpy as np
import matplotlib.pyplot as plt
import random

def rate_plotter():
    arg_list = {}
    ranger = random.randint(1, 8)

    for i in range(ranger):
        n = random.randint(1, 8)
        r = round(random.uniform(0, 1), 1)
        arg_list[n] = r

    num_plots = len(arg_list)
    ncols = int(np.ceil(np.sqrt(num_plots)))
    nrows = int(np.ceil(num_plots / ncols))

    fig, axs = plt.subplots(nrows, ncols, figsize=(8, 8))
    fig.suptitle('Rate Equation for various inputs of population N and rate of multiplicity R')

    for i, (n, r) in enumerate(arg_list.items()):
        n1 = n
        array_holder = []
        for _ in range(40):
            array_holder.append(n)
            n = r * n * (1 - n)

        x = np.array(array_holder)
        y = np.array(range(40))

        row = i // ncols
        col = i % ncols
        axs[row, col].plot(x, y, color="red")
        axs[row, col].set_title(f"N = {n1} and R = {r}")

    for ax in axs.flat:
        ax.label_outer()

    plt.tight_layout()
    plt.show()

rate_plotter()

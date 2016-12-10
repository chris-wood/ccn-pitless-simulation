#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

binSize = 1000000000

def main(argv):
    delays = {}
    fileNames = ["delay-int-pitfull-dfn",
                 "delay-data-pitfull-dfn",
                 "delay-int-pitless-dfn"]
    numberOfFiles = 10
    colors = {fileNames[0]: "r",
              fileNames[1]: "b",
              fileNames[2]: "g"}
    legendLabels = ["Stateful Interest Processing",
                    "Stateful Content Processing",
                    "Stateless Packet Processing"]

    for fileName in fileNames:
        delay = []
        counter = []

        for num in range(0, numberOfFiles):
            print "Processing '" + fileName + "-" + str(num + 1) + ".txt'..."

            delay.append([])
            counter.append([])
            delay[num].append(0.0)
            counter[num].append(0)
            currentTime = binSize
            with open(fileName + "-" + str(num + 1) + ".txt", "r") as fd:
                for line in fd:
                    if line.split("\t")[0] == "Time":
                        continue

                    simTime = float(line.strip("\n").split("\t")[1])
                    d = (float(line.split("\t")[2]) / 1000)
                    if simTime > currentTime + binSize:
                        delay[num].append(0.0)
                        counter[num].append(0)
                        currentTime = currentTime + binSize
                    delay[num][len(delay[num]) - 1] = delay[num][len(
                        delay[num]) - 1] + d
                    counter[num][len(delay[num]) - 1] = counter[num][len(
                        delay[num]) - 1] + 1

        for num in range(1, numberOfFiles):
            for i in range(0, len(delay[0])):
                delay[0][i] = delay[0][i] + delay[num][i]
                counter[0][i] = counter[0][i] + counter[num][i]

        for i in range(1, len(delay[0])):
            delay[0][i] = float(delay[0][i]) / counter[0][i]

        delays[fileName] = delay[0]

    print "Plotting..."
    fig, ax = plt.subplots()
    shift = 0
    for fileName in fileNames:
        x = range(1, len(delays[fileName]))
        ax.plot(x, delays[fileName][1:], '-', color=colors[fileName])

    ax.set_xlabel("Simulation Time (seconds)")
    ax.set_ylabel(r"Forwarding Delay ($\mu$sec)")
    ax.grid(True)
    ax.legend(legendLabels, loc=1)

    print "Saving the plot..."
    pdf = PdfPages("no_cache_dfn_comparison.pdf")
    pdf.savefig(fig)
    pdf.close()

if __name__ == "__main__":
    main(sys.argv)

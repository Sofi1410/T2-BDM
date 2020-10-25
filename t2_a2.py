import numpy as np
import matplotlib.pyplot as plt
dist=[59,10,60,10,11,10,59,10,96258]
camel=[0,58]
gato=[59,68]
elephant=[69,128]
faces=[129,138]
flamingo=[139,149]
head=[150,159]
caballo=[160,218]
lion=[219,228]
otros=[229,96486]
names=[camel,gato,elephant,faces,flamingo,head,caballo,lion,otros]
data = np.loadtxt("./algoritmo2.txt")
##print(len(data)) arroja 229
##print(len(data[0])) 96487
n=1
R=np.zeros(11)
P=np.zeros(11)
for a in range(0,9):
    for num in range(names[a][0],names[a][1]):
        distancesinorder = np.argsort(data[num])
        relevant = np.zeros((dist[a]), int)
        for a in range(0, dist[a]):
            relevant[a] = distancesinorder[a]

        start = np.zeros((96487), dtype=np.uint8)
        start[relevant] = 1

        precision = []
        recall = []

        cont = 0
        for i in range(start.shape[0]):
            if start[i] == 1:
                cont = cont + 1
            precision.append(cont / (i + 1))
            recall.append(cont / len(relevant))

        recall = [val * 100 for val in recall]
        numBins = 10
        currentRecall = 100 - 100 / numBins
        maxPrec = precision[-1]
        precision_recall = np.zeros((numBins + 1))
        recall2 = np.zeros((numBins + 1))
        pos = numBins
        precision_recall[pos] = maxPrec
        recall2[pos] = 100
        cont = len(precision) - 2
        pos = pos - 1

        while cont >= 0:
            if recall[cont] >= currentRecall:
                if precision[cont] > maxPrec:
                    maxPrec = precision[cont]
                cont = cont - 1
            else:
                precision_recall[pos] = maxPrec
                recall2[pos] = currentRecall
                currentRecall = currentRecall - numBins
                pos = pos - 1

        while pos >= 0:
            precision_recall[pos] = maxPrec
            pos = pos - 1

        recall2 = recall2 / 100
        R+=recall2
        P+=precision_recall

P=P/229
R=R/229




plt.figure()
plt.plot(P, R, 'bo--')
plt.grid(True)
plt.show()
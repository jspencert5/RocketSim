from matplotlib import pyplot as plt

def createGraph(y,x, path, title, ylabel, xlabel, c, figNum):
    plt.figure(figNum)
    plt.plot(x,y, color=c)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(path, bbox_inches='tight')
    figNum = figNum + 1
    #plt.show()

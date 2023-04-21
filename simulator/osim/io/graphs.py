from matplotlib import pyplot as plt

def createGraph(x,y, path):
    plt.plot(y,x)
    plt.savefig(path, bbox_inches='tight')
    #plt.show()




import numpy as np
import matplotlib
matplotlib.rcParams["backend"] = "tkagg"
import matplotlib.pyplot as plt

class Plot:
    def __init__(self,a):
        self.a=a

    def plotize(self):
        np.random.seed(1)
        arr1 = np.cumsum(np.random.randint(1,10,self.a))
        arr2 = np.cumsum(np.random.randint(1,10,self.a))
        new_arr = np.array([])

        for i in list(zip(arr1,arr2)):
            new_arr = np.append(i,new_arr)
            plt.xlim(0,100)
            plt.ylim(0,100)
            plt.plot(new_arr.reshape(2,-1,order="F")[0] ,
                     new_arr.reshape(2,-1,order="F")[1])
            plt.pause(1)
        plt.show()


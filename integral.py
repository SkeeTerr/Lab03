from scipy import integrate
import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

class Input(object):
    def __init__(self):
        """Constructors"""
        #Верхня межа інтегрування
        self.up
        #Нижня межа інтегрування        
        self.down
        #Функція для інтегрування        
        self.function = lambda x: 6*(x**2)+6*x+1
    
    #Метод повертає параметри інтегрування
    def returnintegral(self):
        self.down = int(input('Вкажіть нижню межу інтегрування інтегрування:\n'))
        self.up = int(input('Вкажіть верхню межу інтегрування:\n'))


            

class Calculation(Input):
    def __init__(self):
        """Constructors"""
        #Результат інтегрування
        self.v
        #Похибка інтегрування
        self.err
        #Функція для інтегрування
        self.function = lambda x: 6*(x**2)+6*x+1
    
    #Метод інтегрування
    def integration(self):
        self.v, self.err = integrate.quad(self.function, self.down, self.up)

        
class Output(Calculation):
    def __init__(self):
        """Constructors"""
        #Функція для інтегрування
        self.function = lambda x: 6*(x**2)+6*x+1
    
    #Метод, що виводить результати інтегрування в консоль
    def outfunction(self):
        print("Результат інтегрування функції 6*(x^2)+6*x+1: " + str(self.v))
        print("Похибка інтегрування функції складає інтегрування функції 6*(x^2)+6*x+1: " + str(self.err))

    #Метод, який виводить графічне зобрження функції
    def showfunction(self):
        fig, ax = plt.subplots(figsize=(8,3))
        x = np.linspace(self.down,self.up, 10000)
        ax.plot(x, self.function(x), lw=2)
        ax.fill_between(x, self.function(x), color='green', alpha=0.5)
        ax.set_xlabel("x,X", fontsize=18)
        ax.set_ylabel("f(x),f(X)", fontsize=18)
        ax.set_ylim(0, 1500)
        plt.show()

Func = Output()
Func.returnintegral()
Func.integration()
Func.outfunction()
Func.showfunction()
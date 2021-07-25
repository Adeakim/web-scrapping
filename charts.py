import matplotlib.pyplot as plt
from abc import ABC,abstractmethod
from graphvalues import *

class ChartInterface(ABC):
    '''this is the class providing interface to draw the barchart and piechart'''
    @abstractmethod
    def piechart(self):
        pass
    
    @abstractmethod
    def barchart(self):
        pass
class DrawChart(ChartInterface,GetGraphValues):
    '''This is the class that is plotting the graph from the values gotten from 
    GetGraphValues class'''
    def piechart(self):
        '''Function to draw the pie chart'''
        plt.xlabel('common words')
        plt.ylabel('frequency')
        plt.title('bar chart showing frequency of most used common words')
        plt.bar(self.x_axis_values(), self.y_axis_values()) 
        return plt.show()
        
    def barchart(self):
        '''Funtion to draw the barchart'''
        plt.pie(self.y_axis_values(),labels=self.x_axis_values(),autopct='%1.1f%%')
        return plt.show()

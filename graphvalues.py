from getwebsite import *
from analyzeweb import *


class GetGraphValues(AnalyzeWeb):
    def x_axis_values(self):
        x_axis=[item[0] for item in self.countwords()]
        return x_axis
    def y_axis_values(self):
        y_axis=[item[1] for item in self.countwords()]
        return y_axis
    
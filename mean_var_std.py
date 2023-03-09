import numpy as np
import math

def calculate(list):
    if len(list) != 9:
        return 'List must contain nine numbers.'
    else:
        results = {}
        
        array = np.array(list).reshape((3,3))
        
        rows_mean = []
        rows_var = []
        rows_std = []
        rows_max = []
        rows_min = []
        rows_sum = []
        for i in array:
            rows_mean.append(i.mean())
            rows_var.append(i.var())
            rows_std.append(i.std())
            rows_max.append(i.max())
            rows_min.append(i.min())
            rows_sum.append(i.sum())
        print(rows_mean)
        print(rows_var)
        print(rows_std)
        print(rows_max)
        print(rows_min)
        print(rows_sum)
        
        col_mean = []
        col_var = []
        col_std = []
        col_max = []
        col_min = []
        col_sum = []
        for i in array.T:
            col_mean.append(i.mean())
            col_var.append(i.var())
            col_std.append(i.std())
            
        return array
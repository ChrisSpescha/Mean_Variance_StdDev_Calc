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
            col_max.append(i.max())
            col_min.append(i.min())
            col_sum.append(i.sum())
        
        result = {'mean' : [col_mean, rows_mean, array.mean()],
                 'variance': [col_var, rows_var, array.var()],
                 'standard deviation': [col_std, rows_std, array.std()],
                 'max': [col_max, rows_max, array.max()],
                 'min': [col_min, rows_min, array.min()],
                 'sum': [col_sum, rows_sum, array.sum()],
                 }
        return result
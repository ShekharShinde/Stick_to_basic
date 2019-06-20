# -*- coding: utf-8 -*-

#%%
def mean(x):
    return sum(x)/len(x)

def median(x):
    x.sort()
    n=len(x)
    return ((x[(n//2)]) if n%2!=0 else ((x[n//2 - 1] + x[n//2]) / 2))

def mode(x):
    unique = list(set(x))
    unique.sort()
    freq=[]
    for i in unique:
        freq.append(x.count(i))
    return unique[freq.index(max(freq))], max(freq)

def var(x):
    x_bar = mean(x)
    return sum((xi - x_bar) ** 2 for xi in x) / len(x)

def std(x):
    return var(x)**0.5

def cov(x,y):
    n1, n2 = len(x), len(y)
    try:
        assert n1 == n2
        x_bar = mean(x)
        y_bar = mean(y)
        return (sum((x[i]-x_bar)*(y[i]-y_bar) for i in range(n1)) / n1)
    except AssertionError:
        return print('length_mismatch')

def pearsonCorrCoeff(x,y):
    covarience = cov(x,y)
    std_x = std(x)
    std_y = std(y)
    return covarience/(std_x * std_y)
#%%
#Creating data
import random
mylist = []
for i in range(0,100):
    x = random.randint(1,10)
    mylist.append(x)

arr1 = mylist[:50]
arr2 = mylist[50:]
#%%
#Displaying stat properties calculated using user defiend functions
print('mean = ',mean(arr1))
print('median = ',median(arr1))
print('mode, freq = ',*mode(arr1))
print('var = ',round(var(arr1),4))
print('std = ',round(std(arr1),4))
print('pearsonCorrCoeff = ',round(pearsonCorrCoeff(arr1,arr2),4))
print('covarince = ',round(cov(arr1,arr2),4), '\n')

#%%
#Displaying stat properties calculated using default functions

from scipy import stats
import numpy as np

print('inbuilt_mean = ',np.mean(arr1))
print('inbuilt_median = ',np.median(arr1))
print('inbuilt_mode, freq = ',*stats.mode(arr1))
print('inbuilt_var = ',round(np.var(arr1),4))
print('inbuilt_std = ',round(np.std(arr1),4))
print('inbuilt_pearsonCorrCoeff = ',round(stats.pearsonr(arr1,arr2)[0],4), '\n')

#%%












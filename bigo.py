# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 09:20:42 2018

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np

def f(n):
    return 1000*n+3000
def g(n):
    return 0.6*n**2

x = np.linspace(0,5000)

plt.plot(x,f(x),'r',label='1000n +3000')
plt.legend()
plt.plot(x,g(x),'b',label ='0.6$n^2$')
plt.legend()
plt.grid(b=True, which='major', axis='both')
plt.xlim(0,5000)
plt.show()
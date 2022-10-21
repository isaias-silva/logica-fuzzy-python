# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:17:36 2022

@author: alunoead
"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


#variaveis universo
x_sinal=np.arange(0,101,1)
#sinais
sinal_fraco=fuzz.trapmf(x_sinal,[0,0,10,30])
plt.figure()

sinal_medio=fuzz.trapmf(x_sinal,[30,40,60,70])
sinal_forte=fuzz.trapmf(x_sinal,[70,90,100,100])

plt.plot(x_sinal,sinal_fraco)
plt.plot(x_sinal,sinal_medio)
plt.plot(x_sinal,sinal_forte)
plt.xlabel("sinal")
plt.ylabel("intensidade")
plt.savefig("fig.png")
import control as ct
import matplotlib.pyplot as plt
import numpy as np

R=3.4
L = 0.0015
J = 0.00040095
B = 1.00223579
Kv = 0.23351629
Km = 0.23351629

G = ct.tf([Km/J/L],[1,R/L,Km*Kv/J/L,0])
print(G)

#ct.root_locus(G)
#plt.show()

Kp = 2
T = ct.tf([Km*Kp/J/L],[1,R/L,Km*Kv/J/L,Km*Kp/J/L])
print(T.poles())

t = np.arange(0,1,0.0001)
res = ct.forced_response(T,t,t)
plt.plot(res.t,res.y[0],t,t)
plt.show()
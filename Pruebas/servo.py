import numpy as np 
import matplotlib.pyplot as plt
import control as ct

R = 2.27 #Ω
L = 0.0047 #H	
B = 0.003026 #kg.m2/s
J = 0.00246 #kg. m2	
Kb = 0.25 #V/rad/s
Km = 0.25 #N.m/A

sysla = ct.tf([Km/J/L],[1,R/L,Kb*Km/J/L,0])
print(sysla)
#ct.root_locus(sysla)
#plt.show()
K = 0.5 # float(input('valor de k = '))
syslc = ct.tf([Km*K/J/L],[1,R/L,Kb*Km/J/L,Km*K/J/L])
plt.figure()
res=ct.step_response(syslc)
#plt.plot(res.t,res.outputs[:])
#plt.show()
print(res.outputs[:])

print(syslc.poles())

t=np.arange(0,1,0.0001)
resr = ct.forced_response(syslc,t,t**2)
print(resr.y)
plt.plot(resr.t,resr.y[0])
plt.show()

import control as ct
import matplotlib.pyplot as plt
G = ct.tf([1],[1,2,3,0])
print(G)

ct.root_locus(G)
plt.show()
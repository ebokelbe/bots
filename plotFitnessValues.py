import numpy as np
import matplotlib.pyplot as plt
import constants as c

AFitnessValues = np.load('fitnessValuesA.npy')
BFitnessValues = np.load('fitnessValuesB.npy')
avgA = np.mean(AFitnessValues, axis=0, dtype=np.float64)
sA = np.std(AFitnessValues, axis=0, dtype=np.float64)
avgB = np.mean(BFitnessValues, axis=0, dtype=np.float64)
sB = np.std(BFitnessValues, axis=0, dtype=np.float64)

plt.plot(avgA-sA, color='red')   
plt.plot(avgA, color='red', label='A mean fitness (base quadruped)')
plt.plot(avgA+sA, color='red')  
    
plt.plot(avgB-sB, color='green')  
plt.plot(avgB, color='green', lw=1, label='B mean fitness (runway quadruped)')
plt.plot(avgB+sB, color='green')  

#plt.plot(backTargetAngles, lw=3, label='Back Target Angles')
#plt.plot(row1, label='A Values Row 1')
plt.legend()
plt.show()

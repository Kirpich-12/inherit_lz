import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
  
'''
fig, ax = plt.subplots()
fig1 = Rectangle((0, 0), 1, 1, lw = 10, color = 'red')
ax.plot(fig1)
ax.grid()
plt.show()
'''

fig = plt.figure() 
ax = fig.add_subplot(111) 
ax.add_patch( Rectangle((0, 0), 1, 1, fill = 0, ec ='g', lw = 10) ) 
plt.show()
import numpy as np
import matplotlib.pyplot as plt

font = {'family'	: 'cmr10',
		'size'		: '10'}

plt.matplotlib.rc('font',**font)


g = 9.81 # m/s^2
y0 = 5
t1 = np.sqrt(2*y0/g)

t = np.linspace(0,t1,100)
y = y0-0.5*g*t**2

plt.figure(figsize=(4,3), dpi=300)
plt.plot(t,y)
plt.grid()
plt.xlabel('Time [s]')
plt.ylabel('Position [m]')
#plt.title('Falling object')

#fig = plt.gcf()	# Get Current Figure

plt.show()	

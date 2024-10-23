import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,20,10)
y1=x
print(y1)
y2=np.square(x)
print(y2)
y3=np.sqrt(x)
print(y3)
plt.plot(x,y1,'red',x,y2,'green',x,y3,'blue')
plt.legend(['X','Square(x)','Sqrt(x)'])
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Linear_Vikas_1KI23CS180")
plt.xticks(x)
plt.yticks(y2)
plt.show()
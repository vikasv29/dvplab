import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def sinplot(n=5):
    x=np.linspace(0,30,5)
    for i in range(1,n+1):
        plt.plot(x,np.sin(x+i*0.5)*(n+2)-i)
sinplot()
plt.title("Vikas V_1KI23CS180_Aesthetic function plot")
sns.set_context("talk")
plt.show()
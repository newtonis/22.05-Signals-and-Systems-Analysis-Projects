import numpy as np
import matplotlib.pyplot as plt
import math
def woodenv(att,sus,rel,fs):
    #att = attack time es como 5tau
    tau_att = att/5
    tau_rel = rel/5
    # = > t_att = 1-exp(-t/tau)
    total_t = att+sus+rel
    t = np.linspace(0, total_t, num=fs)
    y1 = np.zeros(len(t))
    y2 = np.zeros(len(t))
    for index,ti in enumerate(t):
        if(ti<=att):
            t2 = att
            alpha = (math.log(2))/t2
            y1[index] = np.exp(alpha*ti)-1
            y2[index] = np.exp(alpha*ti)-1
        elif( att<ti and ti<att+sus ):
            y1[index] = 1
            y2[index] = 1
        elif(ti>=att+sus and ti<att+sus+rel/2):
            tau = (rel/2)*(1/(5-math.log(2)))
            taux = ti-(att+sus)
            taux2 = rel/2-taux  # taux2 hace que el tiempo vaya de rel/2 a 0
            taux2 = (5*tau-rel/2)+taux2 # y ahora hacemos que vaya de 5tau a t2=ln(2)tau
            y1[index]=1-np.exp(-(taux2)/tau)
            y2[index] = 1
        elif(ti>=att+sus+rel/2):
            tau = (rel/2)/5
            y1[index] = (1/2)*np.exp(-(ti-(att+sus+rel/2))/(tau))
            y2[index] = 1
    return t,y1,y2

t,y1,y2 = woodenv(0.5,0.5,0.5,8000)
plt.plot(t,y1)
plt.show()
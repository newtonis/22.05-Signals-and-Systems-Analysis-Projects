import numpy as np
import matplotlib.pyplot as plt
def woodenv(att,sus,rel,fs):
    #att = attack time es como 5tau
    tau_att = att/5
    tau_rel = rel/5
    # = > t_att = 1-exp(-t/tau)
    total_t = att+sus+rel
    t = np.linspace(0, total_t, num=fs)
    y1 = np.zeros(len(t))
    for index,ti in enumerate(t):
        if(ti<=att):
            y1[index] = 1-(np.exp(-ti/(tau_att)))
        if( att<ti and ti<att+sus ):
            y1[index] = 1-np.exp(-5)
        elif(ti>=att+sus):
            y1[index] = np.exp(-(ti-(att+sus))/(tau_rel))

    return t,y1

t,y1 = woodenv(0.5,0.5,0.5,8000)
plt.plot(t,y1)
plt.show()
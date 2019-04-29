from numpy import *


def linScale(ynorm,alpha,beta):
    y = alpha*ynorm + beta
    return y


def woodEnv(att,sus,rel,fs):
    #att = attack time es como 5tau
    tau_att = att/5
    tau_rel = rel/5
    # = > t_att = 1-exp(-t/tau)

    total_t = att+sus+rel
    t = arange(0, total_t, 1/fs)
    y1 = zeros(len(t))
    y2 = zeros(len(t))
    for index,ti in enumerate(t):
        if(ti<=att):
            t2 = att
            alpha = (math.log(2))/t2
            y1[index] = exp(alpha*ti)-1
            y2[index] = exp(alpha*ti)-1
        elif( att<ti and ti<att+sus ):
            y1[index] = 1
            y2[index] = 1
        elif(ti>=att+sus and ti<att+sus+rel/2):
            tau = (rel/2)*(1/(5-math.log(2)))
            taux = ti-(att+sus)
            taux2 = rel/2-taux  # taux2 hace que el tiempo vaya de rel/2 a 0
            taux2 = (5*tau-rel/2)+taux2 # y ahora hacemos que vaya de 5tau a t2=ln(2)tau
            y1[index]=1-exp(-(taux2)/tau)
            y2[index] = 1
        elif(ti>=att+sus+rel/2):
            tau = (rel/2)/5
            y1[index] = (1/2)*exp(-(ti-(att+sus+rel/2))/(tau))
            y2[index] = 1
    return y1,y2

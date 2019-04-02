import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from cmath import *
from math import *

def read_csv(filename):
    data = dict()
    data["t"] = []
    data["vin"] = []
    data["vout"] = []

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["x-axis"] != "second":
                data["t"].append(float(row["x-axis"]) )
                data["vout"].append(float(row["1"]) )
                data["vin"].append(float(row["3"]) )

    return data


def read_csv_bode(filename):
    data = dict()

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                for content in row.keys():
                    if not content in data:
                        data[content] = []

                    data[content].append(float(row[content]))
            except ValueError:
                pass
    return data


def getfreq(x,y,threshhold):
    sum = 0
    total = 0
    status = 0
    last = -1
    for i in range(len(y)):
        if status == 0 and y[i] < threshhold:
            status = 1
            if last != -1:
                sum += x[i] - last
                total += 1
            last = x[i]
        elif status == 1 and y[i] > threshhold:
            status = 0
    #if sum != 0:
    #    print(total / sum)
    return total/sum

def getfreq2(x,y,threshhold,err):
    state = "not found"
    t1 = 0
    t2 = 0
    for i in range(len(y)):
        if y[i]>threshhold and state== "not found":
            state = "found first"
            t1 = x[i]
        if((x[i]-t1)>err):
            if y[i]>threshhold and state== "found first":
                state = "found two"
                t2 = x[i]
    return 1/(t2-t1)

#hay que tener cuidado con el err, tiene que ser para el duty y funciona
# def getduty(x,y,flanco,freq):
#     state = "not found"
#     t1 = 0
#     t2 = 0
#     pos_edge_cnt = 0
#     neg_edge_cnt = 0
#
#     max_pos = 20
#     max_neg = 20
#     yaux = y.copy()
#     yaux.reverse()
#
#     for i in range(1,len(y)):
#         if(state == "not found"):
#             if abs(y[i]-y[i-1]) > flanco:
#                 pos_edge_cnt+=1
#             if pos_edge_cnt>0 and abs(y[i]-y[i-1])< flanco:
#                 pos_edge_cnt=0
#             if(pos_edge_cnt>max_pos):
#                 state = "found first"
#                 t1 = x[i]
#
#         if(state == "found first"):
#             if abs(yaux[i]-yaux[i-1]) > flanco:
#                 neg_edge_cnt+=1
#             if neg_edge_cnt>0 and abs(yaux[i]-yaux[i-1])< flanco:
#                 neg_edge_cnt=0
#
#
#             if(neg_edge_cnt>max_neg):
#                 state = "found two"
#                 t2 = x[i]
#
#     T = 1 / freq
# #    t2 = t2-T
#     print(t1)
#     print(t2)
#     ton = t2-t1
#     duty = (ton/T)*100
#     return duty





def plotfunc(xtitle,ytitle,xvector,yvector,graphlabel):
    plt.plot(xvector, yvector,label=graphlabel)
   # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    plt.xlim(xvector[0], xvector[-1])
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

% Calculo de Funcion transferencia Denormalizada %
clc;
s = tf('s');
wp = 2*pi*1100;
A = ((s/wp)^2 + 0.5548*(s/wp) +0.2702).*((s/wp)^2 + 0.0918*(s/wp) + 0.9870).*((s/wp)^2 + 0.4284*(s/wp) + 0.5282).*((s/wp)^2 + 0.2650*(s/wp) + 0.8013).*((s/wp)^2 + 0.6344*(s/wp) + 0.1218);
H = 1/(72.*A);

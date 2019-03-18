% Filtro LP - Orden 10 Legendre %
% Ap = 0.9dB y As = 42dB %
clc;

Q1 = 9.06;
Wo1 = 2*pi*1621.86;
Q2 = 2.82;
Wo2 = 2*pi*1472.99;
Q3 = 1.45;
Wo3 = 2*pi*1214.37;
Q4 = 0.84;
Wo4 = 2*pi*902.65;
Q5 = 0.54;
Wo5 = 2*pi*658.14;

% Circuito 1

C_12a = 100e-9;
R_12a = 1/(Wo1*C_12a);
R_3a = 3.3e3;
R_4a = R_3a*(2*Q1 - 1);
R_56a = 10e3;

% Circuito 2

C_2 = 100e-9;
R_2 = 1/(Wo2*C_2);
R_A2 = 1.2e3;
R_B2 = (2-(1/Q2))*R_A2;

% Circuito 3

C_3 = 100e-9;
R_3 = 1/(Wo3*C_3);
R_A3 = 1.2e3;
R_B3 = (2-(1/Q3))*R_A3;

% Circuito 4

C_4 = 100e-9;
R_4 = 1/(Wo4*C_4);
R_A4 = 1.5e3;
R_B4 = (2-(1/Q4))*R_A4;

% Circuito 5

C_5 = 100e-9;
R_5 = 1/(Wo5*C_5)
R_A5 = 15e3;
R_B5 = (2-(1/Q5))*R_A5
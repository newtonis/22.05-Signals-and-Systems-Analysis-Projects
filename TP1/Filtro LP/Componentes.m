% Filtro LP - Orden 8 Legendre %
% Ap = 1dB y As = 41dB
clc;

Q1 = 6.04;
Wo1 = 2*pi*1021.08;
Q2 = 1.84;
Wo2 = 2*pi*887.46;
Q3 = 0.91;
Wo3 = 2*pi*673.85;
Q4 = 0.54;
Wo4 = 2*pi*487.96;

% Circuito 1

C_12a = 100e-9;
R_12a = 1/(Wo1*C_12a);
R_3a = 1.8e3;
R_4a = R_3a*(2*Q1 - 1);
R_56a = 10e3;

% Circuito 2

C_2 = 100e-9;
R_2 = 1/(Wo2*C_2);
R_A2 = 1.5e3;
R_B2 = (2-(1/Q2))*R_A2;

% Circuito 3

C_3 = 100e-9;
R_3 = 1/(Wo3*C_3);
R_A3 = 1.2e3;
R_B3 = (2-(1/Q3))*R_A3;

% Circuito 4

C_4 = 100e-9;
R_4 = 1/(Wo4*C_4);
R_A4 = 15e3;
R_B4 = (2-(1/Q4))*R_A4;
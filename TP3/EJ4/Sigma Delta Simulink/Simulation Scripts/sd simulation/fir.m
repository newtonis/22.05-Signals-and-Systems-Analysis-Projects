clear;
clc;
wn = 0.15;
fs = 512000;
N = 31; % orden de la ventana de hamming 
c=fir1(N,wn); % n y wn 
% N y wn =fc/(fs/2)
%fc = wn*fs/2  % frec de corte del filtro fir
% uses a Hamming window to design an nth-order
% lowpass, bandpass, or multiband FIR filter with linear phase.
% The filter type depends on the number of elements of Wn.
%freqz(c,1,512); % b a n
H1 = dfilt.df2t(c,1);
H2 = dfilt.df2t(c,1);
H3 = dfilt.df2t(c,1);
Hcas1 = dfilt.cascade(H1,H2,H3);
%Hcas2 = dfilt.df2t(Hcas1,H3);


%[b1,a1]=butter(8,0.6);          % Lowpass
%[b2,a2]=butter(8,0.4,'high');   % Highpass
%H1=dfilt.df2t(b1,a1);
%H2=dfilt.df2t(b2,a2);
%Hcas=dfilt.cascade(H1,H2)  
freqz(Hcas1)
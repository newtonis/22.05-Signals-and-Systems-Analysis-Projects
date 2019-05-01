//
// Created by newtonis on 4/30/2019.
//

#include "Reverb.h"
#include "WavFile.h"
#include <iostream>
using namespace std;


Reverb::Reverb(
        unsigned int sampleRate,
        unsigned int framesPerBuffer,
        unsigned int windowWidth,
        int mode,
        map<string,int> &config
        ): AudioEffect(
            sampleRate,
            framesPerBuffer,
            windowWidth/2),
            windowedData(windowWidth),
            transform(windowWidth) {
    this->mode = mode;
    this->windowWidth = windowWidth;
    this->start = true;
    this->config = config;
    this->impulseLength = 20000;

    loadWavFile("impulse/Factory Hall.wav", outputA, outputB, impulseLength);

    for (int i = 0;i < DP_MAX;i++){
        for (int j = 0;j < MAX_REB;j++){
            aux[i][j] = 0;
            comb_aux[i][j] = 0;
        }
    }

    for (int i = 0;i < MAX_BUFFER_SIZE;i++){
        last_x[i] = 0; // z[0] el anterior, z[1] el ante-anterior etc
        last_y[i] = 0;
        last_z[i] = 0;

    }
    for (int i = 0;i < 12;i++) {
        D.push_back(53); //0.0012f*44100
    }

    comb_count = 4;
    for (int i = 0;i < comb_count;i++){
        combD.push_back(500);
        combA.push_back(0.5);
    }
    a = 0.99;
}

void Reverb::processInput(CircularBuffer& in, CircularBuffer& out){
    if (mode == ECO) {
        eco(in, out);
    }else if(mode == PLANO){
        reverbPlano(in, out);
    }else if(mode == PASABAJO){
        reverbPlanoPB(in, out);
    }else if(mode == CONVOLUCION){
        reverbConvolution(in, out);
    }else if(mode == COMPLETO){
        reverbSchroeder(in, out);
    }
}

void Reverb::eco(CircularBuffer& in, CircularBuffer& out){
    float g = 0.999;
    int m = 5000;

    int i = 0;
    while (in.currSize() > 0){
        float actual = in.next();

        float salida = actual + g * last_x[i%m];

        last_x[i%m] = actual;
        last_y[i%m] = salida;
        i ++;
        out.push_back(salida);
    }
}

void Reverb::reverbPlano(CircularBuffer& in, CircularBuffer& out){
    float g = 0.5;
    int m = 5000;

    int i = 0;
    while (in.currSize() > 0){
        float actual = in.next();

        float salida = actual + g * last_y[i%m];

        last_x[i%m] = actual;
        last_y[i%m] = salida;
        i ++;
        out.push_back(salida);
    }
}

void Reverb::reverbPlanoPB(CircularBuffer& in, CircularBuffer& out){
    float g = 0.5;
    int m = 5000;


    int i = 100;
    while (in.currSize() > 0){
        float x = in.next();
        float z = g * last_y[(i-m)%m];
        float y = x + (last_z[i%m] + last_z[(i-1)%m])/2; // filtro pb

        out.push_back(y);

        i ++;

        last_x[(i-1)%m] = x;
        last_y[(i-1)%m] = y;
        last_z[(i-1)%m] = z;
    }


}

void Reverb::reverbConvolution(CircularBuffer &in, CircularBuffer &out) {

    for (int i = 0;i < impulseLength;i++){
        last_x[i] = 0;
    }
    int i = impulseLength;

    while (in.currSize() > 0){
        float ans = 0;
        float x = in.next();
        for (int index = 0; index < impulseLength;index ++){
            ans += outputA[index] * last_x[(i - index)%impulseLength];
        }
        i ++;
        last_x[(i - 1)%impulseLength] = x;
        out.push_back(ans);
    }

}
void Reverb::reverbSchroeder(CircularBuffer& in, CircularBuffer& out){
    int i = DP_MAX * 20;
    int d = DP_MAX;

    while (in.currSize() > 0){
        float x = in.next();
        float y = 0;

        for (int j = 0;j < D.size();j++){
            y += last_x[(i-D[j])%d] + aux[(i-D[j])%d][j] * this->a;
        }
        last_x[i%d] = x;
        last_y[i%d] = y;


        for (int j = 0;j <= comb_count;j++){
            if (j != 0) {
                int cur_d = combD[j-1];
                float cur_a = combA[j-1];

                comb_aux[i % d][j] = \
                    -cur_a * comb_aux[i % d][j - 1] + \
                    comb_aux[(i - cur_d) % d][j - 1] + \
                    cur_a * comb_aux[(i - cur_d) % d][j];

            }else{
                comb_aux[i % d][j] = last_y[i % d];
            }

        }
        out.push_back(comb_aux[i % d][comb_count]);

        i++;
    }

}
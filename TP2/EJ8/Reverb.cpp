//
// Created by newtonis on 4/30/2019.
//

#include "Reverb.h"
#include "WavFile.h"


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
    this->impulseLength = 500;

    loadWavFile("impulse/Factory Hall.wav", outputA, outputB, impulseLength);

}

void Reverb::processInput(CircularBuffer& in, CircularBuffer& out){
    if (mode == ECO) {
        eco(in, out);
    }else if(mode == PLANO){
        reverbPlano(in, out);
    }else if(mode == PASABAJO){
        reverbPlanoPB(in, out);
    }
}

void Reverb::eco(CircularBuffer& in, CircularBuffer& out){
    float g = 0.999;
    int m = 5000;

    for (int i = 0;i < m;i++){
        last_x[i] = 0; // z[0] el anterior, z[1] el ante-anterior etc
        last_y[i] = 0;
    }
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

    for (int i = 0;i < m;i++){
        last_x[i] = 0; // z[0] el anterior, z[1] el ante-anterior etc
        last_y[i] = 0;
    }
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

    for (int i = 0;i < m;i++){
        last_x[i] = 0; // z[0] el anterior, z[1] el ante-anterior etc
        last_y[i] = 0;
        last_z[i] = 0;
    }
    int i = 100;
    while (in.currSize() > 0){
        float x = in.next();
        float z = g * last_y[(i-m)%m];
        float y = x + (last_z[i%m] + last_z[(i-1)%m])/2; // filtro pb

        out.emplace(y);

        i ++;

        last_x[(i-1)%m] = x;
        last_y[(i-1)%m] = y;
        last_z[(i-1)%m] = z;
    }


}

void Reverb::reverbConvolution(CircularBuffer &in, CircularBuffer &out) {
    float g = 0.5;

    while (in.currSize() > 0){
        float ans = 0;
        float act = in.next();
        for (int index = )
    }



}
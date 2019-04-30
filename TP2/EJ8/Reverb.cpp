//
// Created by newtonis on 4/30/2019.
//

#include "Reverb.h"



Reverb::Reverb(
        unsigned int sampleRate,
        unsigned int framesPerBuffer,
        unsigned int windowWidth,
        int mode): AudioEffect(
            sampleRate,
            framesPerBuffer,
            windowWidth/2),
            windowedData(windowWidth),
            transform(windowWidth) {
    this->mode = mode;
    this->windowWidth = windowWidth;
    this->start = true;
}

void Reverb::processInput(CircularBuffer& in, CircularBuffer& out){
    if (mode == ECO) {
        eco(in, out);
    }else if(mode == PLANO){
        reverbPlano(in, out);
    }




    /*while (in.currSize() >= windowWidth) { // agarro las ventanas que pueda
        windowedData.clear();
        for (unsigned int i = 0; i < windowWidth; i++) {
            windowedData.emplace(in.read(i)); // agarro una ventana
        }
        //in.pop(windowWidth/2); // overlap de 50%
        in.pop(windowWidth); // no overlap
        processWindow(windowedData, out);
    }*/

    /*int index = 0;
    int size = in.currSize();
    while (in.currSize() > 0){
        last_x[index] = x[index];
        x[index] = in.next();
        index ++;
    }



    for (int n = 0;n < size;n++) {
        if (n < m) {
            if (start) {
                y[n] = last_x[n - m + size] - g * x[n] + g * y[n - m + size];
            } else {
                y[n] = g * x[n];
            }
            continue;
        }
        y[n] = x[n - m] - g * x[n] + g * y[n - m];
        if (n > 0) {
            out.emplace((y[n] + y[n - 1]) / 2);
        }else{
            out.emplace(y[n]);
        }
    }
    if (this->start){
        this->start = false;
    }*/

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
        out.emplace(salida);
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
        out.emplace(salida);
    }
}


void Reverb::processWindow(CircularBuffer& in, CircularBuffer& out){


}

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

}

void Reverb::processInput(CircularBuffer& in, CircularBuffer& out){
    while (in.currSize() >= windowWidth) { // agarro las ventanas que pueda
        windowedData.clear();
        for (unsigned int i = 0; i < windowWidth; i++) {
            windowedData.emplace(in.read(i)); // agarro una ventana
        }
        in.pop(windowWidth/2); // overlap de 50%
        //in.pop(windowWidth); // no overlap
        processWindow(windowedData, out);
    }
}

void Reverb::processWindow(CircularBuffer& in, CircularBuffer& out){
    int index = 0;
    int size = in.currSize();
    while (in.currSize() > 0){
        x[index] = in.next();
        index ++;
    }
    float g = 0.99;
    int m = 5;

    for (int n = 0;n < size;n++){
        if (n < m){
            y[n] = -g * x[n];
            continue;
        }

        y[n] = x[n] -g * x[n] + x[n - m] + g * y[n - m];

        out.emplace(y[n]);
    }
}
//
// Created by Rocío Parra on 26-Apr-19.
//

#include "Robotization.h"
#include "my_fft.h"
#include "windows.h"
#include <iterator>
#include <iostream>

using namespace std;

Robotization::Robotization(
        unsigned int sampleRate,
        unsigned int framesPerBuffer,
        unsigned int windowWidth) :
        AudioEffect(
                sampleRate,
                framesPerBuffer,
                windowWidth/2),
                windowedData(windowWidth), transform(windowWidth) {

    this->windowWidth = windowWidth;
    hanning(windowWidth, window);
//    for (auto it = window.begin(); it != window.end(); it++) {
//        cout << *it << endl;
//    }
}



void Robotization::processInput(CircularBuffer& in, CircularBuffer& out)
{
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

void Robotization::processWindow(CircularBuffer& in, CircularBuffer& out) {
    for (unsigned int i = 0; i < windowWidth; i++) {
        //transform[i] = complex<float>(in.read(i),0);
        transform[i] = complex<float>(in.read(i)*window[i], 0);
    } // guardo en transform el input para no generar otro arreglo mas

    fft(transform, transform); // ahora si en transform tengo el valor apropiado
    for (unsigned int i = 0; i < windowWidth; i++) {
        complex<float> zeroPhase(abs(transform[i]), 0);
        transform[i] = zeroPhase;
    }

    ifft(transform, transform);
    // ahora en transform esta  la salida, tambien para no hacer otro arreglo


    unsigned int outSize = out.currSize();
    if (outSize < windowWidth/2) {
        //si no tengo suficientes muestras todavia no puedo superponerlas!
        //esto deberia pasar solo la primera vez
        for (unsigned int i = 0; i < windowWidth/2; i++) {
            out.emplace(transform[i].real());
        }
    }
    else {
        //sumo la salida de la segunda mitad de la ventana anterior con la primera mitad de esta
        for (unsigned int i = outSize-windowWidth/2, j = 0; i < outSize; i++, j++) {
            out.write(i, out.read(i)+transform[j].real());
        }
    }

    for (unsigned int i = windowWidth/2; i < windowWidth; i++) {
        //estos datos se tienen que sumar con la primera mitad de la proxima ventana
        out.emplace(transform[i].real());
    }
}


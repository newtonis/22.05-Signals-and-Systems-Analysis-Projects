//
// Created by newtonis on 4/30/2019.
//

#ifndef EJ8_REVERB_H
#define EJ8_REVERB_H


#include "AudioEffect.h"
#include <complex>

using namespace std;


#define MAX_BUFFER_SIZE     (4096)

enum{
    SIMPLE,
    PLANO,
    PASABAJO
};


class Reverb : public AudioEffect {
    public:
        Reverb(unsigned int sampleRate, unsigned int framesPerBuffer, unsigned int windowWidth, int mode);
        void processInput(CircularBuffer& in, CircularBuffer& out);
        void processWindow(CircularBuffer& in, CircularBuffer& out);

    protected:
        float x[MAX_BUFFER_SIZE];
        float y[MAX_BUFFER_SIZE];
        int mode;

        unsigned int windowWidth;

        std::vector<float> window;
        CircularBuffer windowedData;
        std::vector<complex<float>> transform;

};


#endif //EJ8_REVERB_H

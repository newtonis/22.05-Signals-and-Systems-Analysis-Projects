//
// Created by newtonis on 4/30/2019.
//

#ifndef EJ8_REVERB_H
#define EJ8_REVERB_H


#include "AudioEffect.h"
#include <complex>

using namespace std;


#define MAX_BUFFER_SIZE     (10000)

enum{
    ECO,
    PLANO,
    PASABAJO
};


class Reverb : public AudioEffect {
    public:
        Reverb(unsigned int sampleRate, unsigned int framesPerBuffer, unsigned int windowWidth, int mode);
        void processInput(CircularBuffer& in, CircularBuffer& out);
        void processWindow(CircularBuffer& in, CircularBuffer& out);
        void eco(CircularBuffer& in, CircularBuffer& out);
        void reverbPlano(CircularBuffer& in, CircularBuffer& out);

    protected:
        float x[MAX_BUFFER_SIZE], last_x[MAX_BUFFER_SIZE];
        float y[MAX_BUFFER_SIZE], last_y[MAX_BUFFER_SIZE];
        float z[MAX_BUFFER_SIZE];
        int mode;
        bool start;

        unsigned int windowWidth;

        std::vector<float> window;
        CircularBuffer windowedData;
        std::vector<complex<float>> transform;

};


#endif //EJ8_REVERB_H

//
// Created by newtonis on 4/30/2019.
//

#ifndef EJ8_REVERB_H
#define EJ8_REVERB_H


#include "AudioEffect.h"
#include <complex>
#include <map>

using namespace std;


#define MAX_BUFFER_SIZE     (10000)

enum{
    ECO,
    PLANO,
    PASABAJO,
    COMPLETO,
    COVOLUCION
};


class Reverb : public AudioEffect {
    public:
        Reverb(
                unsigned int sampleRate,
                unsigned int framesPerBuffer,
                unsigned int windowWidth,
                int mode,
                map<string,int> &config
                );


        void processInput(CircularBuffer& in, CircularBuffer& out);
        void eco(CircularBuffer& in, CircularBuffer& out);
        void reverbPlano(CircularBuffer& in, CircularBuffer& out);
        void reverbPlanoPB(CircularBuffer& in, CircularBuffer& out);
        void reverbConvolution(CircularBuffer& in, CircularBuffer& out);
        int impulseLength;

    protected:
        float x[MAX_BUFFER_SIZE], last_x[MAX_BUFFER_SIZE];
        float y[MAX_BUFFER_SIZE], last_y[MAX_BUFFER_SIZE];
        float z[MAX_BUFFER_SIZE], last_z[MAX_BUFFER_SIZE];
        int mode;
        map<string,int> config;

        vector <float> outputA, outputB;
        bool start;

        unsigned int windowWidth;

        std::vector<float> window;
        CircularBuffer windowedData;
        std::vector<complex<float>> transform;

};


#endif //EJ8_REVERB_H

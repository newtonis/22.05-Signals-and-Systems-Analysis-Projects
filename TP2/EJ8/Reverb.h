//
// Created by newtonis on 4/30/2019.
//

#ifndef EJ8_REVERB_H
#define EJ8_REVERB_H


#include "AudioEffect.h"
#include <complex>
#include <map>

using namespace std;


#define MAX_BUFFER_SIZE     (21000)
#define DP_MAX (3000)
#define MAX_REB 20

enum{
    ECO,
    PLANO,
    PASABAJO,
    COMPLETO,
    CONVOLUCION
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
        void reverbSchroeder(CircularBuffer& in, CircularBuffer& out);
        int impulseLength;

    protected:
        float x[MAX_BUFFER_SIZE], last_x[MAX_BUFFER_SIZE];
        float y[MAX_BUFFER_SIZE], last_y[MAX_BUFFER_SIZE];
        float z[MAX_BUFFER_SIZE], last_z[MAX_BUFFER_SIZE];

        float aux[DP_MAX][MAX_REB];
        float comb_aux[DP_MAX][MAX_REB];
        float comb_a[DP_MAX];

        int mode;
        map<string,int> config;

        vector <int> D;
        vector <int> combD;
        vector <float> combA;

        int comb_count;

        float a;

        vector <float> outputA, outputB; // para la respuesta al impulso
        bool start;

        unsigned int windowWidth;

        std::vector<float> window;
        CircularBuffer windowedData;
        std::vector<complex<float>> transform;

};


#endif //EJ8_REVERB_H

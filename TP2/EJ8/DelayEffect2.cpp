//
// Created by joa-m on 1/5/2019.
//

#include "DelayEffect2.h"


#include <cmath>

#define pi 3.1415926535897932384626433


DelayEffect2::DelayEffect2(unsigned int sampleRate, unsigned int framesPerBuffer,
                                   float ff, float fb, float bl, float f_mod, float mod_depth) :
        AudioEffect(sampleRate, framesPerBuffer),
        ff(ff), fb(fb), bl(bl),
        f_mod(f_mod),
        mod_depth(mod_depth),
        last_samples(std::ceil(sampleRate*mod_depth))
{

    t = 0;
    this->w = 2*pi*f_mod;
}

void DelayEffect2::processInput(CircularBuffer &in, CircularBuffer &out) {
    while (!in.empty()) {
        float x_n = in.next();
        float x_n_k = 0;
        float x_n_k_2 = 0;


        unsigned int delay = getKA();
        if (delay < last_samples.currSize()) {
            x_n_k = last_samples.read(delay);
        }   // esto me asigna el x(n-k) sin salirse del buffer

        unsigned int delay_2 = getKB();
        if (delay_2 < last_samples.currSize()) {
            x_n_k_2 = last_samples.read(delay_2);
        }   // esto me asigna el x(n-k) sin salirse del buffer


        // en esta prueba xa e ya tienne mismo delay
        float xa = x_n_k;
        float ya = x_n_k_2;

        float xb = xa*(1+sin(w*t));
        float yb = ya*(1-sin(w*t));

        float yL =yb*0.7 + xb;
        float yR =xb*0.7 + yb;

        // siempre viene izq primero
        if(&out == &outLeft ){
            outLeft.push_back(yL);
            outRight.push_back(yR);
        }else{
            float last_left = outLeft.read(outLeft.currSize()-1);
            float last_right = outLeft.read(outRight.currSize()-1);
            outLeft.write(outLeft.currSize()-1,yL+last_left);
            outRight.write(outRight.currSize()-1,yR+last_right);
        }

        if (last_samples.isFull()) {
            last_samples.pop_back(1);
        }
        last_samples.push_front(x_n);
    }
}


unsigned int DelayEffect2::getKA() {
    auto k = (unsigned int) (std::floor(mod_depth*sampleRate/2 * (std::sin(2*pi*f_mod*t) )));
    //t = std::fmod(t+float(1)/sampleRate, 2*pi*f_mod); // resto de dividir (t+T)/(2pi*f_mod)
    return k;
}

unsigned int DelayEffect2::getKB() {
    auto k = (unsigned int) (std::floor(mod_depth*sampleRate/2 * (-std::sin(2*pi*f_mod*t) )));
    t = std::fmod(t+float(1)/sampleRate, 2*pi*f_mod); // resto de dividir (t+T)/(2pi*f_mod)
    return k;
}


void DelayEffect2::processStereoInput(const float *stereoInput) {
    splitInput(stereoInput);

    float tsinc = t;
    processInput(inLeft, outLeft);

    t = tsinc;
    processInput(inRight, outRight);

    inRight.clear();
}

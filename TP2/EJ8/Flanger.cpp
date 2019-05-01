//
// Created by Rocío Parra on 30-Apr-19.
//

#include "Flanger.h"
#include <cmath>

#define pi 3.1415926535897932384626433

#define FF 0.7
#define FB 0.0
#define BL 1.0


Flanger::Flanger(unsigned int sampleRate, unsigned int framesPerBuffer, float f_mod, float mod_depth) :
 AudioEffect(sampleRate, framesPerBuffer),
 f_mod(f_mod),
 mod_depth(mod_depth),
 last_samples(std::ceil(sampleRate*mod_depth))
 {
    t = 0;
}

void Flanger::processInput(CircularBuffer &in, CircularBuffer &out) {
    //unsigned int max_delay = std::ceil(sampleRate*mod_depth);

    while (!in.empty()) {
        float xh = in.next();
        float delayed_xh = 0;

        unsigned int delay = delayLine();
        if (delay < last_samples.currSize()) {
            delayed_xh = last_samples.read(delay);
        }

        xh += FB*delayed_xh;

        out.push_back(BL * xh + FF * delayed_xh);

        if (last_samples.isFull()) {
            last_samples.pop_back(1);
        }
        last_samples.push_front(xh);
    }
}



unsigned int Flanger::delayLine() {
    auto k = (unsigned int) (std::floor(mod_depth*sampleRate/2 * (std::sin(2*pi*f_mod*t) + 1)));
    t = std::fmod(t+float(1)/sampleRate, 2*pi*f_mod);

    return k;
}

void Flanger::processStereoInput(const float *stereoInput) {
    splitInput(stereoInput);

    float tsinc = t;
    processInput(inLeft, outLeft);

    t = tsinc;
    processInput(inRight, outRight);
}

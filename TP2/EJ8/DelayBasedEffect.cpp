//
// Created by Rocío Parra on 01-May-19.
//

#include "DelayBasedEffect.h"


#include <cmath>

#define pi 3.1415926535897932384626433



DelayBasedEffect::DelayBasedEffect(unsigned int sampleRate, unsigned int framesPerBuffer,
        float ff, float fb, float bl, float f_mod, float mod_depth) :
        AudioEffect(sampleRate, framesPerBuffer),
        ff(ff), fb(fb), bl(bl),
        f_mod(f_mod),
        mod_depth(mod_depth),
        last_samples(std::ceil(sampleRate*mod_depth))
{
    t = 0;
}

void DelayBasedEffect::processInput(CircularBuffer &in, CircularBuffer &out) {
    while (!in.empty()) {
        float xh = in.next();
        float delayed_xh = 0;

        unsigned int delay = delayLine();
        if (delay < last_samples.currSize()) {
            delayed_xh = last_samples.read(delay);
        }

        xh += fb*delayed_xh;

        out.push_back(bl * xh + ff * delayed_xh);

        if (last_samples.isFull()) {
            last_samples.pop_back(1);
        }
        last_samples.push_front(xh);
    }
}



unsigned int DelayBasedEffect::delayLine() {
    auto k = (unsigned int) (std::floor(mod_depth*sampleRate/2 * (std::sin(2*pi*f_mod*t) + 1)));
    t = std::fmod(t+float(1)/sampleRate, 2*pi*f_mod);

    return k;
}

void DelayBasedEffect::processStereoInput(const float *stereoInput) {
    splitInput(stereoInput);

    float tsinc = t;
    processInput(inLeft, outLeft);

    t = tsinc;
    processInput(inRight, outRight);
}

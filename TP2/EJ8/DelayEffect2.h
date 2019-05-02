//
// Created by joa-m on 1/5/2019.
//

#ifndef EJ8_DELAYEFFECT2_H
#define EJ8_DELAYEFFECT2_H

#include "AudioEffect.h"

class DelayEffect2 : public AudioEffect{
public:
    DelayEffect2(unsigned int sampleRate, unsigned int framesPerBuffer, float ff, float fb, float bl,
                     float f_mod, float mod_depth);

    void processInput(CircularBuffer& in, CircularBuffer& out) override;

    void processStereoInput(const float * stereoInput) override;


private:
    unsigned int getKA();
    unsigned int getKB();


    const float f_mod;
    const float mod_depth;
    const float ff, fb, bl;

    CircularBuffer last_samples;

    float t;
    float w;
};



#endif //EJ8_DELAYEFFECT2_H

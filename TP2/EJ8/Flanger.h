//
// Created by Rocío Parra on 30-Apr-19.
//

#ifndef EJ8_FLANGER_H
#define EJ8_FLANGER_H


#include "AudioEffect.h"
#include "CircularBuffer.h"

class Flanger : public AudioEffect{
public:
    Flanger(unsigned int sampleRate, unsigned int framesPerBuffer, float f_mod, float mod_depth);

    void processInput(CircularBuffer& in, CircularBuffer& out) override;
    void processStereoInput(const float * stereoInput) override;


private:
    unsigned int delayLine();

    const float f_mod;
    const float mod_depth;
    CircularBuffer last_samples;

    float t;
};


#endif //EJ8_FLANGER_H

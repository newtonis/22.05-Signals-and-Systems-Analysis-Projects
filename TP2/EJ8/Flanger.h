//
// Created by Rocío Parra on 30-Apr-19.
//

#ifndef EJ8_FLANGER_H
#define EJ8_FLANGER_H


#include "DelayBasedEffect.h"
#include "CircularBuffer.h"

class Flanger : public DelayBasedEffect{
public:
    Flanger(unsigned int sampleRate, unsigned int framesPerBuffer, float f_mod, float mod_depth, float g);

    void processInput(CircularBuffer& in, CircularBuffer& out) override;
    void processStereoInput(const float * stereoInput) override;


private:
};


#endif //EJ8_FLANGER_H

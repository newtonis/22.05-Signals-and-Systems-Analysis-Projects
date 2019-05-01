//
// Created by Rocío Parra on 01-May-19.
//

#ifndef EJ8_VIBRATO_H
#define EJ8_VIBRATO_H


#include "DelayBasedEffect.h"

class Vibrato : public DelayBasedEffect {
public:
    Vibrato(unsigned int sampleRate, unsigned int framesPerBuffer, float f_mod, float mod_depth);

private:
};


#endif //EJ8_VIBRATO_H

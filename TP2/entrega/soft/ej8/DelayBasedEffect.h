//
// Created by Rocío Parra on 01-May-19.
//

#ifndef EJ8_DELAYBASEDEFFECT_H
#define EJ8_DELAYBASEDEFFECT_H

#include "AudioEffect.h"

class DelayBasedEffect : public AudioEffect{
public:
    DelayBasedEffect(unsigned int sampleRate, unsigned int framesPerBuffer, float ff, float fb, float bl,
            float f_mod, float mod_depth);

    void processInput(CircularBuffer& in, CircularBuffer& out) override;
    void processStereoInput(const float * stereoInput) override;


private:
    unsigned int delayLine();

    const float f_mod;
    const float mod_depth;
    const float ff, fb, bl;

    CircularBuffer last_samples;

    float t;
};


#endif //EJ8_DELAYBASEDEFFECT_H

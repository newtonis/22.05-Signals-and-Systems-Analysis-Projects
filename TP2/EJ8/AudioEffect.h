//
// Created by Rocío Parra on 26-Apr-19.
//

#ifndef EJ8_AUDIOEFFECT_H
#define EJ8_AUDIOEFFECT_H

#include <string>
#include <queue>
#include <vector>
#include "CircularBuffer.h"

class AudioEffect {
public:
    //static factory(std::string name, void * params, unsigned int const sampleRate, unsigned int const framesPerBuffer);
    AudioEffect(unsigned int sampleRate, unsigned int framesPerBuffer, unsigned int minOutSize = 0);

    virtual void processStereoInput(const float * stereoInput);
    virtual void processInput(CircularBuffer& in, CircularBuffer& out) = 0;
    void setNextOutput(float * stereoOutput);


protected:
    void splitInput(const float * stereoInput);

    unsigned int const sampleRate;
    unsigned int const framesPerBuffer;
    unsigned int const minOutSize;

    CircularBuffer inLeft;
    CircularBuffer inRight;
    CircularBuffer outLeft;
    CircularBuffer outRight;
};


#endif //EJ8_AUDIOEFFECT_H

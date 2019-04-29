//
// Created by Rocío Parra on 26-Apr-19.
//

#include "AudioEffect.h"
#include <iostream>

AudioEffect::AudioEffect(unsigned int sampleRate, unsigned int framesPerBuffer, unsigned int minOutSize)
: sampleRate(sampleRate), framesPerBuffer(framesPerBuffer), inLeft(framesPerBuffer),
inRight(framesPerBuffer), outLeft(framesPerBuffer), outRight(framesPerBuffer),
minOutSize(minOutSize)
{
    ;
}


void AudioEffect::setNextOutput(float * stereoOutput)
{
    if (stereoOutput) {
        unsigned int i = 0;
        while (i < framesPerBuffer && outLeft.currSize() > minOutSize) {
            stereoOutput[2 * i] = outLeft.next();
            stereoOutput[2 * i + 1] = outRight.next();

            i++;
        }

        while (i < framesPerBuffer ) {
            stereoOutput[2 * i] = 0; // esto solo deberia suceder la primera vuelta y despues arreglarse
            stereoOutput[2 * i + 1] = 0;

            i++;
        }
    }
}

void AudioEffect::splitInput(const float * stereoInput)
{
    if (stereoInput) {
        for (unsigned int i = 0; i < framesPerBuffer; i++) {
            //inLeft.emplace(0);
            inLeft.emplace(stereoInput[2*i]);
            inRight.emplace(stereoInput[2*i+1]);
            //inRight.emplace(0);
        }
    }
}

void AudioEffect::processStereoInput(const float *stereoInput) {
    splitInput(stereoInput);
    processInput(inLeft, outLeft);
    processInput(inRight, outRight);
}


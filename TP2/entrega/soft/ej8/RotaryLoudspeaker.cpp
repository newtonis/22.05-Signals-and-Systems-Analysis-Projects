//
// Created by joa-m on 1/5/2019.
//

#include "RotaryLoudspeaker.h"

RotaryLoudspeaker::RotaryLoudspeaker(unsigned int sampleRate, unsigned int framesPerBuffer, float fmod, float mod_depth) :
        DelayEffect2(sampleRate, framesPerBuffer, 1, 0, 0, fmod, mod_depth)
{

}

/*
RotaryLoudspeaker::RotaryLoudspeaker(unsigned int sampleRate, unsigned int framesPerBuffer, float w):
            AudioEffect(sampleRate,framesPerBuffer,w), windowedData(w), transform(w){
    this->w = w;
}

void RotaryLoudspeaker::processInput(CircularBuffer& in, CircularBuffer& out){
    unsigned int t = 0;
    while (in.currSize() > 0){
        float x_n = in.next();
        float delay_form1 = sin(w*t);
        float delay_form2= sin(w*t);
    }

}
*/



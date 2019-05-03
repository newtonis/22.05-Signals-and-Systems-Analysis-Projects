//
// Created by joa-m on 1/5/2019.
//

#ifndef EJ8_ROTARYLOUDSPEAKER_H
#define EJ8_ROTARYLOUDSPEAKER_H

#include "DelayEffect2.h"
#include <complex>
#define pi 3.1415926535897932384626433


class RotaryLoudspeaker : public DelayEffect2 {
public:
    RotaryLoudspeaker(unsigned int sampleRate, unsigned int framesPerBuffer, float f_mod,float mod_depth);

private:
};


/*
class RotaryLoudspeaker: public AudioEffect {
public:
    RotaryLoudspeaker(unsigned int sampleRate, unsigned int framesPerBuffer, float w);
    void processInput(CircularBuffer& in, CircularBuffer& out);

protected:
    float w;
    unsigned int windowWidth;
    std::vector<std::complex<float>> transform;
    CircularBuffer windowedData;

    //void processWindow(CircularBuffer& in, CircularBuffer& out);
*/
/*  std::vector<float> window;
    CircularBuffer windowedData;
    std::vector<std::complex<float>> transform;*//*

};


*/



#endif //EJ8_ROTARYLOUDSPEAKER_H

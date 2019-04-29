#ifndef EJ8_ROBOTIZATION_H
#define EJ8_ROBOTIZATION_H

#include "AudioEffect.h"
#include <complex>

class Robotization : public AudioEffect {
public:
    Robotization(unsigned int sampleRate, unsigned int framesPerBuffer, unsigned int windowWidth);
    void processInput(CircularBuffer& in, CircularBuffer& out);

protected:
    void processWindow(CircularBuffer& in, CircularBuffer& out);
    unsigned int windowWidth;

    std::vector<float> window;
    CircularBuffer windowedData;
    std::vector<std::complex<float>> transform;
};


#endif //EJ8_ROBOTIZATION_H

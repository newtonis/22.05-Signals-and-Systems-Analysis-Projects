//
// Created by Rocío Parra on 27-Apr-19.
//

#ifndef EJ8_NADA_H
#define EJ8_NADA_H

#include "AudioEffect.h"
#include "my_fft.h"

class Nada : public AudioEffect {
public:
    Nada(unsigned int sampleRate, unsigned int framesPerBuffer) : AudioEffect(sampleRate, framesPerBuffer, 0)
    {
        transform.resize(framesPerBuffer);
        ffjk = true;
    }
    void processInput(CircularBuffer& in, CircularBuffer& out) {
        ffjk = !ffjk;
        if (ffjk) {
            unsigned int i = 0;
            while (in.currSize()) {
                transform[i++] = complex<float>(in.next(), 0);
            }

            fft(transform, transform);
            ifft(transform, transform);

            for (i = 0; i < framesPerBuffer; i++) {
                out.emplace(transform[i].real());
            }
        }
        else {
            while (in.currSize()) {
                out.emplace(in.next());
            }
        }
    }

private:
    vector<complex<float>> transform;
    bool ffjk;
};


#endif //EJ8_NADA_H

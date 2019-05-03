//
// Created by Rocío Parra on 01-May-19.
//

#include "Vibrato.h"
#include <cmath>

#define pi 3.1415926535897932384626433

#define FF 1
#define FB 0
#define BL 0


Vibrato::Vibrato(unsigned int sampleRate, unsigned int framesPerBuffer, float f_mod, float mod_depth) :
        DelayBasedEffect(sampleRate, framesPerBuffer, 1, 0, 0, f_mod, mod_depth)
{
    ;
}


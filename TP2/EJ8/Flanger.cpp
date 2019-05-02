//
// Created by Rocío Parra on 30-Apr-19.
//

#include "Flanger.h"
#include <cmath>

#define pi 3.1415926535897932384626433

//#define FF 0.8
//#define FB 0
//#define BL 1
//

Flanger::Flanger(unsigned int sampleRate, unsigned int framesPerBuffer, float f_mod, float mod_depth) :
 DelayBasedEffect(sampleRate, framesPerBuffer, 0.7, 0.7, 0.7, f_mod, mod_depth)
 {

}

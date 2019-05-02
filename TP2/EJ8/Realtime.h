//
// Created by newtonis on 5/2/2019.
//

#ifndef EJ8_REALTIME_H
#define EJ8_REALTIME_H

#include <stdio.h>
#include <math.h>
#include "portaudio.h"
#include "Robotization.h"
#include "Reverb.h"


#define SAMPLE_RATE         (44100)
#define PA_SAMPLE_TYPE      paFloat32
#define FRAMES_PER_BUFFER   (4096)
#define FUZZ(x) CubicAmplifier(CubicAmplifier(CubicAmplifier(CubicAmplifier(x))))


int Realtime(AudioEffect *bot, string &msg) ;
PaError setupPortaudio(PaStream * &stream, void *bot);
float CubicAmplifier( float input );
static int fuzzCallback( const void *inputBuffer, void *outputBuffer,
                         unsigned long framesPerBuffer,
                         const PaStreamCallbackTimeInfo* timeInfo,
                         PaStreamCallbackFlags statusFlags,
                         void *userData );


static int gNumNoInputs = 0;
/* This routine will be called by the PortAudio engine when audio is needed.
** It may be called at interrupt level on some machines so don't do anything
** that could mess up the system like calling malloc() or free().
*/
static int fuzzCallback( const void *inputBuffer, void *outputBuffer,
                         unsigned long framesPerBuffer,
                         const PaStreamCallbackTimeInfo* timeInfo,
                         PaStreamCallbackFlags statusFlags,
                         void *userData );


#endif //EJ8_REALTIME_H

//
// Created by newtonis on 5/2/2019.
//

#include "realtime.h"
#include "AudioEffect.h"
#include <iostream>
#include <climits>
#include <string>

using namespace std;

//
/*
** Note that many of the older ISA sound cards on PCs do NOT support
** full duplex audio (simultaneous record and playback).
** And some only support full duplex at lower sample rates.
*/






/* Non-linear amplifier with soft distortion curve. */
float CubicAmplifier( float input )
{
    float output, temp;
    if( input < 0.0 )
    {
        temp = input + 1.0f;
        output = (temp * temp * temp) - 1.0f;
    }
    else
    {
        temp = input - 1.0f;
        output = (temp * temp * temp) + 1.0f;
    }

    return output;
}


/* This routine will be called by the PortAudio engine when audio is needed.
** It may be called at interrupt level on some machines so don't do anything
** that could mess up the system like calling malloc() or free().
*/
static int fuzzCallback( const void *inputBuffer, void *outputBuffer,
                         unsigned long framesPerBuffer,
                         const PaStreamCallbackTimeInfo* timeInfo,
                         PaStreamCallbackFlags statusFlags,
                         void *userData )
{
    auto *out = (float*)outputBuffer;
    const auto *in = (const float*)inputBuffer;
    unsigned int i;
    (void) timeInfo; /* Prevent unused variable warnings. */
    (void) statusFlags;
    auto * bot = (AudioEffect *)userData;

    if( inputBuffer == nullptr )
    {
        for( i=0; i<framesPerBuffer; i++ )
        {
            *out++ = 0;  /* left - silent */
            *out++ = 0;  /* right - silent */
        }
        gNumNoInputs += 1;
    }
    else
    {
        bot->processStereoInput(in);
        bot->setNextOutput(out);
    }

    return paContinue;
}

/*******************************************************************/
PaError setupPortaudio(PaStream * &stream);
PaError terminatePortaudio(PaStream * &stream);
//
int Realtime(AudioEffect *bot, string &msg) {
    PaStream * stream = nullptr;
    PaError err = setupPortaudio(stream, (void*)bot);

    if (err == paNoError) {


        printf(">>> \n");

        cin >> msg;

        err = terminatePortaudio(stream);
        if (err == paNoError) {
            printf("Finished. gNumNoInputs = %d\n", gNumNoInputs);
            return EXIT_SUCCESS;
        }
    }

    fprintf(stderr, "An error occured while using the portaudio stream\n");
    fprintf(stderr, "Error number: %d\n", err);
    fprintf(stderr, "Error message: %s\n", Pa_GetErrorText(err));
    return EXIT_FAILURE;
}

PaError setupPortaudio(PaStream * &stream, void *bot)
{
    PaStreamParameters inputParameters, outputParameters;
    PaError err;

    err = Pa_Initialize();
    if( err == paNoError ) {

        inputParameters.device = Pa_GetDefaultInputDevice(); /* default input device */
        if (inputParameters.device == paNoDevice) {
            err = paNoDevice;
        }
        else {
            inputParameters.channelCount = 2;       /* stereo input */
            inputParameters.sampleFormat = PA_SAMPLE_TYPE;
            inputParameters.suggestedLatency = Pa_GetDeviceInfo(inputParameters.device)->defaultLowInputLatency;
            inputParameters.hostApiSpecificStreamInfo = nullptr;

            outputParameters.device = Pa_GetDefaultOutputDevice(); /* default output device */
            if (outputParameters.device == paNoDevice) {
                err = paNoDevice;
            }
            else {
                //auto * bot = new Reverb(SAMPLE_RATE, FRAMES_PER_BUFFER, 4096);
                //auto * bot = new Nada(SAMPLE_RATE, FRAMES_PER_BUFFER);

                outputParameters.channelCount = 2;       /* stereo output */
                outputParameters.sampleFormat = PA_SAMPLE_TYPE;
                outputParameters.suggestedLatency = Pa_GetDeviceInfo(outputParameters.device)->defaultLowOutputLatency;
                outputParameters.hostApiSpecificStreamInfo = nullptr;

                err = Pa_OpenStream(
                        &stream,
                        &inputParameters,
                        &outputParameters,
                        SAMPLE_RATE,
                        FRAMES_PER_BUFFER,
                        0, /* paClipOff, */  /* we won't output out of range samples so don't bother clipping them */
                        fuzzCallback,
                        bot);
                if (err == paNoError) {
                    err = Pa_StartStream(stream);
                }
            }
        }
    }
    return err;
}


PaError terminatePortaudio(PaStream * &stream) {
    PaError err = Pa_CloseStream(stream);
    if (err == paNoError) {
        Pa_Terminate();
    }
    return err;
}
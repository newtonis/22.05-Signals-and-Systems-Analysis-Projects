//#include "Robotization.h"
//#include "Nada.h"
//
///* licencia de portaudio: el codigo de como configurar el microfono,
// * los parlantes, el callback y eso es sacado de "pa_fuzz.c"
//*/
///*
// * $Id$
// *
// * This program uses the PortAudio Portable Audio Library.
// * For more information see: http://www.portaudio.com
// * Copyright (c) 1999-2000 Ross Bencina and Phil Burk
// *
// * Permission is hereby granted, free of charge, to any person obtaining
// * a copy of this software and associated documentation files
// * (the "Software"), to deal in the Software without restriction,
// * including without limitation the rights to use, copy, modify, merge,
// * publish, distribute, sublicense, and/or sell copies of the Software,
// * and to permit persons to whom the Software is furnished to do so,
// * subject to the following conditions:
// *
// * The above copyright notice and this permission notice shall be
// * included in all copies or substantial portions of the Software.
// *
// * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
// * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
// * ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
// * CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
// * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// */
//
///*
// * The text above constitutes the entire PortAudio license; however,
// * the PortAudio community also makes the following non-binding requests:
// *
// * Any person wishing to distribute modifications to the Software is
// * requested to send the modifications to the original developer so that
// * they can be incorporated into the canonical version. It is also
// * requested that these non-binding requests be included along with the
// * license above.
// */
//
#include <stdio.h>
#include <math.h>
#include "portaudio.h"
#include "Robotization.h"
#include "Reverb.h"
//
///*
//** Note that many of the older ISA sound cards on PCs do NOT support
//** full duplex audio (simultaneous record and playback).
//** And some only support full duplex at lower sample rates.
//*/
//#define SAMPLE_RATE         (44100)
//#define PA_SAMPLE_TYPE      paFloat32
//#define FRAMES_PER_BUFFER   (4096)
//
//
//float CubicAmplifier( float input );
//static int fuzzCallback( const void *inputBuffer, void *outputBuffer,
//                         unsigned long framesPerBuffer,
//                         const PaStreamCallbackTimeInfo* timeInfo,
//                         PaStreamCallbackFlags statusFlags,
//                         void *userData );
//
///* Non-linear amplifier with soft distortion curve. */
//float CubicAmplifier( float input )
//{
//    float output, temp;
//    if( input < 0.0 )
//    {
//        temp = input + 1.0f;
//        output = (temp * temp * temp) - 1.0f;
//    }
//    else
//    {
//        temp = input - 1.0f;
//        output = (temp * temp * temp) + 1.0f;
//    }
//
//    return output;
//}
//#define FUZZ(x) CubicAmplifier(CubicAmplifier(CubicAmplifier(CubicAmplifier(x))))
//
//static int gNumNoInputs = 0;
///* This routine will be called by the PortAudio engine when audio is needed.
//** It may be called at interrupt level on some machines so don't do anything
//** that could mess up the system like calling malloc() or free().
//*/
//static int fuzzCallback( const void *inputBuffer, void *outputBuffer,
//                         unsigned long framesPerBuffer,
//                         const PaStreamCallbackTimeInfo* timeInfo,
//                         PaStreamCallbackFlags statusFlags,
//                         void *userData )
//{
//    auto *out = (float*)outputBuffer;
//    const auto *in = (const float*)inputBuffer;
//    unsigned int i;
//    (void) timeInfo; /* Prevent unused variable warnings. */
//    (void) statusFlags;
//    auto * bot = (Robotization *)userData;
//
//    if( inputBuffer == nullptr )
//    {
//        for( i=0; i<framesPerBuffer; i++ )
//        {
//            *out++ = 0;  /* left - silent */
//            *out++ = 0;  /* right - silent */
//        }
//        gNumNoInputs += 1;
//    }
//    else
//    {
//        bot->processStereoInput(in);
//        bot->setNextOutput(out);
//    }
//
//    return paContinue;
//}
//
///*******************************************************************/
//PaError setupPortaudio(PaStream * &stream);
//PaError terminatePortaudio(PaStream * &stream);
////
//int main() {
//    PaStream * stream = nullptr;
//    PaError err = setupPortaudio(stream);
//
//    if (err == paNoError) {
//
//
//        printf("Hit ENTER to stop program.\n");
//        getchar();
//        err = terminatePortaudio(stream);
//        if (err == paNoError) {
//            printf("Finished. gNumNoInputs = %d\n", gNumNoInputs);
//            return EXIT_SUCCESS;
//        }
//    }
//
//    fprintf(stderr, "An error occured while using the portaudio stream\n");
//    fprintf(stderr, "Error number: %d\n", err);
//    fprintf(stderr, "Error message: %s\n", Pa_GetErrorText(err));
//    return EXIT_FAILURE;
//}
//
//PaError setupPortaudio(PaStream * &stream)
//{
//    PaStreamParameters inputParameters, outputParameters;
//    PaError err;
//
//    err = Pa_Initialize();
//    if( err == paNoError ) {
//
//        inputParameters.device = Pa_GetDefaultInputDevice(); /* default input device */
//        if (inputParameters.device == paNoDevice) {
//            err = paNoDevice;
//        }
//        else {
//            inputParameters.channelCount = 2;       /* stereo input */
//            inputParameters.sampleFormat = PA_SAMPLE_TYPE;
//            inputParameters.suggestedLatency = Pa_GetDeviceInfo(inputParameters.device)->defaultLowInputLatency;
//            inputParameters.hostApiSpecificStreamInfo = nullptr;
//
//            outputParameters.device = Pa_GetDefaultOutputDevice(); /* default output device */
//            if (outputParameters.device == paNoDevice) {
//                err = paNoDevice;
//            }
//            else {
//                auto * bot = new Reverb(SAMPLE_RATE, FRAMES_PER_BUFFER, 4096);
//                //auto * bot = new Nada(SAMPLE_RATE, FRAMES_PER_BUFFER);
//
//                outputParameters.channelCount = 2;       /* stereo output */
//                outputParameters.sampleFormat = PA_SAMPLE_TYPE;
//                outputParameters.suggestedLatency = Pa_GetDeviceInfo(outputParameters.device)->defaultLowOutputLatency;
//                outputParameters.hostApiSpecificStreamInfo = nullptr;
//
//                err = Pa_OpenStream(
//                        &stream,
//                        &inputParameters,
//                        &outputParameters,
//                        SAMPLE_RATE,
//                        FRAMES_PER_BUFFER,
//                        0, /* paClipOff, */  /* we won't output out of range samples so don't bother clipping them */
//                        fuzzCallback,
//                        bot);
//                if (err == paNoError) {
//                    err = Pa_StartStream(stream);
//                }
//            }
//        }
//    }
//    return err;
//}
//
//
//PaError terminatePortaudio(PaStream * &stream) {
//    PaError err = Pa_CloseStream(stream);
//    if (err == paNoError) {
//        Pa_Terminate();
//    }
//    return err;
//}

#include <map>
#include "AudioFile.h"
#include "Robotization.h"
#include "windows.h"
#include "Reverb.h"
#include "Flanger.h"
#include "Vibrato.h"
#include "InputParser.h"
#include "WavProcess.h"


using namespace std;


int main() {
    parseInput();

//    std::vector<float> holis;
//    hanning(8, holis);
//    hanning(512, holis);
//
//
//    std::string name = "president-is-moron";
//    AudioFile<float> audioFile;
//    AudioFile<float> out;
//    AudioFile<float>::AudioBuffer newBuffer;
//    unsigned int windowWidth = 4096;
//
//    audioFile.load("input/" + name + ".wav");
//    int sampleRate = audioFile.getSampleRate();
//    int numSamples = audioFile.getNumSamplesPerChannel();
//    int realSamples = audioFile.getNumSamplesPerChannel();
//
//    map<string, int> config;
//
//    Reverb *bot = new Reverb(sampleRate, numSamples, windowWidth, ECO);
//    bot->myG = 0.999;
//    bot->myM = 5000;
//
//    auto *buffer = new float[numSamples * 2];
//    for (int i = 0; i < numSamples; i++) {
//        if (i < realSamples) {
//            buffer[2 * i] = audioFile.samples[0][i];
//            buffer[2 * i + 1] = audioFile.samples[1][i];
//        } else {
//            buffer[2 * i] = 0;
//            buffer[2 * i + 1] = 0;
//        }
//    }
//
//
////    freopen("output/x.txt", "w+",stdout);
////    for (int i = 0;i < numSamples;i++){
////        cout << buffer[2*i] << '\n';
////    }
//
//
//    bot->processStereoInput(buffer);
//    bot->setNextOutput(buffer);
//
//    newBuffer.resize(2);
//    newBuffer[0].resize(numSamples);
//    newBuffer[1].resize(numSamples);
//    for (int i = 0; i < numSamples; i++) {
//        newBuffer[0][i] = buffer[2*i];
//        newBuffer[1][i] = buffer[2*i+1];
//    }
//
//
//
////    freopen("output/y.txt","w+",stdout);
////    for (int i = 0;i < numSamples;i++){
////        cout << buffer[2*i] << '\n';
////    }
//
//
//    out.setAudioBuffer(newBuffer);
//    out.save ("output2/"+name + "_" + std::to_string(windowWidth) +"_out.wav");
//    delete [] buffer;


    /*auto *bot = new Reverb(44100, 4096, 4096, ECO);
    bot->myG = 0.993;
    bot->myM = 5000;

    string a = "input/president-is-moron.wav";
    string b =   "output2/test.wav";
    wavProcess(bot, a, b);*/

}
#include <stdio.h>
#include <math.h>
#include "portaudio.h"
#include "Robotization.h"
#include "Reverb.h"
#include "Flanger.h"

#define SAMPLE_RATE         (44100)
#define PA_SAMPLE_TYPE      paFloat32
#define FRAMES_PER_BUFFER   (4096)


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
                         void *userData )
{
    auto *out = (float*)outputBuffer;
    const auto *in = (const float*)inputBuffer;
    unsigned int i;
    (void) timeInfo; /* Prevent unused variable warnings. */
    (void) statusFlags;
    auto * bot = (Robotization *)userData;

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
int main() {
    PaStream * stream = nullptr;
    PaError err = setupPortaudio(stream);

    if (err == paNoError) {


        printf("Hit ENTER to stop program.\n");
        getchar();
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

PaError setupPortaudio(PaStream * &stream)
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
                auto * bot = new Flanger(SAMPLE_RATE, FRAMES_PER_BUFFER, 1, 0.01);

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





//#include "AudioFile.h"
//#include "Robotization.h"
//#include "windows.h"
//#include "Reverb.h"
//#include "Flanger.h"
//
//
//int main()
//{
//    std::string name = "president-is-moron";
//    AudioFile<float> audioFile;
//    AudioFile<float> out;
//    AudioFile<float>::AudioBuffer newBuffer;
//    //unsigned int windowWidth = 256;
//    float f_mod = 1, mod_depth = 0.01;
//
//    audioFile.load (name + ".wav");
//    int numSamples = audioFile.getNumSamplesPerChannel();
//    int sampleRate = audioFile.getSampleRate();
//
//    //Reverb bot(sampleRate, numSamples, windowWidth, PLANO);
//    Flanger bot(sampleRate, numSamples, f_mod, mod_depth);
//
//    auto * buffer = new float [numSamples*2];
//    for (int i = 0; i < numSamples; i++) {
//        buffer[2*i] = audioFile.samples[0][i];
//        buffer[2*i + 1] = audioFile.samples[1][i];
//    }
//
//    bot.processStereoInput(buffer);
//    bot.setNextOutput(buffer);
//
//    newBuffer.resize(2);
//    newBuffer[0].resize(numSamples);
//    newBuffer[1].resize(numSamples);
//    for (int i = 0; i < numSamples; i++) {
//        newBuffer[0][i] = buffer[2*i];
//        newBuffer[1][i] = buffer[2*i+1];
//    }
//
//    out.setAudioBuffer(newBuffer);
//    out.save (name + "_" + std::to_string(f_mod) + "Hz_" + std::to_string(mod_depth*1000) +"ms_out.wav");
//    delete [] buffer;
//}
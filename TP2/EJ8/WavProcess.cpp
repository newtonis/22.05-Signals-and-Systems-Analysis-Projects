//
// Created by newtonis on 5/2/2019.
//

#include "WavProcess.h"
#include <map>
#include "AudioFile.h"
#include "Robotization.h"
#include "windows.h"
#include "Reverb.h"
#include "Flanger.h"
#include "Vibrato.h"
#include "InputParser.h"


using namespace std;

void wavProcess(AudioEffect *bot, string &input, string &output){
    AudioFile<float> audioFile;
    AudioFile<float> out;
    AudioFile<float>::AudioBuffer newBuffer;
    unsigned int windowWidth = 4096;

    audioFile.load(input);
    int sampleRate = audioFile.getSampleRate();
    int numSamples = audioFile.getNumSamplesPerChannel();
    int realSamples = audioFile.getNumSamplesPerChannel();

    map<string, int> config;

    //Reverb bot(sampleRate, numSamples, windowWidth, COMPLETO, config);

    auto *buffer = new float[numSamples * 2];
    for (int i = 0; i < numSamples; i++) {
        if (i < realSamples) {
            buffer[2 * i] = audioFile.samples[0][i];
            buffer[2 * i + 1] = audioFile.samples[1][i];
        } else {
            buffer[2 * i] = 0;
            buffer[2 * i + 1] = 0;
        }
    }


    //freopen("output/x.txt", "w+",stdout);
    //for (int i = 0;i < numSamples;i++){
    //    cout << buffer[2*i] << '\n';
    //}


    bot->processStereoInput(buffer);
    bot->setNextOutput(buffer);

    newBuffer.resize(2);
    newBuffer[0].resize(numSamples);
    newBuffer[1].resize(numSamples);
    for (int i = 0; i < numSamples; i++) {
        newBuffer[0][i] = buffer[2*i];
        newBuffer[1][i] = buffer[2*i+1];
    }

    //freopen("output/y.txt","w+",stdout);
    //for (int i = 0;i < numSamples;i++){
    //    cout << buffer[2*i] << '\n';
    //}

    out.setAudioBuffer(newBuffer);
    out.save (output);
    delete [] buffer;

}
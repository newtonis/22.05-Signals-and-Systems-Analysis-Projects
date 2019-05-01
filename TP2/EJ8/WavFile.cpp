//
// Created by newtonis on 4/30/2019.
//

#include "WavFile.h"
#include "AudioFile.h"


void loadWavFile(string filename, vector <float> &outputA, vector <float> &outputB,int maxlength){
    outputA.clear();
    outputB.clear();

    AudioFile<float> audioFile;
    AudioFile<float> out;
    AudioFile<float>::AudioBuffer newBuffer;

    int sampleRate = audioFile.getSampleRate();
    int numSamples = audioFile.getNumSamplesPerChannel();
    cout << "loading " << filename << " sample rate " << sampleRate << '\n';
    for (int i = 0;i < min(numSamples, maxlength);i++) {
        outputA.push_back(audioFile.samples[0][i]);
        outputB.push_back(audioFile.samples[1][i]);
    }
}
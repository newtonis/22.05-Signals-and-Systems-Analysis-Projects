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

    audioFile.load(filename);
    int sampleRate = audioFile.getSampleRate();
    int numSamples = audioFile.getNumSamplesPerChannel();
    cout << "loading " << filename << "\n";
    cout << "sample rate = " << sampleRate << '\n';
    cout << "num samples = " << numSamples << '\n';

    for (int i = 0;i < min(numSamples, maxlength);i++) {
        outputA.push_back(audioFile.samples[0][i]);
        outputB.push_back(audioFile.samples[1][i]);
    }
}
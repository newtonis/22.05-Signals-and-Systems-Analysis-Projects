//
// Created by newtonis on 4/30/2019.
//

#ifndef EJ8_WAVREADER_H
#define EJ8_WAVREADER_H

#include <string>
#include <vector>

using namespace std;


void loadWavFile(string filename, vector <float> &outputA, vector <float> &outputB,int maxLength);




#endif //EJ8_WAVREADER_H

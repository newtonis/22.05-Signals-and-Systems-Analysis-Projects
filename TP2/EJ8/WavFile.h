//
// Created by newtonis on 4/30/2019.
//

#ifndef EJ8_WAVREADER_H
#define EJ8_WAVREADER_H

#include <string>
#include <vector>

using namespace std;


class WavReader {
    public:
        WavReader(string filename);
        void getContent();
    private:
        bool loaded;
        vector <float> content;

};


#endif //EJ8_WAVREADER_H

//
// Created by newto on 5/1/2019.
//

#ifndef EJ8_INPUTPARSER_H
#define EJ8_INPUTPARSER_H

#include <iostream>
#include <string>
#include "AudioEffect.h"

using namespace std;


enum{
    REALTIME,
    FILENAME
};

void parseInput();
void Robot();
void Flanger();
int RunReverb();
void Vibrato();
void Giro3d();

int EcoSimple();
int ReverbPlano();
int ReverbPB();
int ReverbCompleto();
int reverbConvolucion();

void realtimeProtocol(AudioEffect *bot);
void wavProtocol(AudioEffect *bot);

#endif //EJ8_INPUTPARSER_H

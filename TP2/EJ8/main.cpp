#include <iostream>

extern "C" {
#include "portaudio.h"
}
int main() {
    Pa_Initialize();
    std::cout << "Hello, World!" << std::endl;
    Pa_Terminate();
    return 0;
}
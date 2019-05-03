#include "windows.h"
#include <cmath>

#define pi 3.141592653589793238462643383279
#include <iostream>

void hanning(unsigned int N, std::vector<float>& hann)
{
    if (N == 0)
        return;

    //std::cout << "Hanning " << n << ":" << std::endl;

    hann.resize(N);

    float sum = 0;
    float final = 0;
    for (unsigned int n = 0; n < N; n++) {
        hann[n] = 0.5 * (1.0 - std::cos(2.0*pi*n/(N-1)));
        std::cout << hann[n] << " - ";
        sum += hann[n];
    }

//    for (unsigned int i = 0; i < N ; i++) {
//        hann[i] /= sum;
//        final += hann[i];
//    }

    std::cout << std::endl << "Suma de ventana " << N << ": " << final << std::endl;
}
#ifndef EJ8_MY_FFT_H
#define EJ8_MY_FFT_H

#include <complex>
#include <vector>

using namespace std;

void fft(vector<complex<float>>& in, vector<complex<float>>& out);
void ifft(vector<complex<float>>& in, vector<complex<float>>& out);


#endif //EJ8_MY_FFT_H

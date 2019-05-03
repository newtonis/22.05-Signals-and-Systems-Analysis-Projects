#include <bits/stdc++.h>
#include "my_fft.h"

using namespace std;

#define pi 3.141592653589793238462643383279


void generateWn(float wReal[], float wIm[],int n){
    for (int i = 0;i < n/2;i++){
        wReal[i] = cos(2*pi*i/n);
        wIm[i] = -sin(2*pi*i/n);
        wReal[i+n/2] = -wReal[i];
        wIm[i+n/2] = -wIm[i];
    }
}

void fft(vector<complex<float>>& in, vector<complex<float>>& out){
    int n = in.size();
    int log2n = 0, v = 1;
    while (v < n){
        v *= 2;
        log2n ++;
    }

    static float arrReal[4096], arrComplex[4096];
    //static *wReal = new float[n];
    //static *wIm = new float[n];
    static float wReal[4096], wIm[4096];
    static bool generated = false;
    //static bool generated[12] = {false, false, false, false, false, false, false, false, false, false, false, false};

    if (not generated) {
        //cout << "generating ..." << '\n';
        generateWn(wReal, wIm, 4096);
        generated = true;
    }

    static int reverse[13][4096];
    static int maxCalc = 1;
    static int log2Calc = 0;
    reverse[0][0] = 0;

    while (maxCalc < n){
        maxCalc *= 2;
        log2Calc ++;

        for (int j = 0;j < maxCalc;j++){
            if (j < maxCalc / 2){
                reverse[log2Calc][j] = reverse[log2Calc-1][j]*2;
            }else{
                reverse[log2Calc][j] = reverse[log2Calc][j-maxCalc/2] + 1;
            }
        }

    }

    for (int j = 0;j < n;j++){
        int r = reverse[log2n][j];
        arrReal[r] = in[j].real();
        arrComplex[r] = in[j].imag();
    }

    int pow2 = 2;
    int incFac = 4096 / n;

    for (int i = 1;pow2 <= n;i++){
        int m = pow2;
        int u = n / pow2;
        for (int k = 0;k < n;k += m){

            for (int j = 0;j < m/2;j++){
                float Wr = wReal[incFac*j*u%4096];
                float Wi = wIm[incFac*j*u%4096];

                float tReal = Wr * arrReal[k + j + m/2] - Wi * arrComplex[k + j + m/2];
                float tComplex = Wi * arrReal[k + j + m/2] + Wr * arrComplex[k + j + m/2];

                float uReal = arrReal[k + j];
                float uComplex = arrComplex[k + j];

                arrReal[k + j] = uReal + tReal;
                arrComplex[k + j] = uComplex + tComplex;
                arrReal[k + j + m/2] = uReal - tReal;
                arrComplex[k + j + m/2] = uComplex - tComplex;
            }
        }
        pow2 *= 2;
    }
    for (int i = 0;i < n;i++){
        out[i].real(arrReal[i]);
        out[i].imag(arrComplex[i]);
    }
}


void ifft(vector<complex<float>>& in, vector<complex<float>>& out){
    int n = in.size();
    int log2n = 0, v = 1;
    while (v < n){
        v *= 2;
        log2n ++;
    }

    static float arrReal[4096], arrComplex[4096];
    //static *wReal = new float[n];
    //static *wIm = new float[n];
    static float wReal[4096], wIm[4096];
    static bool generated = false;
    //static bool generated[12] = {false, false, false, false, false, false, false, false, false, false, false, false};

    if (not generated) {
        //cout << "generating ..." << '\n';
        generateWn(wReal, wIm, 4096);
        generated = true;
    }

    static int reverse[13][4096];
    static int maxCalc = 1;
    static int log2Calc = 0;
    reverse[0][0] = 0;

    while (maxCalc < n){
        maxCalc *= 2;
        log2Calc ++;

        for (int j = 0;j < maxCalc;j++){
            if (j < maxCalc / 2){
                reverse[log2Calc][j] = reverse[log2Calc-1][j]*2;
            }else{
                reverse[log2Calc][j] = reverse[log2Calc][j-maxCalc/2] + 1;
            }
        }

    }

    for (int j = 0;j < n;j++){
        int r = reverse[log2n][j];
        arrReal[r] = in[j].real();
        arrComplex[r] = in[j].imag();
    }

    int pow2 = 2;
    int incFac = 4096 / n;

    for (int i = 1;pow2 <= n;i++){
        int m = pow2;
        int u = n / pow2;
        for (int k = 0;k < n;k += m){

            for (int j = 0;j < m/2;j++){
                float Wr = wReal[ (incFac*(m-j)*u%4096)];
                float Wi = wIm[ (incFac*(m-j)*u%4096) ];

                float tReal = Wr * arrReal[k + j + m/2] - Wi * arrComplex[k + j + m/2];
                float tComplex = Wi * arrReal[k + j + m/2] + Wr * arrComplex[k + j + m/2];

                float uReal = arrReal[k + j];
                float uComplex = arrComplex[k + j];

                arrReal[k + j] = uReal + tReal;
                arrComplex[k + j] = uComplex + tComplex;
                arrReal[k + j + m/2] = uReal - tReal;
                arrComplex[k + j + m/2] = uComplex - tComplex;
            }
        }
        pow2 *= 2;
    }
    for (int i = 0;i < n;i++){
        out[i].real(arrReal[i]/n);
        out[i].imag(arrComplex[i]/n);
    }
}

//int main() {
//    freopen("input.txt", "r", stdin);
//    freopen("output_try.txt", "w+", stdout);
//
//    for (int i = 0;i < 100;i ++){
//        int n; cin >> n;
//        cout << n << '\n';
//        vector<complex<float>> in;
//        for (int j = 0;j < n;j++){
//            float v1; cin >> v1;
//            float v2; cin >> v2;
//
//            in.emplace_back(complex<float>(v1, v2));
//
//        }
//
//        fft(in , in);
//
//        for (int j = 0;j < n;j++){
//            cout << in[j].real() << '\n' << in[j].imag() << '\n';
//        }
//    }
//}
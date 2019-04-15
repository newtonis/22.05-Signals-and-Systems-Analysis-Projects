#include <bits/stdc++.h>

using namespace std;

#define pi 3.141592653589793238462643383279


void getPow2(int pow2[],int log2n){
    pow2[0] = 1;
    for (int i = 1;i <= log2n;i++) pow2[i] = pow2[i-1]*2;
}

void generateWn(float wReal[], float wIm[],int n){
    for (int i = 0;i < n/2;i++){
        wReal[i] = cos(2*pi*i/n);
        wIm[i] = -sin(2*pi*i/n);
        wReal[i+n/2] = -wReal[i];
        wIm[i+n/2] = -wIm[i];
    }
}


void fftLenta(vector<complex<float>>& in, vector<complex<float>>& out){
    int n = in.size();
    int log2n = 0, v = 1;
    while (v < n){
        v *= 2;
        log2n ++;
    }
    int pow2[log2n+1]; // declaro variables

    float dpReal[2][n], dpIm[2][n], wReal[n], wIm[n];

    getPow2(pow2, log2n);
    generateWn(wReal, wIm, n);

    for (int j = 0;j < n;j++){
        dpReal[0][j] = in[j].real();
        dpIm[0][j] = in[j].imag();
    }

    int maxjLast = n, maxkLast=1;
    for (int i = 1;i <= log2n;i++){  // proceso
        int maxj = n/pow2[i], maxk = pow2[i];

        for (int j = 0;j < maxj;j++){
            for (int k = 0;k < maxk/2;k++){
                float p1 = wReal[k*maxj%n]*dpReal[(i-1)%2][j+maxj+k%maxkLast*maxjLast];
                float p2 = wIm[k*maxj%n]*dpIm[(i-1)%2][j+maxj+k%maxkLast*maxjLast];

                dpReal[i%2][j + k*maxj] = dpReal[(i-1)%2][j+k%maxkLast*maxjLast] + p1 - p2;

                float p3 = wReal[k*maxj%n]*dpIm[(i-1)%2][j+maxj+k%maxkLast*maxjLast];
                float p4 = wIm[k*maxj%n]*dpReal[(i-1)%2][j+maxj+k%maxkLast*maxjLast];

                dpIm[i%2][j + k*maxj] = dpIm[(i-1)%2][j+k%maxkLast*maxjLast] + p3 + p4;

                dpReal[i%2][j + (k+ maxk/2)*maxj] = dpReal[(i-1)%2][j+k%maxkLast*maxjLast] - p1 + p2;
                dpIm[i%2][j + (k+maxk/2)*maxj ] = dpIm[(i-1)%2][j+k%maxkLast*maxjLast] - p3 - p4;
            }
        }
        maxjLast = maxj;
        maxkLast = maxk;
    }

    for (int k = 0;k < n;k++){
        out[k].real(dpReal[log2n%2][k*maxjLast]);
        out[k].imag(dpIm[log2n%2][k*maxjLast]);
    }
}


float dpReal[2][4096], dpIm[2][4096], wReal[4096], wIm[4096];


// fft vieja
void fft(vector<complex<float>>& in, vector<complex<float>>& out){
    // 2^log2n = n sino no funciona
    // O(n) memoria
    // n/2*logn multiplicaciones
    // O(nlogn) total

    int n = in.size();
    int log2n = 0, v = 1;
    while (v < n){
        v *= 2;
        log2n ++;
    }
    int pow2[log2n+1]; // declaro variables

    /*auto **dpReal = new float*[2];
    dpReal[0] = new float[n];
    dpReal[1] = new float[n];

    auto **dpIm = new float*[2];
    dpIm[0] = new float[n];
    dpIm[1] = new float[n];

    auto *wReal = new float[n];
    auto *wIm = new float[n];*/


    getPow2(pow2, log2n);
    generateWn(wReal, wIm, n);

    for (int j = 0;j < n;j++){
        dpReal[0][j] = in[j].real();
        dpIm[0][j] = in[j].imag();
    }

    int maxjLast = n, maxkLast=1;
    for (int i = 1;i <= log2n;i++){  // proceso
        int maxj = n/pow2[i], maxk = pow2[i];

        for (int j = 0;j < maxj;j++){
            for (int k = 0;k < maxk/2;k++){
                float p1 = wReal[k*maxj%n]*dpReal[(i-1)%2][j+maxj+k%maxkLast*maxjLast];
                float p2 = wIm[k*maxj%n]*dpIm[(i-1)%2][j+maxj+k%maxkLast*maxjLast];

                dpReal[i%2][j + k*maxj] = dpReal[(i-1)%2][j+k%maxkLast*maxjLast] + p1 - p2;

                float p3 = wReal[k*maxj%n]*dpIm[(i-1)%2][j+maxj+k%maxkLast*maxjLast];
                float p4 = wIm[k*maxj%n]*dpReal[(i-1)%2][j+maxj+k%maxkLast*maxjLast];

                dpIm[i%2][j + k*maxj] = dpIm[(i-1)%2][j+k%maxkLast*maxjLast] + p3 + p4;

                dpReal[i%2][j + (k+ maxk/2)*maxj] = dpReal[(i-1)%2][j+k%maxkLast*maxjLast] - p1 + p2;
                dpIm[i%2][j + (k+maxk/2)*maxj ] = dpIm[(i-1)%2][j+k%maxkLast*maxjLast] - p3 - p4;
            }
        }
        maxjLast = maxj;
        maxkLast = maxk;
    }

    for (int k = 0;k < n;k++){
        out[k].real(dpReal[log2n%2][k*maxjLast]);
        out[k].imag(dpIm[log2n%2][k*maxjLast]);
    }
}

/*
 * (36+0j)
(-4+9.65685424949238j)
(-4+4j)
(-4+1.6568542494923806j)
(-4+0j)
(-4-1.6568542494923806j)
(-4-4j)
(-4-9.65685424949238j)
 */
int main() {
    vector <complex<float>> arr;
//    arr.emplace_back(1);
//    arr.emplace_back(2);
//    arr.emplace_back(3);
//    arr.emplace_back(4);
//    arr.emplace_back(5);
//    arr.emplace_back(6);
//    arr.emplace_back(7);
//    arr.emplace_back(8);

    // medir tiempo
    for (int i = 0;i < 4096;i++){
        arr.emplace_back(i);
    }

    clock_t begin = clock();

    for (int i = 0;i < 100;i++) {
        fft(arr, arr);
    }

    clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;


    cout << "time global = " << elapsed_secs << '\n';

    begin = clock();

    for (int i = 0;i < 100;i++) {
        fftLenta(arr, arr);
    }

    end = clock();
    elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;

    cout << "time stack = " << elapsed_secs << '\n';

    //fftOld(arrReal, arrIm, n, log2n, ansReal, ansIm);

    //for (complex<float> item : arr){
    //    cout<<item.real()<<" + "<<item.imag()<<"j"<<'\n';
    //}

}
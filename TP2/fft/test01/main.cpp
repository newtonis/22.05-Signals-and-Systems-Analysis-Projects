#include <bits/stdc++.h>

using namespace std;

#define pi 3.141592653589793238462643383279


void getPow2(int pow2[],int log2n){
    pow2[0] = 1;
    for (int i = 1;i <= log2n;i++) pow2[i] = pow2[i-1]*2;
}

void generateWn(float wReal[], float wIm[],int n){
    for (int i = 0;i < n;i++){
        wReal[i] = cos(2*pi*i/n);
        wIm[i] = -sin(2*pi*i/n);
    }
}
void fft(vector<complex<float>>& in, vector<complex<float>>& out){
    // 2^log2n = n sino no funciona
    int n = in.size();
    int log2n = 0, v = 1;
    while (v < n){
        v *= 2;
        log2n ++;
    }
    int pow2[log2n+1]; // declaro variables
    float dpReal[2][in.size()], dpIm[2][in.size()], wReal[in.size()], wIm[in.size()];
    getPow2(pow2, log2n);
    generateWn(wReal, wIm, n);

    for (int j = 0;j < n;j++){
        dpReal[0][j] = in[j].real();
        dpIm[0][j] = in[j].imag();
    }

    int maxjLast = n, maxkLast=0, lastI = 0;
    for (int i = 1;i <= log2n;i++){  // proceso
        int maxj = n/pow2[i], maxk = pow2[i-1];

        for (int j = 0;j < maxj;j++){
            for (int k = 0;k < maxk;k++){
                int factor, indexB;
                if (maxkLast != 0) {
                    factor = (k / maxkLast) % 2 ? -1 : 1;
                    indexB = j + k % maxkLast * maxjLast;
                }else{
                    factor = 1;
                    indexB = j;
                }
                float p1 = factor*wReal[k*maxj%n]*dpReal[lastI][indexB + maxj];
                float p2 = factor*wIm[k*maxj%n]*dpIm[lastI][indexB + maxj];

                dpReal[i%2][j + k*maxj] = factor*dpReal[lastI][indexB] + p1 - p2;

                float p3 = factor*wReal[k*maxj%n]*dpIm[lastI][indexB + maxj];
                float p4 = factor*wIm[k*maxj%n]*dpReal[lastI][indexB + maxj];

                dpIm[i%2][j + k*maxj] = factor*dpIm[lastI][indexB] + p3 + p4;
            }
        }
        maxjLast = maxj;
        maxkLast = maxk;
        lastI = i;
    }
    for (int k = 0;k < n;k++){
        int indexB = (k % maxkLast)*maxjLast;
        int factor = (k / maxkLast) % 2 ? -1 : 1;
        out[k].real(factor*dpReal[log2n%2][indexB]);
        out[k].imag(factor*dpIm[log2n%2][indexB]);
    }
}

// fft vieja
void fftOld(vector<complex<float>>& in, vector<complex<float>>& out){
    // 2^log2n = n sino no funciona
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
            for (int k = 0;k < maxk;k++){
                float p1 = wReal[k*maxj%n]*dpReal[(i-1)%2][j+maxj+k%maxkLast*maxjLast];
                float p2 = wIm[k*maxj%n]*dpIm[(i-1)%2][j+maxj+k%maxkLast*maxjLast];

                dpReal[i%2][j + k*maxj] = dpReal[(i-1)%2][j+k%maxkLast*maxjLast] + p1 - p2;

                float p3 = wReal[k*maxj%n]*dpIm[(i-1)%2][j+maxj+k%maxkLast*maxjLast];
                float p4 = wIm[k*maxj%n]*dpReal[(i-1)%2][j+maxj+k%maxkLast*maxjLast];

                dpIm[i%2][j + k*maxj] = dpIm[(i-1)%2][j+k%maxkLast*maxjLast] + p3 + p4;
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

void fftLenta(const float arrReal[],const float arrIm[], int n, int log2n,float ansReal[], float ansIm[]){
    // 2^log2n = n sino no funciona
    int pow2[log2n+1]; // declaro variables
    float dpReal[log2n+1][n][n], dpIm[log2n+1][n][n], wReal[n], wIm[n];

    getPow2(pow2, log2n+1);
    generateWn(wReal, wIm, n);

    for (int j = 0;j < n;j++){
        dpReal[0][j][0] = arrReal[j];//
        dpIm[0][j][0] = arrIm[j];//
    }

    for (int i = 1;i <= log2n;i++){  // proceso
        int maxj = n/pow2[i], maxk = pow2[i];
        for (int j = 0;j < maxj;j++){
            for (int k = 0;k < maxk;k++){
                float p1 = wReal[maxj*k%n]*dpReal[i-1][j+maxj][k%pow2[i-1]];
                float p2 = wIm[maxj*k%n]*dpIm[i-1][j+maxj][k%pow2[i-1]];

                dpReal[i][j][k] = dpReal[i-1][j][k%pow2[i-1]] + p1 - p2;

                float p3 = wReal[maxj*k%n]*dpIm[i-1][j+maxj][k%pow2[i-1]];
                float p4 = wIm[maxj*k%n]*dpReal[i-1][j+maxj][k%pow2[i-1]];

                dpIm[i][j][k] = dpIm[i-1][j][k%pow2[i-1]] + p3 + p4;
            }
        }
    }

    for (int k = 0;k < n;k++){
        ansReal[k] = dpReal[log2n][0][k];
        ansIm[k] = dpIm[log2n][0][k];
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
    arr.emplace_back(1);
    arr.emplace_back(2);
    arr.emplace_back(3);
    arr.emplace_back(4);
    arr.emplace_back(5);
    arr.emplace_back(6);
    arr.emplace_back(7);
    arr.emplace_back(8);

    fftOld(arr, arr);

    //fftOld(arrReal, arrIm, n, log2n, ansReal, ansIm);

    for (complex<float> item : arr){
        cout<<item.real()<<" + "<<item.imag()<<"j"<<'\n';
    }

}
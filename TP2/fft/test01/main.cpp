#include <bits/stdc++.h>
using namespace std::literals;
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

void fft(const float arrReal[],const float arrIm[], int n, int log2n,float ansReal[], float ansIm[]){
    // 2^log2n = n sino no funciona
    int pow2[log2n+1]; // declaro variables
    float dpReal[2][n], dpIm[2][n], wReal[n], wIm[n];

    getPow2(pow2, log2n);
    generateWn(wReal, wIm, n);

    for (int j = 0;j < n;j++){
        dpReal[0][j] = arrReal[j];
        dpIm[0][j] = arrIm[j];
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
        ansReal[k] = dpReal[log2n%2][k*maxjLast];
        ansIm[k] = dpIm[log2n%2][k*maxjLast];
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
    float arrReal[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    float arrIm[8] = {0, 0, 0, 0, 0, 0, 0, 0};

    int n = 8;
    int log2n = 3;

    float ansReal[8], ansIm[8];

    fft(arrReal, arrIm, n, log2n, ansReal, ansIm);

    for (int i = 0;i < 8;i++){
        cout<<ansReal[i]<<" + "<<ansIm[i]<<"j"<<'\n';
    }

}
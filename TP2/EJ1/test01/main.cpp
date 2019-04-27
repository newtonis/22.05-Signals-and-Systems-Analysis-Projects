#include <bits/stdc++.h>

using namespace std;

#define pi 3.141592653589793238462643383279

//float dpReal[2][4096], dpIm[2][4096], wReal[4096], wIm[4096];

void show(vector <complex<float>> arr){
    for (int i = 0;i < 6;i++){
        cout << arr[i] << ' ';
    }
    cout << '\n';
}

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
unsigned int rev(unsigned int n,int maxn){
    unsigned int rev = 0;
    maxn /= 2;
    while (n > 0){
        if (n&1) {
            rev |= maxn;
        }
        maxn /= 2;
        n /= 2;
    }
    return rev;
}

void fftCormen(vector<complex<float>>& in, vector<complex<float>>& out){
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

void fft(vector<complex<float>>& in, vector<complex<float>>& out){
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




// fft vieja
void fftGlobal(vector<complex<float>>& in, vector<complex<float>>& out){
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

    float wReal[4096], wIm[4096];
    float dpReal[2][4096], dpIm[2][4096];
    int incFac = 4096 / n;

    getPow2(pow2, log2n);
    generateWn(wReal, wIm, 4096);

    for (int j = 0;j < n;j++){
        dpReal[0][j] = in[j].real();
        dpIm[0][j] = in[j].imag();
    }

    int maxjLast = n, maxkLast=1;
    for (int i = 1;i <= log2n;i++){  // proceso
        int maxj = n/pow2[i], maxk = pow2[i];

        for (int j = 0;j < maxj;j++){
            for (int k = 0;k < maxk/2;k++){
                float p1 = wReal[incFac*k*maxj%4096]*dpReal[(i-1)%2][j+maxj+k%maxkLast*maxjLast];
                float p2 = wIm[incFac*k*maxj%4096]*dpIm[(i-1)%2][j+maxj+k%maxkLast*maxjLast];

                dpReal[i%2][j + k*maxj] = dpReal[(i-1)%2][j+k%maxkLast*maxjLast] + p1 - p2;

                float p3 = wReal[incFac*k*maxj%4096]*dpIm[(i-1)%2][j+maxj+k%maxkLast*maxjLast];
                float p4 = wIm[incFac*k*maxj%4096]*dpReal[(i-1)%2][j+maxj+k%maxkLast*maxjLast];

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
    vector <complex<float>> arr2;
    vector <complex<float>> out1(256);
    vector <complex<float>> out2(4096);
    vector <complex<float>> out3(256);
    vector <complex<float>> out4(4096);
    vector <complex<float>> out5(2048);

    for (int i = 0;i < 4096;i++){
        arr.emplace_back(i);//i*454%(i+1)+1j);
    }

    clock_t begin = clock();

    for (int i = 0;i < 1000;i++){
        fftCormen(arr, out4);
    }
    clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;

    cout << "time stack = " << elapsed_secs << '\n';

    cout << "time fft 3 (cormen)= " << elapsed_secs << '\n';
    //fftOld(arrReal, arrIm, n, log2n, ansReal, ansIm);

    //show(out2);
    //show(out4);
    show(out3);
    show(out1);

}
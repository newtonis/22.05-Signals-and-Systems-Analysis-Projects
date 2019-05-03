//
// Created by newto on 5/1/2019.
//

#include "InputParser.h"
#include "Reverb.h"
#include "Realtime.h"
#include "WavProcess.h"
#include <cmath>
#include "Robotization.h"
#include "Flanger.h"
#include "Vibrato.h"

using namespace std;


void parseInput(){
    bool on = true;

    while (on) {
        cout << "Bienvenido al generador de efectos \n";
        cout << "Seleccione un efecto \n";
        cout << " - Robot" << '\n';
        cout << " - Flanger" << '\n';
        cout << " - Reverb" << '\n';
        cout << " - Vibrato" << '\n';
        cout << " - Giro-3d" << '\n';
        cout << " - Salir" << '\n';

        string comando; cin >> comando;
        int ans;

        if (comando == "Robot") {
            Robot();
        } else if (comando == "Flanger"){
            fFlanger();
        } else if (comando == "Reverb"){
            ans = RunReverb();
        } else if (comando == "Vibrato"){
            fVibrato();
        } else if (comando == "Giro 3d") {
            Giro3d();
        } else if (comando == "Salir"){
            cout << "Saliendo ... \n"; on = false;
        } else if (comando == "Restart") {
            cout << "Restart ... \n";
        }else{
            cout << "Comando incorrecto \n";
        }

        if (ans == -1){
            cout << "Saliendo ... \n"; on = false;
        }
    }
}
int RealOrWav(){
    cout << "Seleccionar modo " << '\n';
    cout << " - Realtime" << '\n';
    cout << " - Filename " << '\n';
    string modo;
    cin >> modo;

    if (modo == "Realtime") {
        cout << "Modo 'Realtime' seleccionado " << '\n';
        return REALTIME;
    } else if (modo == "Filename") {
        cout << "Modo 'Filename' seleccionado " << '\n';
        return FILENAME;
    } else {
        cout << "Comando incorrecto \n";
        return -1;
    }

}
int Robot(){
    cout << "Robotización seleccionada \n";
    cout << "Seleccionar ancho de ventana (2-12)\n";

    int ancho; cin >> ancho;
    if (ancho == -1) {
        return -1;
    }
    int windowWidth = (int)pow(2, ancho);

    cout << "Ancho seleccionado = " << ancho << '\n';
    int mode = RealOrWav();

    auto *bot = new Robotization(44100, 4096, windowWidth);

    if (mode == REALTIME){
        realtimeProtocol((AudioEffect*)bot);
    }else if(mode == FILENAME){
        wavProtocol((AudioEffect*)bot);
    }

    return 0;
}
int fFlanger(){
    cout << "Flanger seleccionada \n";
    cout << "Frecuencia de modulacion (0 - 5 hz) \n";

    float fm; cin >> fm;
    if (fm < 0){
        return -1;
    }

    cout << "frecuencia de modulacion = " << fm << '\n';
    cout << "Profundidad de modulacion (0 - 20 ms)" << '\n';
    float pm; cin >> pm;
    if (pm < 0){
        return -1;
    }

    int mode = RealOrWav();

    auto *bot = new Flanger(44100, 4096, fm, pm);

    if (mode == REALTIME){
        realtimeProtocol((AudioEffect*)bot);
    }else if(mode == FILENAME){
        wavProtocol((AudioEffect*)bot);
    }
    return 0;
}
int RunReverb(){
    cout << "Seleccionado Reverb ... \n";
    cout << "Seleccionar tipo de Reverb \n";
    cout << " - Eco-simple \n";
    cout << " - Reverberador-plano \n";
    cout << " - Reverberador-pasa-bajos \n";
    cout << " - Reverberador-completo \n";
    cout << " - Reverberador-convolucion \n";
    fflush(stdout);
    fflush(stdin);

    string modo; cin >> modo;
    if (modo == "Eco-simple"){
        EcoSimple();
    }else if(modo == "Reverberador-plano") {
        ReverbPlano();
    }else if(modo == "Reverberador-pasa-bajos") {
        ReverbPB();
    }else if(modo == "Reverberador-completo") {
        ReverbCompleto();
    }else if(modo == "Reverberador-convolucion"){
        reverbConvolucion();
    }else if (modo == "Salir"){
        return -1;
    }else if (modo == "Restart") {
        return 0;
    }else{
        cout << "No ha sido implementado aún";
    }

    return 0;
}
int fVibrato(){
    cout << "Vibrato seleccionado \n";
    cout << "Frecuencia de modulacion (0 - 5 hz) \n";

    float fm; cin >> fm;
    if (fm < 0) {
        return -1;
    }
    cout << "frecuencia de modulacion = " << fm << '\n';
    cout << "Profundidad de modulacion (0 - 20 ms)" << '\n';
    float pm; cin >> pm;
    if (pm < 0){
        return -1;
    }
    int mode = RealOrWav();

    auto *bot = new Vibrato(44100, 4096, fm, pm);

    if (mode == REALTIME){
        realtimeProtocol((AudioEffect*)bot);
    }else if(mode == FILENAME){
        wavProtocol((AudioEffect*)bot);
    }
    return 0;
}
int Giro3d(){
    cout << "No ha sido implementado aún\n";
    return 0;
}
int EcoSimple(){
    cout << "Eco simple seleccionado \n";
    cout << "Seleccionar g y m" << '\n';
    cout << "g = \n";
    float g; cin >> g;
    if (g < 0) return -1;
    cout << "m = \n";
    int m; cin >> m;

    if (m < 5 or m > 10000){
        return -1; // parametros invalidos
    }
    if (g < 0 or g > 1){
        return -1; // invalido
    }
    cout << "Fueron configurados los parametros del eco simple \n";
    int mode = RealOrWav();

    auto *bot = new Reverb(44100, 4096, 4096, ECO);
    bot->myG = g;
    bot->myM = m;


    if (mode == REALTIME){
        realtimeProtocol((AudioEffect*)bot);
    }else if(mode == FILENAME){
        wavProtocol((AudioEffect*)bot);
    }


    return 0;
}
void realtimeProtocol(AudioEffect *bot){
    string msg;
    cout << "Comandos de realtime \n";
    cout << "- Exit \n";
    cout << "- Wait \n";
    bool on = true;

    while (on) {
        string cur_msg;
        Realtime(bot, cur_msg);
        if (cur_msg == "Exit"){
            on = false;
        }else if (cur_msg == "Wait") {
            cout << "Escribir algo distinto de 'Exit' para volver a empezar\n";
            string smt;
            cin >> smt;
            if (smt == "Exit"){
                on = false;
            }
        }
    }
}

void wavProtocol(AudioEffect *bot){
    while (true) {
        cout << "Se ha seleccionado la opcion para procesar wav (Escribir 'Salir' para terminar)\n";
        cout << "Archivo de entrada : " << '\n';
        fflush(stdout);
        fflush(stdin);

        string entrada;
        cin >> entrada;
        cout << "Entrada = " << entrada << '\n';

        if (entrada == "Salir"){
            break;
        }
        cout << "Archivo de salida : " << '\n';
        string salida;
        cin >> salida;
        if (salida == "Salir"){
            break;
        }

        cout << "Salida = " << salida << '\n';
        cout << "Procesando \n";
        wavProcess(bot, entrada, salida);
        cout << "Terminado\n";
        cout << "Archivos procesados con exito\n";
    }
    cout << "Se ha salido de la opcion para procesar wav \n";
}


int ReverbPlano(){
    cout << "Reverb plano seleccionado \n";
    cout << "Seleccionar g y m" << '\n';
    cout << "g = \n";
    float g; cin >> g;
    if (g < 0) return -1;
    cout << "m = \n";
    int m; cin >> m;

    if (m < 5 or m > 10000){
        return -1; // parametros invalidos
    }
    if (g < 0 or g > 1){
        return -1; // invalido
    }
    cout << "Fueron configurados los parametros del eco simple \n";
    int mode = RealOrWav();

    auto *bot = new Reverb(44100, 4096, 4096, PLANO);
    bot->myG = g;
    bot->myM = m;

    if (mode == REALTIME){
        realtimeProtocol((AudioEffect*)bot);
    }else if(mode == FILENAME){
        wavProtocol((AudioEffect*)bot);
    }
    return 0;
}
int ReverbPB(){
    cout << "Reverb pasa bajo seleccionado \n";
    cout << "Seleccionar g y m" << '\n';
    cout << "g = \n";
    float g; cin >> g;
    if (g < 0) return -1;

    cout << "m = \n";
    int m; cin >> m;
    if (m == -1) return -1;

    if (m < 5 or m > 10000){
        return -1; // parametros invalidos
    }
    if (g < 0 or g > 1){
        return -1; // invalido
    }
    cout << "Fueron configurados los parametros del eco simple \n";
    int mode = RealOrWav();

    auto *bot = new Reverb(44100, 4096, 4096, PASABAJO);
    bot->myG = g;
    bot->myM = m;

    if (mode == REALTIME){
        realtimeProtocol((AudioEffect*)bot);
    }else if(mode == FILENAME){
        wavProtocol((AudioEffect*)bot);
    }
    return 0;
}
int ReverbCompleto(){
    cout << "Reverb completo seleccionado \n";
    cout << "Cantidad de filtros en paralelo: \n";

    int pf; cin >> pf;
    if (pf == -1) return -1;

    cout << "Cantidad de filtros en serie: \n";
    int cc; cin >> cc;
    if (cc == -1) return -1;

    cout << "Delay filtros en serie: \n";
    int dc; cin >> dc;
    if (dc == -1) return -1;
    cout << "Ganancia filtros en serie:" << '\n';
    float gc; cin >> gc;
    if (gc == -1) return -1;

    if (gc < 0 or gc > 1) return -1;
    if (pf < 1 or pf > 15) return -1;
    if (dc < 5 or dc > 10000) return -1;

    auto *bot = new Reverb(441000, 4096, 4096, COMPLETO);

    bot->configureReverbCompleto(
            pf,
            cc,
            dc,
            gc);


    int mode = RealOrWav();
    if (mode == REALTIME){
        realtimeProtocol((AudioEffect*)bot);
    }else if(mode == FILENAME){
        wavProtocol((AudioEffect*) bot);
    }
    return 0;
}

int reverbConvolucion(){
    cout << "Reverb por convolución seleccionado \n";
    cout << "Seleccionar respuesta al impulso \n";
    cout << "Filename = \n";
    string filename; cin >> filename;
    if (filename == "Salir") return -1;
    cout << "Archivo seleccionado : " << filename << '\n';


    auto *bot = new Reverb(441000, 4096, 4096, CONVOLUCION);
    bot->wavFile = filename;

    int mode = RealOrWav();
    if (mode == REALTIME){
        realtimeProtocol((AudioEffect*)bot);
    }else if(mode == FILENAME){
        wavProtocol((AudioEffect*) bot);
    }
    return 0;
}

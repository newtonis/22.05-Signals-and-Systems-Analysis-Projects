//
// Created by newto on 5/1/2019.
//

#include "InputParser.h"
#include "Reverb.h"
#include "Realtime.h"
#include "WavProcess.h"

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
            Flanger();
        } else if (comando == "Reverb"){
            ans = RunReverb();
        } else if (comando == "Vibrato"){
            Vibrato();
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
void Robot(){
    cout << "No ha sido implementado aún \n";
}
void Flanger(){
    cout << "No ha sido implementado aún \n";
}
int RunReverb(){
    cout << "Seleccionado Reverb ... \n";
    cout << "Seleccionar tipo de Reverb \n";
    cout << " - Eco-simple \n";
    cout << " - Reverberador-plano \n";
    cout << " - Revervbrador-pasa-bajos \n";
    cout << " - Reverberador-completo \n";
    cout << " - Reverberador-convolución \n";
    fflush(stdout);
    fflush(stdin);

    string modo; cin >> modo;
    if (modo == "Eco-simple"){
        EcoSimple();
    }else if(modo == "Reverberador-plano"){
        cout << "No ha sido implementado aún";
    }else if (modo == "Salir"){
        return -1;
    }else if (modo == "Restart") {
        return 0;
    }else{
        cout << "No ha sido implementado aún";
    }

    return 0;
}
void Vibrato(){
    cout << "No ha sido implementado aún\n";
}
void Giro3d(){
    cout << "No ha sido implementado aún\n";
}
int EcoSimple(){
    cout << "Eco simple seleccionado \n";
    cout << "Seleccionar g y m" << '\n';
    cout << "g = \n";
    float g; cin >> g;
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
    cout << "Se ha seleccionado la opcion para procesar wav \n";
    cout << "Archivo de entrada : " << '\n';
    string entrada; cin >> entrada;
    cout << "Archivo de salida : " << '\n';
    string salida; cin >> salida;

    wavProcess(bot, entrada, salida);

}

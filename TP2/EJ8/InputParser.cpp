//
// Created by newto on 5/1/2019.
//

#include "InputParser.h"
#include "Reverb.h"

#include <string>
using namespace std;



void Robot();
void Flanger();
int Reverb();
void Vibrato();
void Giro3d();
int EcoSimple();

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
            ans = Reverb();
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
int Reverb(){
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




    return 0;
}
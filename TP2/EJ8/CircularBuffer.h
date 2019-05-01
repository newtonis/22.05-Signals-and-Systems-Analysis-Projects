//
// Created by Rocío Parra on 27-Apr-19.
//

#ifndef EJ8_CIRCULARBUFFER_H
#define EJ8_CIRCULARBUFFER_H
#include <vector>

class CircularBuffer {
public:
    CircularBuffer(unsigned int initMaxSize, unsigned int stepMaxSize = 0);
    //si no le paso step lo hace igual a initMaxSize
    ~CircularBuffer();

    float read(unsigned int n);
    bool write(unsigned int n, float data);
    // posiciones que ya existen: sobre escribe
    // una posicion mas que la maxima: igual a push_back(data)
    // si no: error

    void push_back(float data);
    void push_front(float data);
    bool pop_front(unsigned int n); // saca los primeros n datos
    void pop_back(unsigned int n);
    void clear();
    float next(); // pop_front(1) y devuelve el dato que se saco



    unsigned int currSize();
    bool isFull();
    bool empty();
    void getCopy(std::vector<float>& copy);


private:
    std::vector<float> buffer;
    unsigned int currFullSize;    //tamanio total del vector
    unsigned int stepMaxSize;

    unsigned int first;         // donde esta el primer elemento
    unsigned int last;          // donde va a estar el proximo
    bool full;

    std::vector<float> backup;

    void rearrange(); // pone los datos a partir de la posicion 0
    void resize(unsigned int n, float fill = 0);
    // si lo hago mas chico saco los ultimos
    // si lo hago mas grande lleno con fill

};


#endif //EJ8_CIRCULARBUFFER_H

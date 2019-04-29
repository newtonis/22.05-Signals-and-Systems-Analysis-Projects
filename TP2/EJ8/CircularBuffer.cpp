//
// Created by Rocío Parra on 27-Apr-19.
//

#include "CircularBuffer.h"

#include <algorithm>

CircularBuffer::CircularBuffer(unsigned int initMaxSize, unsigned int stepMaxSize)
{
    buffer = std::vector<float>(initMaxSize);
    first = 0;
    last = 0;
    currFullSize = initMaxSize;
    full = false;

    backup = std::vector<float>(initMaxSize);

    if (stepMaxSize == 0) {
        stepMaxSize = initMaxSize;
    }
    this->stepMaxSize = stepMaxSize;
}

CircularBuffer::~CircularBuffer()
{
    last = first;
    full = true;
}

unsigned int CircularBuffer::currSize() {
    if (first == last) {
        if (full)
            return currFullSize;
        else
            return 0;
    }

    if (first < last) {
        return last - first;
    }
    else {
        return currFullSize - first + last - 1;
    }
}

void CircularBuffer::emplace(float data) {
    if (full) {
        rearrange();
        if (currSize() == currFullSize) {
            last = currFullSize;
            currFullSize += stepMaxSize;
            buffer.resize(currFullSize);
            backup.resize(currFullSize);
            full = false;
        }
    }

    buffer[last++] = data;

    if (last == currFullSize) {
        last = 0;
    }

    if (last == first) {
        full = true;
    }
}

bool CircularBuffer::pop(unsigned int n) {
    if (currSize() >= n) {
        first = (first + n) % currFullSize;
        if (n) {
            full = false;
        }
        return true;
    }
    else {
        return false;
    }
}

float CircularBuffer::next() {
    float data = 0;
    if (currSize()) {
        data = buffer[first];
        pop(1);
    }
    return data;
}

void CircularBuffer::rearrange() {
    unsigned int curr = currSize();
    if (curr != 0 && first != 0) {
        getCopy(buffer);

        for (unsigned int i = 0; i < curr; i++) {
            buffer[i] = backup[i];
        }

        first = 0;
        last = curr%currFullSize; // si esta lleno es 0, si no es curr
    }
}

float CircularBuffer::read(unsigned int n) {
    float data = 0;
    if (currSize() > n) {
        data = buffer[(first + n) % currFullSize];
    }
    return data;
}

bool CircularBuffer::write(unsigned int n, float data) {
    unsigned int curr = currSize();
    if (n == curr) {
        emplace(data);
    }
    else if (n < curr) {
        buffer[(first + n) % currFullSize] = data;
    }
    else {
        return false;
    }

    return true;
}

void CircularBuffer::resize(unsigned int n, float fill) {
    if (n <= currFullSize) {
        unsigned int previousSize = currSize();
        last = (first + n) % currFullSize;

        // si el tamanio actual es mayor que el anterior lleno los nuevos
        for (unsigned int i = previousSize; i < n; i++) {
            write(i, fill);
        }

        if (n == currFullSize) {
            full = true;
        }
    }
    else {
        unsigned int newSize = currFullSize + stepMaxSize * ((n-currFullSize)/stepMaxSize + 1);
        if ((n-currFullSize)%stepMaxSize == 0) {
            newSize -= stepMaxSize;
        }

        rearrange();
        buffer.resize(newSize, fill);
        backup.resize(newSize);
    }
}

void CircularBuffer::getCopy(std::vector<float>& copy) {
    unsigned int curr = currSize();
    if (copy.size() < curr) {
        copy.resize(curr);
    }

    for (unsigned int i = 0; i < curr; i++) {
        copy[i] = buffer[(first + i)%currFullSize];
    }
}

void CircularBuffer::clear() {
    last = first;
    full = false;
}

bool CircularBuffer::isFull() {
    return full;
}




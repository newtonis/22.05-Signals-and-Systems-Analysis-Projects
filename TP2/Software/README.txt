
Se debe instalar visual studio para poder correr simpleAudio

Se debe instalar ffmpeg y debe ser agregado al path la carpeta bin de su instalacion
(Advanced system settings -> enviroment variables-> path)

El resto es instalacion de librerias comun


Correr el archivo generateDemoSounds para generar los sonidos de prueba de los instrumentos siempre que se
modifican o se agregan instrumentos nuevos

Modificar el archivo ProcessMidi/InstrumentsSynth/instrumentos.xml para configurar nuevos instrumentos.
Agregar su codigo en la carpeta ProcessMidi/InstrumentsSynth/Instruments que debe tener la funcion

nombreFuncion(vel, fm, duration, fs)

donde vel es la intensidad (que tan fuerte se apretó la tecla)
fm es la frecuencia fundamental, es decir la nota musical
duration es la duracion en segundos del sonido
fs es la frecuencia de muestreo, que en este software siempre será 44.1 kHz


El programa principal es UI.py

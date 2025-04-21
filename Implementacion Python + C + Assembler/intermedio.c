#include <stdio.h>

extern float suma_en_asm(float valor);  // Ensamblador espera float por pila

float convertir_float(float valor) {
    return suma_en_asm(valor);  // Se pasa por pila en cdecl
}
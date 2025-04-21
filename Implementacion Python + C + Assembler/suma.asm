global suma_en_asm

section .text
suma_en_asm:
    push ebp
    mov ebp, esp

    ; Cargar el parámetro float desde la pila
    fld dword [ebp+8]      ; ST(0) = valor

    ; Cargar 1.0 en la FPU
    fld1                   ; ST(0) = 1.0, ST(1) = valor

    ; Sumar ST(0) + ST(1) → ST(1)
    faddp st1, st0         ; ST(0) = resultado

    ; Retornar el float por ST(0)
    pop ebp
    ret

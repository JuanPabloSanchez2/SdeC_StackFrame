# SdeC_StackFrame
Se desarrolla en el siguiente repositorio, el practico #2 de Sistemas de Computación


## Diagramas

### Diagrama de bloques
```mermaid
graph TD
    A[main.py] -->|Llama a API| B[mi_servidor.py]
    B -->|Llama a función en C| C[intermedio.c]
    C -->|Llama a ensamblador| D[suma.asm]
    D -->|Devuelve resultado| C
    C -->|Devuelve resultado| B
    B -->|Devuelve resultado| A

```
### Diagrama de secuencia
```mermaid
sequenceDiagram
    participant Usuario
    participant main.py
    participant mi_servidor.py
    participant intermedio.c
    participant suma.asm

    Usuario->>main.py: Ejecuta script
    main.py->>mi_servidor.py: Llama a convertir_float_sv
    mi_servidor.py->>intermedio.c: Llama a función en C (convertir_float)
    intermedio.c->>suma.asm: Llama a función en ensamblador (suma_en_asm)
    suma.asm-->>intermedio.c: Devuelve resultado
    intermedio.c-->>mi_servidor.py: Devuelve resultado
    mi_servidor.py-->>main.py: Devuelve resultado
    main.py-->>Usuario: Muestra resultado
   ```

## Depuracion

### Verificacion del stack con gdb

![Screenshot from 2025-04-21 10-04-26](https://github.com/user-attachments/assets/5240ede2-6db1-4d93-86ff-89603dce2916)
![Screenshot from 2025-04-21 10-05-04](https://github.com/user-attachments/assets/8cfb6436-f0cd-43f3-aea7-f53fe97f5e7b)
![Screenshot from 2025-04-21 10-05-36](https://github.com/user-attachments/assets/b4a1731c-b56a-4137-9a50-e0427bb1416e)
![Screenshot from 2025-04-21 10-07-00](https://github.com/user-attachments/assets/360a6ca4-acec-4f2f-8654-3e75b21cd194)

----

### Profiling
Profiling del programa sin asm:

![Screenshot from 2025-04-21 10-19-14](https://github.com/user-attachments/assets/51f77b50-7484-405a-bf4f-182871a8cfa6)

----

Profiling del programa con asm:

![Screenshot from 2025-04-21 10-17-46](https://github.com/user-attachments/assets/8c606eab-bce5-4306-a620-aa5320b6cf3f)



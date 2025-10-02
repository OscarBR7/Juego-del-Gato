# Juego del Gato

Este proyecto implementa **juego del gato** en Python, donde un humano juega contra una máquina que utiliza el **algoritmo Minimax** para tomar decisiones inteligentes.  
El tablero se muestra en la terminal y el jugador humano interactúa introduciendo el número de la celda donde desea colocar su símbolo.

---

## Tecnologías utilizadas

- Python 
- Librería `random` – para seleccionar aleatoriamente quién inicia el juego y qué símbolo usará cada jugador  
- Librería `math` – para utilizar infinito positivo y negativo en el algoritmo Minimax  
- Librería `os` – para limpiar la terminal y mejorar la experiencia visual

---

## Estructura del proyecto

```
PROYECTO-GATO
│
├── gato.py               # Código principal del juego
├── leeme.txt             # Instrucciones básicas de ejecución
└── README.md             # Este archivo de documentación
```

---

## Instalación

1. Tener instalado **Python 3.x**.  
   Puedes descargarlo desde:  
   https://www.python.org/downloads/

2. Usar cualquier editor de código (VS Code, PyCharm, etc.) o incluso el Bloc de notas.  

3. Tener acceso a una terminal para ejecutar el programa:  
   - En Windows: CMD o PowerShell  
   - En Linux/Mac: Terminal  

---

## Ejecución

1. Descargar el archivo o clonar el repositorio.  
2. Abrir una terminal.  
3. Navegar hasta la ubicación del archivo con el comando `cd`.  
4. Ejecutar el programa con el siguiente comando:

```
python gato.py
```

(o en algunos entornos también funciona con `py gato.py`).

5. Seguir las instrucciones en pantalla:  
   - El humano introduce un número del 1 al 9 para colocar su ficha en el tablero.  
   - La máquina responde automáticamente con la mejor jugada calculada con **Minimax**.  

6. El juego termina cuando alguno de los jugadores gana o si no quedan celdas disponibles (empate).

---

## Autor

Proyecto desarrollado como práctica de **Agentes Inteligentes con Minimax en Python**.

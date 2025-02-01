# 🐍 Snake Game

¡Bienvenido al repositorio del clásico juego del gusanito! Este proyecto está desarrollado en Python utilizando la librería `pygame`. Incluye niveles, dificultad progresiva, puntuación y colisiones.

## Estructura

    python-snake-game/
    │
    ├── src/
    │   ├── constants.py
    │   ├── game.py
    │   ├── snake.py
    │   ├── food.py
    │   ├── levels.py
    │   ├── main.py
    │   └── fonts/
    │       └── Roboto-Regular.ttf
    │
    ├── .gitignore
    ├── requirements.txt
    └── high_score.txt

## 🛠️ Requisitos

Antes de ejecutar el juego, asegúrate de tener instalado Python 3.12 y las dependencias necesarias.

1.  **Instalar Python**:
    Descarga Python desde [python.org](https://www.python.org/downloads/).

2. **Crear y activar un entorno virtual**:

   - **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3.  **Instalar dependencias**:
    Ejecuta el siguiente comando para instalar las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

## 🎮 Cómo Ejecutar el Juego

1.  Clona este repositorio o descarga los archivos del proyecto.
2.  Navega a la carpeta del proyecto:

    ```bash
    cd python-snake-game
    ```

3.  Ejecuta el juego:

    ```bash
    python src/main.py
    ```

## 🚀 Generar un Ejecutable (.exe)

Si deseas generar un archivo ejecutable para Windows, sigue estos pasos:

1.  Instala pyinstaller:

    ```bash
    pip install pyinstaller
    ```

2.  Genera el ejecutable:

    ```bash
    pyinstaller --onefile src/main.py --name snake_game
    ```

El archivo .exe se generará en la carpeta `dist/`.

2.  Genera el ejecutable:

    ```bash
    ./dist/snake_game
    ```

## 🎯 Características del Juego

*   **Niveles**: Cada 50 puntos, el nivel aumenta y la velocidad del juego se incrementa.
*   **Dificultad**: La velocidad aumenta con cada nivel.
*   **Puntuación**: Se muestra en la pantalla.
*   **Colisiones**: La serpiente muere si choca consigo misma.

## 🕹️ Controles

*   Flecha arriba (↑): Mover hacia arriba.
*   Flecha abajo (↓): Mover hacia abajo.
*   Flecha izquierda (←): Mover hacia la izquierda.
*   Flecha derecha (→): Mover hacia la derecha.

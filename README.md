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

3.  Asegúrate de que tu entorno virtual esté activado.
4.  Ejecuta el juego:

    ```bash
    python src/main.py
    ```

## 🚀 Generar un Ejecutable (.exe)

Si deseas generar un archivo ejecutable para Windows, sigue estos pasos:

1.  Asegúrate de que tu entorno virtual esté activado.
2.  Instala `pyinstaller`:

    ```bash
    pip install pyinstaller
    ```

3.  Genera el ejecutable:

    ```bash
    pyinstaller --onefile --add-data "src/fonts;fonts" src/main.py --name snake_game
    ```

    El archivo `.exe` se generará en la carpeta `dist/`.

4.  Ejecuta el juego generado:

    - **Windows**:
      ```bash
      .\dist\snake_game.exe
      ```
    - **macOS/Linux** (si generaste para tu sistema):
      ```bash
      ./dist/snake_game
      ```

## 🎯 Características del Juego

* **Niveles**: Cada 50 puntos, el nivel aumenta y la velocidad del juego se incrementa progresivamente, haciendo el juego más desafiante.
* **Dificultad**: La velocidad del juego aumenta con cada nivel.
* **Puntuación**: Tu puntuación actual se muestra en la pantalla durante el juego.
* **Colisiones**: La serpiente muere si choca consigo misma o con los límites del área de juego.
* **Sistema de Récords**: El juego guarda automáticamente tu puntuación más alta junto con el nombre del jugador que la obtuvo.

## 🕹️ Controles

* Flecha arriba (↑): Mover hacia arriba.
* Flecha abajo (↓): Mover hacia abajo.
* Flecha izquierda (←): Mover hacia la izquierda.
* Flecha derecha (→): Mover hacia la derecha.

## 💡 Posibles Mejoras Futuras

* Diferentes tipos de comida con efectos variados.
* Introducción de obstáculos estáticos o móviles.
* Modo de juego con múltiples jugadores.
* Funcionalidad de pausa en el juego.
* Efectos de sonido y música de fondo.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` (si se añade) para más detalles.

---

Para implementar estos cambios, simplemente copia el contenido de cada bloque de código y reemplázalo en el archivo correspondiente en tu repositorio.
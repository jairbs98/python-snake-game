FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip --no-cache-dir -r requirements.txt
RUN pip install pyinstaller

COPY src/ ./src/

# Usa pyinstaller para generar el ejecutable
RUN pyinstaller --onefile src/main.py

# Cambia el directorio de trabajo al directorio donde se encuentra el ejecutable
WORKDIR /app/dist

# Define el comando por defecto para el contenedor
CMD ["./main"]
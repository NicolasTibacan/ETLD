# Usar una imagen base de Python 3.11
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para algunas librerías de Python
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requerimientos
COPY requiment.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requiment.txt

# Copiar todo el código del proyecto al contenedor
COPY . .

# Crear el directorio para las gráficas si no existe
RUN mkdir -p analist/plots

# Establecer variables de ambiente para evitar problemas con matplotlib
ENV MPLBACKEND=Agg

# Comando por defecto para ejecutar el proyecto
CMD ["python", "mayn.py"]

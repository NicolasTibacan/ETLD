# 🐳 Guía de Uso de Docker para ETL F1 Project

## 📋 Requisitos Previos

- Docker instalado en tu sistema
- Docker Compose (opcional, pero recomendado)

## 🚀 Construir la Imagen Docker

### Opción 1: Usando Docker directamente

```bash
docker build -t etld-f1-project:latest .
```

### Opción 2: Usando Docker Compose

```bash
docker-compose build
```

## ▶️ Ejecutar el Contenedor

### Opción 1: Ejecución simple (una vez)

```bash
docker run --rm \
  -v $(pwd)/analist/plots:/app/analist/plots \
  -v $(pwd)/Extract/archive:/app/Extract/archive \
  etld-f1-project:latest
```

### Opción 2: Usando Docker Compose

```bash
docker-compose up
```

Para ejecutar en segundo plano:
```bash
docker-compose up -d
```

Para detener y eliminar el contenedor:
```bash
docker-compose down
```

## 🔧 Configuración de Variables de Entorno

Si necesitas conectarte a Railway u otra base de datos externa, crea un archivo `.env` en la raíz del proyecto:

```env
DB_HOST=tu_host_railway
DB_PORT=5432
DB_NAME=tu_base_de_datos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
```

Y modifica el `docker-compose.yml` para incluir:

```yaml
env_file:
  - .env
```

## 📂 Volúmenes Montados

El contenedor monta los siguientes directorios:

- `./analist/plots` → Para guardar las gráficas generadas
- `./Extract/archive` → Para acceder a los archivos CSV
- `./data` → Para la base de datos SQLite local (si se usa)

## 🐛 Solución de Problemas

### Ver logs del contenedor

```bash
docker logs etld-f1-container
```

### Entrar al contenedor en modo interactivo

```bash
docker run -it --rm etld-f1-project:latest /bin/bash
```

### Limpiar imágenes antiguas

```bash
docker system prune -a
```

## 📦 Tamaño de la Imagen

La imagen construida tiene aproximadamente **919 MB**.

## ✅ Verificar que la Imagen se Creó

```bash
docker images | grep etld-f1-project
```

Deberías ver algo como:
```
etld-f1-project   latest    ae3aa91f1091   2 minutes ago   919MB
```

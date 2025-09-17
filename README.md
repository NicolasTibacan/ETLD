# 🏎️📊 Proyecto ETL + Análisis F1 Drivers

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) complementado con un módulo de análisis visual para explorar datos de pilotos de Fórmula 1.

El flujo completo no solo limpia y carga los datos en una base de datos (Railway o SQLite), sino que también genera gráficas automáticas sobre el rendimiento de los corredores.

🚀 ¿Qué hace este código?

✅ ETL Automático:

Extract → Lee el dataset de pilotos (F1Drivers_Dataset.csv).

Transform → Limpia duplicados, estandariza columnas, rellena nulos y genera una copia limpia (F1Drivers_Dataset_CLEAN.csv).

Load → Carga los datos en una BD en Railway (PostgreSQL/MySQL).

Si la conexión falla, usa SQLite local (f1_drivers.db).

Revisa si la tabla ya existe → si existe inserta nuevos datos, si no la crea.

✅ Análisis Visual Automático (carpeta analist/):

Genera y guarda gráficas con Seaborn:

📊 Corredor y número de podios

🏆 Corredor y número de victorias

⏱️ Corredor y número de pole positions
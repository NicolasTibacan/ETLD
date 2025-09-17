from Extract.extrac import extract_data
from tranform.tranform import transform_data
from load.load import load_data
from analist.analist import run_analysis   # 👈 Importamos el análisis

def main():
    print("🚦 Iniciando ETL F1 Drivers...")

    # 1. Extract
    df = extract_data()
    print(f"📥 Datos extraídos: {df.shape[0]} filas, {df.shape[1]} columnas")

    # 2. Transform
    df_clean = transform_data(df)
    print(f"🔧 Datos transformados: {df_clean.shape[0]} filas")

    # 3. Load
    load_data(df_clean)

    # 4. Analysis
    print("📊 Generando gráficas de análisis...")
    run_analysis()

    print("🏁 ETL + Análisis completados!")

if __name__ == "__main__":
    main()

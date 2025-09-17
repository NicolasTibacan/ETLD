import pandas as pd
import os

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Eliminar duplicados
    df = df.drop_duplicates()
    
    # Quitar espacios extra en nombres de columnas
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    # Rellenar valores nulos
    df = df.fillna("Unknown")
    
    # Asegurar tipos (ejemplo si hay año)
    if "year" in df.columns:
        df["year"] = pd.to_numeric(df["year"], errors="coerce").fillna(0).astype(int)

    # 📂 Guardar versión limpia
    output_path = os.path.join(os.path.dirname(__file__), "..", "Extract", "archive", "F1Drivers_Dataset_CLEAN.csv")
    df.to_csv(output_path, index=False)
    print(f"💾 Archivo limpio guardado en: {output_path}")

    return df

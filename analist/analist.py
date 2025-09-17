import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_analysis():
    # Ruta al dataset limpio
    file_path = os.path.join(os.path.dirname(__file__), "..", "Extract", "archive", "F1Drivers_Dataset_CLEAN.csv")
    df = pd.read_csv(file_path)

    # Crear carpeta de salida para gráficas
    plots_dir = os.path.join(os.path.dirname(__file__), "plots")
    os.makedirs(plots_dir, exist_ok=True)

    # ========================
    # 1. Corredor y podios
    # ========================
    if "driver" in df.columns and "podiums" in df.columns:
        top_podiums = df.sort_values("podiums", ascending=False).head(15)  # Top 15 corredores
        plt.figure(figsize=(12,6))
        sns.barplot(data=top_podiums, x="driver", y="podiums", palette="coolwarm")
        plt.xticks(rotation=45)
        plt.title("Corredores y número de podios")
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, "corredor_y_podios.png"))
        plt.close()

    # ========================
    # 2. nacionalidad y cantidad de pilotos
    # ========================
    plt.figure(figsize=(12,6))
    sns.countplot(data=df, x="nationality", order=df["nationality"].value_counts().index)
    plt.xticks(rotation=45)
    plt.title("Número de pilotos por nacionalidad")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "pilotos_por_nacionalidad.png"))
    plt.close()

    # ========================
    # 3. Corredores y pole position
    # ========================
    if "driver" in df.columns and "pole_positions" in df.columns:
        top_poles = df.sort_values("pole_positions", ascending=False).head(15)  # Top 15 corredores
        plt.figure(figsize=(12,6))
        sns.barplot(data=top_poles, x="driver", y="pole_positions", palette="magma")
        plt.xticks(rotation=45)
        plt.title("Corredores y número de pole positions")
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, "corredor_y_pole_position.png"))
        plt.close()

    print(f"📊 Gráficas creadas y guardadas en: {plots_dir}")

if __name__ == "__main__":
    run_analysis()

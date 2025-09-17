from sqlalchemy import create_engine, inspect
from config.Config import Config

def load_data(df, table_name="f1_drivers"):
    try:
        # Intentar conectar a Railway (Postgres, MySQL, etc.)
        engine = create_engine(Config.DB_URL)
        print(f"🔗 Conectado a la BD: {Config.DB_URL}")
    except Exception as e:
        print(f"⚠️ Error al conectar con {Config.DB_URL}, usando SQLite local. Error: {e}")
        engine = create_engine("sqlite:///f1_drivers.db")

    inspector = inspect(engine)

    if table_name in inspector.get_table_names():
        print(f"📂 La tabla '{table_name}' ya existe. Insertando nuevos registros...")
        df.to_sql(table_name, engine, if_exists="append", index=False)
    else:
        print(f"🆕 La tabla '{table_name}' no existe. Creándola...")
        df.to_sql(table_name, engine, if_exists="fail", index=False)

    print(f"✅ Proceso de carga completado en la tabla '{table_name}'.")
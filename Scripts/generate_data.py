# Importar librerías necesarias
import pandas as pd
import numpy as np
import os  # Para manejar rutas de directorios

# Crear la carpeta 'data' si no existe
if not os.path.exists("data"):
    os.makedirs("data")

# Generar datos sintéticos
np.random.seed(42)  # Para reproducibilidad
n_clientes = 1000  # Número de clientes en el dataset

data = {
    "ID_Cliente": np.arange(1, n_clientes + 1),
    "Edad": np.random.randint(18, 70, size=n_clientes),
    "Género": np.random.choice(["Masculino", "Femenino", "Otro"], size=n_clientes),
    "Fecha_Compra": pd.date_range(start="2020-01-01", periods=n_clientes, freq="D"),
    "Monto_Compra": np.round(np.random.uniform(10, 500, size=n_clientes), 2),
    "Producto_Categoría": np.random.choice(["Alimentos", "Electrónica", "Hogar", "Ropa"], size=n_clientes),
    "Método_Pago": np.random.choice(["Efectivo", "Tarjeta de Crédito", "Débito"], size=n_clientes),
    "Ubicación_Tienda": np.random.choice(["Centro", "Norte", "Sur"], size=n_clientes),
    "Promoción": np.random.choice(["Sí", "No"], size=n_clientes),
    "Frecuencia_Compra": np.random.choice(["Ocasional", "Regular", "Frecuente"], size=n_clientes),
}

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV dentro de la carpeta 'data'
df.to_csv("data/datos_retail.csv", index=False)

print("Dataset guardado como 'data/datos_retail.csv'")
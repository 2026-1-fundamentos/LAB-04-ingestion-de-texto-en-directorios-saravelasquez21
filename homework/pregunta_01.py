import os
import zipfile
import pandas as pd


def pregunta_01():
    """
    Procesa el archivo input.zip, extrae las frases de train y test,
    y genera los archivos train_dataset.csv y test_dataset.csv.
    """
    # Se corrige la ruta para apuntar a la carpeta 'files' según tu estructura
    zip_path = "files/input.zip"
    output_dir = "files/output"
    
    # Crear la carpeta de salida si no existe
    os.makedirs(output_dir, exist_ok=True)

    train_data = []
    test_data = []

    # Leer el archivo ZIP directamente de forma eficiente
    with zipfile.ZipFile(zip_path, 'r') as z:
        for file_info in z.infolist():
            # Saltar carpetas vacías o archivos ocultos del sistema
            if file_info.is_dir() or "__MACOSX" in file_info.filename or ".DS_Store" in file_info.filename:
                continue
            
            # Estructura esperada: input/train/neutral/0001.txt
            parts = file_info.filename.split('/')
            if len(parts) < 4:
                continue
                
            split_type = parts[1]  # 'train' o 'test'
            target = parts[2]      # 'neutral', 'positive' o 'negative'
            
            # Extraer y decodificar el texto de la frase
            with z.open(file_info) as f:
                phrase = f.read().decode('utf-8', errors='ignore').strip()
                
                if split_type == "train":
                    train_data.append({"phrase": phrase, "target": target})
                elif split_type == "test":
                    test_data.append({"phrase": phrase, "target": target})

    # Convertir las listas en DataFrames
    df_train = pd.DataFrame(train_data)
    df_test = pd.DataFrame(test_data)

    # Exportar a CSV en la ruta que exige el test
    df_train.to_csv(os.path.join(output_dir, "train_dataset.csv"), index=False)
    df_test.to_csv(os.path.join(output_dir, "test_dataset.csv"), index=False)


if __name__ == "__main__":
    pregunta_01()
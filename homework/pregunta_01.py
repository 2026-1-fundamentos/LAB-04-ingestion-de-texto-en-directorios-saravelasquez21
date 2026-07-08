# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import pandas as pd
import glob
import fileinput

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```

    """

    test_negative = []
    files = glob.glob("files/input/test/negative/*")
    with fileinput.input(files=files) as f:
        for line in f:
            test_negative.append((line))

    test_neutral = []
    files = glob.glob("files/input/test/neutral/*")
    with fileinput.input(files=files) as f:
        for line in f:
            test_neutral.append((line))
    
    test_positive = []
    files = glob.glob("files/input/test/positive/*")
    with fileinput.input(files=files) as f:
        for line in f:
            test_positive.append((line))
    
    train_negative = []
    files = glob.glob("files/input/train/negative/*")
    with fileinput.input(files=files) as f:
        for line in f:
            train_negative.append((line))

    train_neutral = []
    files = glob.glob("files/input/train/neutral/*")
    with fileinput.input(files=files) as f:
        for line in f:
            train_neutral.append((line))
    
    train_positive = []
    files = glob.glob("files/input/train/positive/*")
    with fileinput.input(files=files) as f:
        for line in f:
            train_positive.append((line))


    dic_test_negative = [{"phrase": line, "target": "negative"} for line in test_negative]
    dic_test_neutral = [{"phrase": line, "target": "neutral"} for line in test_neutral]
    dic_test_positive = [{"phrase": line, "target": "positive"} for line in test_positive]
    dic_train_negative = [{"phrase": line, "target": "negative"} for line in train_negative]
    dic_train_neutral = [{"phrase": line, "target": "neutral"} for line in train_neutral]
    dic_train_positive = [{"phrase": line, "target": "positive"} for line in train_positive]

    test_dataset = pd.DataFrame(dic_test_positive + dic_test_neutral + dic_test_negative, columns= ["phrase", "target"])
    train_dataset = pd.DataFrame(dic_train_positive + dic_train_neutral + dic_train_negative, columns= ["phrase", "target"])

    output_folder = "files/output"

    if os.path.exists(output_folder):
        for file in glob.glob(f"{output_folder}/*"):
            os.remove(file)
        os.rmdir(output_folder)
    os.makedirs(output_folder)

    test_path = os.path.join(output_folder, "test_dataset.csv")
    train_path = os.path.join(output_folder, "train_dataset.csv")

    test_dataset.to_csv(test_path, index=False)
    train_dataset.to_csv(train_path, index=False)
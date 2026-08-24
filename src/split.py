import pandas as pd
from pathlib import Path

def split(path : str, nb_period : int) -> tuple:
    """
    Fonction qui sépare le csv d'entrainement de la compétition en deux splits pour la phase 2
    """

    #Loading du csv
    df= pd.read_csv(path)

    #Split du dataset
    train_path, test_path= Path("data/train_split.csv"), Path("data/test_split.csv")

    df[df['period'] < nb_period].to_csv(train_path, index=False)
    df[df['period'] >= nb_period].to_csv(test_path, index=False)

    print("Split termine !")
    print("-"*30)
    print(f"Split train -> {train_path}")
    print(f"Split test -> {test_path}")

    return (train_path, test_path)
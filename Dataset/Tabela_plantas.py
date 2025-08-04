import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Plantas principais da NSK (baseado nos dados fornecidos)
plantas = [
    {"id_planta": 1, "nome": "NSK Brasil Ltda", "pais": "Brazil", "estado": "São Paulo", "cidade": "Suzano"},
    {"id_planta": 2, "nome": "NSK Argentina SRL", "pais": "Argentina", "estado": "Buenos Aires", "cidade": "Buenos Aires"},
    {"id_planta": 3, "nome": "NSK México", "pais": "Mexico", "estado": "Guanajuato", "cidade": "Silao"},
    {"id_planta": 4, "nome": "NSK USA - Ann Arbor", "pais": "USA", "estado": "Michigan", "cidade": "Ann Arbor"},
    {"id_planta": 5, "nome": "NSK Canada", "pais": "Canada", "estado": "Ontario", "cidade": "Brampton"},
    {"id_planta": 6, "nome": "NSK Japan HQ", "pais": "Japan", "estado": "Tokyo", "cidade": "Shinagawa-ku"},
    {"id_planta": 7, "nome": "NSK Germany", "pais": "Germany", "estado": "Ratingen", "cidade": "Ratingen"},
    {"id_planta": 8, "nome": "NSK China - Kunshan", "pais": "China", "estado": "Jiangsu", "cidade": "Kunshan"},
    {"id_planta": 9, "nome": "NSK India", "pais": "India", "estado": "Tamil Nadu", "cidade": "Chennai"},
    {"id_planta": 10, "nome": "NSK Thailand", "pais": "Thailand", "estado": "Chonburi", "cidade": "Amata City"}
]

df_plantas = pd.DataFrame(plantas)
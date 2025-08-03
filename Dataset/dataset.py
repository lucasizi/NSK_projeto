#Pandas para geração de datasets
import pandas as pd
#Numpy para geração de números aleatórios
import numpy as np
#Decimal para arredondamento de valores monetários
from decimal import Decimal, ROUND_HALF_UP, getcontext
#Datetime para manipulação de datas
from datetime import datetime, timedelta
#OS para manipulação de caminhos de arquivos
import os

# Configurar seed para reprodutibilidade, garantindo que os resultados sejam os mesmos em cada execução
np.random.seed(42)

# 1. Dimensão: Plantas
# Lista de plantas principais da NSK com seus detalhes
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

# 2. Dimensão: Produtos
# Gerar 50 produtos associados às plantas
categorias = ["Automotivo", "Industrial", "Aeroespacial", "Energia"]
produtos = []

for i in range(1, 51):
    categoria = np.random.choice(categorias, p=[0.6, 0.3, 0.05, 0.05])
    
    # Preços baseados na categoria
    if categoria == "Automotivo":
        preco = round(np.random.uniform(150, 300), 2)
    elif categoria == "Industrial":
        preco = round(np.random.uniform(300, 600), 2)
    else:
        preco = round(np.random.uniform(500, 1000), 2)
    
    produtos.append({
        "id_produto": i,
        "nome": f"Rolamento {categoria[:3]}-{i:03d}",
        "categoria": categoria,
        "preco_unitario": preco,
        "id_planta": np.random.choice(df_plantas['id_planta'])  # Associar a uma planta
    })

df_produtos = pd.DataFrame(produtos)

# 3. Dimensão: Clientes
# Gerar 100 clientes aleatórios
np.random.seed(42)
paises = ["Brazil", "Argentina", "Mexico", "USA", "Canada", "Germany", "Japan", "China", "India", "Chile", "Colombia"]
segmentos = ["OEM", "Revenda", "Serviço"]

clientes = []
for i in range(1, 101):
    pais = np.random.choice(paises)
    
    # Definir estados/cidades baseados no país
    if pais == "Brazil":
        estados = ["SP", "RJ", "MG", "RS", "PR", "SC"]
        cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Curitiba", "Florianópolis"]
    elif pais == "Argentina":
        estados = ["BA", "CT", "SF", "LP"]
        cidades = ["Buenos Aires", "Córdoba", "Rosario", "La Plata"]
    elif pais == "USA":
        estados = ["MI", "CA", "TX", "OH", "IL"]
        cidades = ["Detroit", "Los Angeles", "Houston", "Cleveland", "Chicago"]
    elif pais == "Mexico":
        estados = ["GUA", "JAL", "NL", "BC"]
        cidades = ["Silao", "Guadalajara", "Monterrey", "Tijuana"]
    else:
        estados = [f"ST{i}" for i in range(1,6)]
        cidades = [f"Cidade {pais} {i}" for i in range(1,6)]
    
    clientes.append({
        "id_cliente": i,
        "nome": f"Cliente {chr(65 + i % 26)}{i}",
        "segmento": np.random.choice(segmentos, p=[0.5, 0.3, 0.2]),
        "pais": pais,
        "estado": np.random.choice(estados),
        "cidade": np.random.choice(cidades)
    })

df_clientes = pd.DataFrame(clientes)

# 4. Fato: Vendas
# Gerar 1.000 vendas
datas = pd.date_range('2024-01-01', '2024-06-30')
vendas = []

for i in range(1, 1001):
    cliente = df_clientes.sample(1).iloc[0]
    produto = df_produtos.sample(1).iloc[0]
    quantidade = np.random.randint(10, 500)
    
    vendas.append({
        "id_venda": i,
        "data_venda": np.random.choice(datas),
        "id_cliente": cliente['id_cliente'],
        "id_produto": produto['id_produto'],
        "quantidade": quantidade
    })

df_vendas = pd.DataFrame(vendas)

# 5. Fato: Qualidade
# Gerar dados de qualidade por planta
qualidade = []
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 6, 30)
current_date = start_date

while current_date <= end_date:
    for id_planta in df_plantas['id_planta']:
        # Capacidade varia por planta
        capacidade = np.random.randint(5000, 20000)
        
        # Produção real com variação
        prod = int(capacidade * np.random.uniform(0.85, 1.10))
        
        # Defeitos baseados em dificuldade
        defeito = int(prod * np.random.uniform(0.01, 0.08))
        
        qualidade.append({
            "id_controle": len(qualidade) + 1,
            "id_planta": id_planta,
            "data": current_date.strftime("%Y-%m-%d"),
            "unidades_produzidas": prod,
            "unidades_defeituosas": defeito,
            "indice_qualidade": round((1 - (defeito / prod)) * 100, 2) if prod > 0 else 100
        })
    
    # Avançar para o próximo mês
    current_date = current_date.replace(day=1) + timedelta(days=32)
    current_date = current_date.replace(day=1)

df_qualidade = pd.DataFrame(qualidade)

# 7. Salvar datasets na pasta do projeto
output_dir = r"C:\Users\lucas\OneDrive\Documentos\GitHub\NSK-Projeto\Dataset"
os.makedirs(output_dir, exist_ok=True)

df_plantas.to_csv(os.path.join(output_dir, 'dim_plantas.csv'), index=False)
df_produtos.to_csv(os.path.join(output_dir, 'dim_produtos.csv'), index=False)
df_clientes.to_csv(os.path.join(output_dir, 'dim_clientes.csv'), index=False)
df_vendas.to_csv(os.path.join(output_dir, 'fato_vendas.csv'), index=False)
df_qualidade.to_csv(os.path.join(output_dir, 'fato_qualidade.csv'), index=False)

print("Datasets gerados com sucesso!")
print(f"Local: {output_dir}")
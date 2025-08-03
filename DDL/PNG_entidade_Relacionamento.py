from graphviz import Digraph
import os

# Configurar PATH do Graphviz
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'

# Criar diagrama
er = Digraph('Modelo_Dados_NSK', format='png',
             graph_attr={
                 'bgcolor': 'white',
                 'rankdir': 'TB',  # Top to Bottom
                 'splines': 'ortho',
                 'fontname': 'Arial',
                 'fontsize': '12',
                 'pad': '0.5'
             },
             node_attr={
                 'shape': 'plaintext',
                 'fontname': 'Arial'
             })

# Definir estilo das tabelas
table_style = '''<
<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="4">
    <TR>
        <TD COLSPAN="2" BGCOLOR="#1E90FF"><B>%s</B></TD>
    </TR>
%s
</TABLE>>'''

# Função para criar tabelas
def create_table(name, fields):
    field_rows = ""
    for i, field in enumerate(fields):
        color = "#F0F8FF" if i % 2 == 0 else "#E6F3FF"
        field_rows += f'    <TR><TD BGCOLOR="{color}" PORT="f{i}">{field[0]}</TD><TD BGCOLOR="{color}">{field[1]}</TD></TR>\n'
    return table_style % (name, field_rows)

# Tabelas e campos
tables = {
    'VENDAS': [
        ('id_venda', 'PK, INT'),
        ('data_venda', 'DATE'),
        ('id_cliente', 'FK, INT'),
        ('id_produto', 'FK, INT'),
        ('quantidade', 'INT'),
    ],
    'CLIENTES': [
        ('id_cliente', 'PK, INT'),
        ('nome', 'VARCHAR(100)'),
        ('segmento', 'VARCHAR(50)'),
        ('pais', 'VARCHAR(50)'),
        ('estado', 'VARCHAR(50)'),
        ('cidade', 'VARCHAR(50)')
    ],
    'PRODUTOS': [
        ('id_produto', 'PK, INT'),
        ('nome', 'VARCHAR(100)'),
        ('categoria', 'VARCHAR(50)'),
        ('preco_unitario', 'DECIMAL(10,2)'),
        ('id_planta', 'FK, INT')
    ],
    'PLANTAS': [
        ('id_planta', 'PK, INT'),
        ('nome', 'VARCHAR(100)'),
        ('pais', 'VARCHAR(50)'),
        ('estado', 'VARCHAR(50)'),
        ('cidade', 'VARCHAR(50)')
    ],
    'QUALIDADE': [
        ('id_controle', 'PK, INT'),
        ('id_planta', 'FK, INT'),
        ('data', 'DATE'),
        ('unidades_produzidas', 'INT'),
        ('unidades_defeituosas', 'INT'),
        ('indice_qualidade', 'DECIMAL(5,2)')
    ]
}

# Adicionar tabelas ao diagrama
for table_name, fields in tables.items():
    er.node(table_name, create_table(table_name, fields))

# Minha definição de relacionamentos
relacionamentos = [
    ('CLIENTES', 'VENDAS', '1', 'N', 'realiza'),                 # Um cliente realiza muitas vendas
    ('VENDAS', 'PRODUTOS', 'N', '1', 'refere_a'),                # Cada venda refere-se a um único produto
    ('PRODUTOS', 'PLANTAS', 'N', '1', 'fabricado_em'),           # Um produto é fabricado em uma planta
    ('PLANTAS', 'QUALIDADE', '1', 'N', 'tem_qualidade_registrada')  # Uma planta tem vários registros de qualidade
]


# Adicionando relacionamentos
for src, dst, card_src, card_dst, label in relacionamentos:
    er.edge(src, dst, 
            label=f' {label}\n{card_src}:{card_dst}',
            fontsize='8',
            fontname='Arial',
            headlabel=card_dst,
            taillabel=card_src,
            labelfloat='false',
            arrowhead='none',
            arrowtail='none')

# Título
er.attr(label='<<B>Modelo de Dados - Sistema de Vendas e Produção NSK</B><BR/><FONT POINT-SIZE="10">Projeto para Processo Seletivo</FONT>>',
        labelloc='t',
        fontsize='16')

# Renderizar e salvar
output_path = r'C:\Users\lucas\OneDrive\Documentos\GitHub\NSK-Projeto\Dataset\modelo_dados_nsk'
er.render(filename=output_path, cleanup=True, view=True)

print(f"Diagrama de modelo de dados salvo em: {output_path}.png")
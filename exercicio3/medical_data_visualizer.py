import pandas as pd           # Importa a biblioteca pandas para manipulação de dados
import seaborn as sns         # Importa seaborn para visualização de dados
import matplotlib.pyplot as plt  # Importa matplotlib para gráficos
import numpy as np            # Importa numpy para operações numéricas

# 1
df = pd.read_csv('exercicio3/medical_examination.csv')  # Lê o arquivo CSV e armazena em um DataFrame

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)  # Calcula IMC e define se está acima do peso ou não

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)  # Normaliza colesterol: 0 para normal, 1 para acima do normal
df['gluc'] = (df['gluc'] > 1).astype(int)                # Normaliza glicose: 0 para normal, 1 para acima do normal

# 4
def draw_cat_plot():  # Função para criar gráfico categórico
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])  # Transforma dados para formato longo

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')  # Agrupa e conta ocorrências de cada categoria

    # 7
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')  # Cria gráfico de barras categórico

    # 8
    fig = fig.figure  # Obtém o objeto figura do gráfico

    # 9
    fig.savefig('catplot.png')  # Salva o gráfico como imagem
    return fig                 

# 10
def draw_heat_map():  # Função para criar mapa de calor de correlação
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &  # Filtra dados onde pressão diastólica <= sistólica
        (df['height'] >= df['height'].quantile(0.025)) &  # Remove alturas abaixo do percentil 2.5%
        (df['height'] <= df['height'].quantile(0.975)) &  # Remove alturas acima do percentil 97.5%
        (df['weight'] >= df['weight'].quantile(0.025)) &  # Remove pesos abaixo do percentil 2.5%
        (df['weight'] <= df['weight'].quantile(0.975))    # Remove pesos acima do percentil 97.5%
    ]

    # 12
    corr = df_heat.corr()  # Calcula matriz de correlação dos dados filtrados

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))  # Cria máscara para mostrar apenas metade superior da matriz

    # 14
    fig, ax = plt.subplots(figsize=(12, 9))  # Cria figura e eixos para o gráfico

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0,
                square=True, linewidths=0.5, cbar_kws={"shrink": .5}, ax=ax)  # Plota o mapa de calor com anotações

    # 16
    fig.savefig('heatmap.png')  # Salva o mapa de calor como imagem
    return fig                 # Retorna o objeto figura
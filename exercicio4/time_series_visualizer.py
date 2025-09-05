import matplotlib.pyplot as plt         # Importa biblioteca para criar gráficos
import pandas as pd                     # Importa biblioteca para manipulação de dados
import seaborn as sns                   # Importa biblioteca para visualização estatística
from pandas.plotting import register_matplotlib_converters  # Importa função para compatibilidade de datas
register_matplotlib_converters()        # Registra conversores de datas para matplotlib

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('exercicio4/fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')  # Lê arquivo CSV, converte coluna 'date' para datas e define como índice

# Clean data
# Filter out days when page views were in the top 2.5% or bottom 2.5% of the dataset
df = df[(df['value'] >= df['value'].quantile(0.025)) &    # Filtra valores acima do percentil 2.5%
        (df['value'] <= df['value'].quantile(0.975))]     # Filtra valores abaixo do percentil 97.5%

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))               # Cria figura e eixo para o gráfico de linha
    ax.plot(df.index, df['value'], color='red', linewidth=1)  # Plota gráfico de linha dos valores ao longo do tempo
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')  # Define título do gráfico
    ax.set_xlabel('Date')                                 # Define rótulo do eixo X
    ax.set_ylabel('Page Views')                           # Define rótulo do eixo Y

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')                          # Salva gráfico como imagem
    return fig                                            # Retorna figura criada

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()                                    # Cria cópia do DataFrame original
    df_bar['year'] = df_bar.index.year                    # Adiciona coluna 'year' com ano extraído do índice
    df_bar['month'] = df_bar.index.month                  # Adiciona coluna 'month' com mês extraído do índice

    # Group by year and month, then calculate mean
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()  # Agrupa por ano e mês e calcula média dos valores

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))               # Cria figura e eixo para o gráfico de barras
    df_bar.plot(kind='bar', ax=ax)                        # Plota gráfico de barras com médias mensais por ano
    ax.set_xlabel('Years')                                # Define rótulo do eixo X
    ax.set_ylabel('Average Page Views')                   # Define rótulo do eixo Y
    ax.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])  # Define legenda dos meses

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')                           # Salva gráfico como imagem
    return fig                                            # Retorna figura criada

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()                                    # Cria cópia do DataFrame original
    df_box.reset_index(inplace=True)                      # Reseta índice para transformar 'date' em coluna
    df_box['year'] = [d.year for d in df_box.date]        # Adiciona coluna 'year' com ano extraído da data
    df_box['month'] = [d.strftime('%b') for d in df_box.date]  # Adiciona coluna 'month' com mês abreviado extraído da data

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6)) # Cria figura com dois eixos lado a lado

    # Year-wise box plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1) # Plota boxplot dos valores por ano
    ax1.set_title('Year-wise Box Plot (Trend)')           # Define título do boxplot anual
    ax1.set_xlabel('Year')                                # Define rótulo do eixo X
    ax1.set_ylabel('Page Views')                          # Define rótulo do eixo Y

    # Month-wise box plot (Seasonality)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']  # Define ordem dos meses
    sns.boxplot(x='month', y='value', data=df_box, order=month_order, ax=ax2)  # Plota boxplot dos valores por mês
    ax2.set_title('Month-wise Box Plot (Seasonality)')     # Define título do boxplot mensal
    ax2.set_xlabel('Month')                                # Define rótulo do eixo X
    ax2.set_ylabel('Page Views')                           # Define rótulo do eixo Y

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')                            # Salva gráfico como imagem
    return fig                                             # Retorna figura criada
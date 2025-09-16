# Exercício 5 - FreeCodeCamp - Python

## Previsor do Nível do Mar

Você analisará um conjunto de dados da mudança média
global do nível do mar desde 1880. Você usará os dados para prever a mudança do nível do mar até o ano 2050.

Use os dados para concluir as seguintes tarefas:

- Use o Pandas para importar os dados de epa-sea-level.csv.

- Use matplotlib para criar um gráfico de dispersão usando a Year coluna como eixo x e a CSIRO Adjusted Sea Level coluna como eixo y.

- Use a linregress função de scipy.stats para obter a inclinação e a interceptação em y da reta de melhor ajuste. Trace a reta de melhor ajuste sobre o topo do gráfico de dispersão. Faça a reta passar pelo ano de 2050 para prever a elevação do nível do mar em 2050.

- Trace uma nova reta de melhor ajuste usando apenas os dados do ano 2000 até o ano mais recente no conjunto de dados. Faça a reta também passar pelo ano 2050 para prever a elevação do nível do mar em 2050 se a taxa de elevação continuar como tem acontecido desde o ano 2000.

- O rótulo x deve ser Year, o rótulo y deve ser Sea Level (inches) e o título deve ser Rise in Sea Level.

- O modelo também inclui comandos para salvar e retornar a imagem.

### Desenvolvimento
---
Escreva seu código em sea_level_predictor.py. Para desenvolvimento, você pode usar main.py para testar seu código.

### Teste
---
Os testes unitários para este projeto estão em test_module.py. Importamos os testes de test_module.py para main.py para sua conveniência.
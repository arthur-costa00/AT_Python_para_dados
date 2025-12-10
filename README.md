# AT_Python_para_dados

Este projeto faz o scraping da lista IMDb Top 250, salva tudo em um banco SQLite e depois realiza algumas analises simples usando Pandas.

O que o projeto faz:
- Acessa a página IMDb Top 250
- Extrai título, ano e nota de cada filme
- Armazena tudo em imdb.db
- Lê o banco e transforma em DataFrame
- Mostra análises como:
- primeiros registros
- top films por nota
- média das notas
- Tudo configurável pelo arquivo config.json

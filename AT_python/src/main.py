import json
from scraping import buscar_html, extrair_filmes
from database import criar_tabelas, salvar_filmes, consultar_filmes
from analysis import criar_dataframe, top_n, media_notas

with open("config.json", "r") as f:
    config = json.load(f)

url = config["url_imdb"]
limite = config["n_filmes"]

html = buscar_html(url)
filmes = extrair_filmes(html, limite)

criar_tabelas()
salvar_filmes(filmes)

dados = consultar_filmes()
df = criar_dataframe([{"titulo": d[0], "ano": d[1], "nota": d[2]} for d in dados])

print(df.head())
print(top_n(df, 5))
print(media_notas(df))

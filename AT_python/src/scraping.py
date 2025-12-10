import requests
from bs4 import BeautifulSoup

def buscar_html(url):
    resposta = requests.get(url)
    return resposta.text

def extrair_filmes(html, limite):
    soup = BeautifulSoup(html, "html.parser")
    itens = soup.select("li.ipc-metadata-list-summary-item")[:limite]
    filmes = []
    for item in itens:
        titulo = item.select_one("h3").text.strip()
        ano = item.select_one(".cli-title-metadata-item").text.strip()
        nota = item.select_one("span.ipc-rating-star--rating").text.strip()
        filmes.append({
            "titulo": titulo,
            "ano": ano,
            "nota": float(nota)
        })
    return filmes

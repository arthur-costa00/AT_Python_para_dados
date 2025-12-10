import sqlite3

def conectar():
    return sqlite3.connect("data/imdb.db")

def criar_tabelas():
    conn = conectar()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            ano TEXT,
            nota REAL
        )
    """)
    conn.commit()
    conn.close()

def salvar_filmes(lista):
    conn = conectar()
    c = conn.cursor()
    for f in lista:
        c.execute("""
            INSERT INTO filmes (titulo, ano, nota) 
            VALUES (?, ?, ?)
        """, (f["titulo"], f["ano"], f["nota"]))
    conn.commit()
    conn.close()

def consultar_filmes():
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT titulo, ano, nota FROM filmes")
    dados = c.fetchall()
    conn.close()
    return dados

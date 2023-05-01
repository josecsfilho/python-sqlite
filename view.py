import sqlite3 as lite


# CRUD


# Create = Inserir / criar
# Ready = acessar / mostrar
# Update = atualizar
# Delete = Deletar /apagar


# criando conexão
con = lite.connect('dados.db')


lista = ['Joao Futi Muanda', 'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de uma consultar pessoalmente']

# Inserir informações
with con:
    cur = con.cursor()
    query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
    cur.execute(query,lista)


# Acessar informações
with con:
    cur = con.cursor()
    query = "SELECT * FROM formulario"  
    cur.execute(query)
    informacao = cur.fetchall()
    print(informacao)
    

lista = ['joao', 1]
# Atualizar informações
with con:
    cur = con.cursor()
    query = "UPDATE formulario SET nome=? WHERE id=?"
    cur.execute(query,lista)



lista = [1]
# Deletar informações
with con:
    cur = con.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cur.execute(query,lista)



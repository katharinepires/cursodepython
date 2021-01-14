#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector


# In[2]:


conexao = mysql.connector.connect(user = "root", password = "#2021meuano", 
                                  host = "127.0.0.1", database = "agenda")
conexao.close()


# Outra maneira de realizar a conexão é:

# In[3]:


from mysql.connector import connection


# In[4]:


conexao = connection.MySQLConnection(user = "root", password = "#2021meuano", 
                                  host = "127.0.0.1", database = "agenda")
conexao.close()


# Executando o MySQL:

# In[5]:


co = connection.MySQLConnection(user = "root", password = "#2021meuano", 
                                  host = "127.0.0.1", database = "agenda")
cursor = co.cursor()


# In[6]:


inserir_cont = ("insert into contatos (nome, telefone, email) values ('João Python', '(13)5599-9963', 'python2_curso@gmail.com')")
cursor.execute(inserir_cont)
#gravar de maneira permanente a informação:
co.commit()
cursor.close()
co.close()


# Usando Tupla para inserir informações:

# In[7]:


conexao = mysql.connector.connect(user = "root", password = "#2021meuano", 
                                  host = "127.0.0.1", database = "agenda")
cursor = conexao.cursor()

inserir_cont = ("insert into contatos (nome, email) values (%s, %s)")
#criando a tupla:
contato = ('Maria Python', 'python2_maria@yahoo.com')
cursor.execute(inserir_cont, contato)
conexao.commit()
cursor.close()
conexao.close()


# Usando dicionário para inserir os dados:

# In[8]:


con = mysql.connector.connect(user = "root", password = "#2021meuano", 
                                  host = "127.0.0.1", database = "agenda")
cursor = con.cursor()

inserir_cont = ("insert into contatos (nome, email) values (%(nome)s, %(email)s)")
#criando o dicionário:
contato = {'nome': 'Paulinho Matador de Porco',
           'email':'matador_porco2@gmail.com'}
cursor.execute(inserir_cont, contato)
con.commit()
cursor.close()
con.close()


# Usando o `update` para alterar:

# In[9]:


c = mysql.connector.connect(user = "root", password = "#2021meuano", 
                                  host = "127.0.0.1", database = "agenda")
cursor = c.cursor()
atualizar = ("update contatos set nome = %s, telefone = %s, email = %s where id = 10")
contato = ('Python', '(56)87954036','matador_porco3@gmail.com')
cursor.execute(atualizar, contato)
c.commit()
cursor.close()
c.close()


# Deletando:

# In[10]:


conexao = mysql.connector.connect(user = "root", password = "#2021meuano", 
                                  host = "127.0.0.1", database = "agenda")
cursor = conexao.cursor()
remover = ("delete from contatos where id = 9")
cursor.execute(remover)
conexao.commit()
cursor.close()
conexao.close()


# Consultando dados:

# In[11]:


print(dir(mysql))


# In[12]:


conexao = mysql.connector.connect(user = "root", password = "#2021meuano", 
                                  host = "127.0.0.1", database = "agenda")
cursor = conexao.cursor()

consulta = ("select nome, telefone, email from contatos where nome like 'E%'")
cursor.execute(consulta)

for (nome, telefone, email) in cursor:
    print(f"Nome: {nome}, contatos: {telefone} e {email}")

cursor.close()
conexao.close()


# In[13]:


conexao = mysql.connector.connect(user = "root", password = "#2021meuano", 
                                  host = "127.0.0.1", database = "agenda")
cursor = conexao.cursor()

consulta = ("select nome, telefone, email from contatos")
cursor.execute(consulta)

for (nome, telefone, email) in cursor:
    print(f"Nome: {nome}, contatos: {telefone} e {email}")

cursor.close()
conexao.close()


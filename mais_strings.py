#!/usr/bin/env python
# coding: utf-8

# # Mais sobre strings
# 

# ### Conversão para maiúsculas e minúsculas:
# Pode-se usar `startswith` e `endswith` para saber qual caractere a string começa e termina. E para converter de maisúcula para minúscula, usamos os comandos `.upper()` e `.lower()` 

# In[1]:


nome = "Katharine Pires"
nome.startswith("Kath")


# In[2]:


nome.startswith("rine")


# In[3]:


nome.endswith("res")


# In[4]:


nome.endswith("rine Pi")


# In[5]:


a = "Cientista de Dados"
"Roi" in a


# In[6]:


"dados" in a


# In[7]:


"dos" in a


# In[8]:


"Cientista" not in a


# In[9]:


"De" not in a


# In[10]:


a.lower()


# In[11]:


a.upper()


# In[12]:


a.upper().startswith('Cien')


# In[13]:


a.lower().endswith("dos")


# ### Contando e pesquisando elementos de uma string:
# Usando o `.count()` podemos contar quantos elementos tem a string.

# In[14]:


texto = "Eu quero muito um emprego. Tendo um emprego terei meu dinheiro. Quero muito dinheiro e um emprego"
texto.count("emprego")


# In[15]:


texto.count("dinheiro")


# In[16]:


texto.count("eu")


# In[17]:


texto.count("endo")


# Usando o arquivo da aula para contar a ocorrência de uma palavra:

# In[18]:


contador = 0
palavra = "volvo"
arquivo_nome = "063 discos-estoque.txt" 
with open(arquivo_nome, "r") as arquivo:
    for linha in arquivo:
        contador = contador + linha.upper().count(palavra.upper())


# Com o `with open` será lido (por isso o `"r")` o arquivo. Com o `for`, será pecorrido o arquivo e cada linha ele irá armazenar o contador, pegando cada ocorrência da palavra em cada linha. 

# In[19]:


print("Palavra pesquisada:" + palavra.upper())
print("Arquivo pesquisado:" + arquivo_nome)
print("Total de palavras encontradas:" + str(contador))


# In[20]:


contador = 0
palavra = input("Informe a palavra que busca encontrar: ")
arquivo_nome = input("Informe o nome do arquivo; ") 
with open(arquivo_nome, "r") as arquivo:
    for linha in arquivo:
        contador = contador + linha.upper().count(palavra.upper())
        

print("Palavra pesquisada:" + palavra.upper())
print("Arquivo pesquisado:" + arquivo_nome)
print("Total de palavras encontradas:" + str(contador))


# Com o `.find()` você pode identificar a posição da primeira ocorrência da string. Se não encontrar, o Python retorna `-1`.

# In[21]:


texto.find("emprego")


# In[22]:


texto.find("Roi")


# Com o `.rfind()` você faz bsucas da direita para esquerda:

# In[23]:


texto.rfind("emprego")


# In[24]:


texto.find("emprego", 20,45) #delimita inicio e fim


# In[25]:


texto.rfind("emprego", 15,25)


# ### Posicionamento de Strings:
# Usando o `.center()` você centraliza a sua string, ela preenche com espaços.

# In[26]:


texto1 = "Olá, como você está?"
texto2 = "Ah! Eu estou muito bem e você?"
texto3 = "Isso é ótimo. Tem alguma novidade? Pois eu tenho um bocado!"
texto4 = texto1.center(100)
texto5 = texto2.center(100)
texto6 = texto3.center(100)

print(texto4)
print(texto5)
print(texto6)


# In[27]:


print(texto4 + "\n" + texto5 + "\n" + texto6)


# In[28]:


texto4 = texto1.center(90, "-")
texto5 = texto2.center(90, "-")
texto6 = texto3.center(90, "-")
print(texto4 + "\n" + texto5 + "\n" + texto6)


# Os métodos `.rjust()` alinha o texto a direite e o `.ljust()` alinha para a esquerda:

# In[29]:


texto7 = "Então me conta loogoo!!"
texto4 = texto1.ljust(10)
texto5 = texto2.rjust(70)
texto6 = texto3.ljust(10)
texto8 = texto7.rjust(70)
print(texto4 + "\n" + texto5 + "\n" + texto6 + "\n" + texto8)


# ### Separação, Remoção de espaço em branco, substituição de strings:
# Separando usando o `.split()`:

# In[30]:


text = "O Mestre na arte da vida faz pouca distinção entre o seu trabalho e o seu lazer, entre a sua mente e o seu corpo, entre a sua educação e a sua recreação, entre o seu amor e a sua religião. Ele dificilmente sabe distinguir um corpo do outro."
text.split(',')


# Sepando a partir da nova linha `\n`, usando o `.splitlines()`:

# In[31]:


text2 = "O Mestre na arte da vida faz pouca distinção entre o seu trabalho e o seu lazer, \nentre a sua mente e o seu corpo, entre a sua educação e a sua recreação, \nentre o seu amor e a sua religião. Ele dificilmente sabe distinguir um corpo do outro."
text2.splitlines()


# Usando `.replace()` para substituição:

# In[32]:


text3 = "Eu quero muito dinheiro. Com dinheiro, serei mais independente. Dinheiro e dinheiro!!"
text3_ = text3.replace("dinheiro", "emprego")
print(text3_)


# In[33]:


text3_ = text3.replace("dinheiro", "emprego", 2) #substitui as duas primeiras ocorrências
print(text3_)


# In[34]:


text3_ = text3.replace("", "+")
print(text3_)


# In[35]:


text3_ = text3.replace("dinheiro", "")
print(text3_)


# Para remover espaços em branco, tem três opções:
# - `strip` => que remove inicio e fim da string
# - `lstrip` => remove inicio da string
# - `rstrip` => remove o fim da string

# In[36]:


a = "     Aqui é um exemplo de espaços no início e fim.     "
b = "     Aqui já um exemplo de espaço no início."
c = "Por fim, um exemplo de espaço no fim.     "

a_ = a.strip()
b_ = b.lstrip()
c_ = c.rstrip()

print("*" + a + "*")
print("*" + b + "*")
print("*" + c + "*")


# In[37]:


print("*" + a_ + "*")
print("*" + b_ + "*")
print("*" + c_ + "*")


# In[38]:


a = "exemplo de nada aqui"
a_ = a.strip("exemplo")
print(a)
print(a_)


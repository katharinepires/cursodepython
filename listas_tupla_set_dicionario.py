#!/usr/bin/env python
# coding: utf-8

# # Listas

# In[1]:


lista = [14, 6, 99]
print(lista[1])


# In[2]:


notas = [8.5, 5.5, 6.8, 10.0]
media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4
print("O aluno ficou com média:",media)


# In[3]:


bancos = ["C6", "Inter", "Bradesco"]
print("Meus bancos são os",bancos)


# In[4]:


bancos[2] = "Easyvest"
print("Meus novos bancos são:",bancos)


# In[5]:


bancos[-1]


# In[6]:


num = [10,15,20]
soma = num + [5,10,15]
print(soma)


# In[7]:


num += [5,10,15]
print(num)


# In[8]:


bancos.append("Nubank")
print(bancos)


# Escolhendo a posição que será inserido:

# In[9]:


bancos.insert(2, "Original")
print(bancos)


# Removendo:

# In[10]:


bancos.remove("Nubank")
print(bancos)


# In[11]:


bancos.sort()
print(bancos)


# Revertendo a lista:

# In[12]:


bancos.reverse()
print(bancos)


# Contar elementos da lista:

# In[13]:


lista = [10,25,10,5,9,1,5,3,10,10,4,9,3,20]
nomes = ["Katharine", "Pires", "Caravlho", "Pires", "Pires"]
lista.count(10), nomes.count("Pires")


# Excluir último elemento da lista:

# In[14]:


nomes.pop()
print(nomes)


# In[15]:


lista.pop() #número que foi eliminado


# In[16]:


n = lista.pop()
print("'n' vai receber o valor que foi eliminado, nesse caso o:",n)


# Usando o `del` para deletar elementos nas listas:

# In[17]:


print(lista)


# In[18]:


del lista[0]
print(lista)


# In[19]:


del lista[2:5]
print(lista)


# Removendo todos os elementos da lista:

# In[20]:


nomes.clear()
print(nomes)


# In[21]:


lista = []
print(lista)


# ## Mais detalhes sobre listas:

# In[22]:


l = [14,6,99, ["Katharine", "G", "C","Pires"]]
print(l)


# In[23]:


nome = l[3]
print(nome)


# In[24]:


soma = l[0] + l[1] + l[2]
print(soma)


# In[25]:


del l[3]
mistura = [l, nome]
print(mistura)


# In[26]:


mistura[0]


# In[27]:


mistura[1]


# In[28]:


len(mistura)


# In[29]:


len(nome)


# Para achar o index:

# In[30]:


nome.index("Pires")


# ### Verificando a existência de item na lista

# In[31]:


familia = ["Katharine", "Vera", "Claudemir"]
membro = input("Qual é o nome? ")
if membro in familia:
    print("Ah, sim!",membro,"é da minha família.")
else:
    print("Puts... Não!",membro,"não é da minha família.")


# In[32]:


familia = ["KATHARINE", "VERA", "CLAUDEMIR"]
membro = input("Qual é o nome? ")
if membro.upper() in familia:
    print("Ah, sim!",membro,"é da minha família.")
else:
    print("Puts... Não!",membro,"não é da minha família.")


# ### Elementos fornecidos pelo usuário

# In[33]:


k = []
while True:
    num = int(input("Informe um número (0 para): "))
    if num == 0:
        break
    k.append(num)
        


# In[34]:


print(k)


# ### Separando pares e ímpares

# In[35]:


pares = []
impares = []
total_par = 0
total_impar = 0

while True:
    numero = int(input("Informe o número, sendo 0 para saída: "))
    if numero == 0:
        break
    elif numero%2 == 0:
        pares.append(numero)
        total_par = total_par + 1
    else:
        impares.append(numero)
        total_impar = total_impar + 1
        

impares.sort()
pares.sort()
print(f"Tivemos um total de {total_par} números pares, sendo eles: {pares}")
print(f"Tivemos um total de {total_impar} números ímpares, sendo eles: {impares}")


# `enumerate`:

# In[36]:


amigas = ["Evelin", "Lisandra", "Estefane"]
e_amigas = list(enumerate(amigas))
print(e_amigas)


# In[37]:


e_amigas = list(enumerate(amigas, 5)) #start=5
print(e_amigas)


# In[38]:


mercado = ["Arroz","Feijão","Macarrão","Açucar","Sal"]
for indice, produto in enumerate(mercado, 1):
    print(indice, produto)


# In[39]:


mercado.sort() #listas diferentes
for indice, produto in enumerate(mercado):
    print(indice + 1, produto)


# ### Copiando listas

# In[40]:


lista = [1,2,3,4,5]
nova_lista = lista
print(lista, nova_lista)


# In[41]:


lista += [6]
print(lista, nova_lista)


# In[42]:


lista += [7]
print(lista, nova_lista)


# Copiando a lista, qualquer alteração feita na lista original, será também passada para a copiada. Para a lista ser independente, é necessário clonar:

# ### Clonando listas

# In[43]:


lista = [6,7,8,9,10]
clone_lista = lista[:]
print(lista, clone_lista)


# In[44]:


lista += [11]
print(lista, clone_lista)


# In[45]:


clone_lista += [12,15]
print(lista, clone_lista)


# # Tupla:
# Diferente das listas, `tuplas`não são mutáveis. Então não podemos alterar: adicionar ou deletar, coisas do tipo. São criadas com `()`, mas nsão é obrigatório o seu uso:

# In[46]:


tupla1 = ("a","b","c")
tupla2 = "a","b","c"


# In[47]:


tupla_v = () #tupla vazia
tupla_um = (1) #python entende como um inteiro e não tupla
tupla_um = 1, #tupla com um único elemento (ou tupla_um = (1,))


# In[48]:


paises = "Brasil", "Argentina","Uruguai","Chile"
pais = paises[0]
print(paises)
print(pais)


# In[49]:


paises_ = paises[0:2]
print(paises_)


# In[50]:


for pais_ in paises:
    print(pais_)


# Converter lista em tupla:

# In[51]:


carros = ["Yaris", "Captur", "Renegade", "HB20"]
tupla_carros = tuple(carros)
print(tupla_carros)


# In[52]:


nomes_t = tuple(nome)
print(nomes_t)


# Converter tupla em lista:

# In[53]:


lista_carros = list(tupla_carros)
print(lista_carros)


# In[54]:


carro_1, carro_2, carro_3, carro_4 = tupla_carros
print(f"Carro 1: {carro_1}")
print(f"Carro 2: {carro_4}")
print(f"Carro 3: {carro_2}")
print(f"Carro 4: {carro_3}")


# In[55]:


tupla_carro = "HB20", "Yaris","Novo Clio",                "Onix", "Gol"
# \ indica que a linha continua
carro1, *carros = tupla_carro
print(f"O carro número 1 é: {carro1}")
print(f"As outras opções são: {carros}")    


# In[56]:


*carros, carro0, carro00 = tupla_carro
print(f"Os carros que minha mãe gostaria: {carros}")
print(f"Os carros que minha mãe nem quer olhar: {carro0} e {carro00}")


# # Set
# É mutável e não ordenada, suporta operações matemáticas como diferença, interseção e união. Naõ possui elementos duplicados. Se cria usando o `{}`. Conjunto vazio se usa o `.set()`, pous só as chaveis o python entende como dicionário.

# In[57]:


conjunto_numeros = {10,15,16,20,25,26}
conjunto_vazio = set()
print(conjunto_numeros)
print(conjunto_vazio)


# Converter lista em set:

# In[58]:


conjunto_nome = set(nome)
print(conjunto_nome)


# União:

# In[59]:


uniao = conjunto_nome.union(conjunto_numeros)
print("A união dos dois conjuntos é:",uniao)


# Diferença:

# In[60]:


conjunto_1 = {0,2,4,6,8,10}
conjunto_2 = {0,1,2,3,4,5}
diferenca = conjunto_1.difference(conjunto_2)
intersecao = conjunto_1.intersection(conjunto_2)
print(f"A diferenca entre os conjuntos é: {diferenca}")
print(f"A interseção entre os conjuntos é: {intersecao}")


# Se um conjunto está em outro conjunto:

# In[61]:


conj_1 = {"Katharine", "Góes", "Carvalho", "Pires"}
conj_2 = {"Vera", "Lúcia", "Góes", "Carvalho"}

if conj_1.issuperset(conj_2):
    print(f"O conjunto {conj_2} está incluso no conjunto {conj_1}")
else:
    print(f"O conjunto {conj_2} não está incluso no conjunto {conj_1}")


# In[62]:


conj_1 = {14,6,99}
conj_2 = {14,99}

if conj_2.issubset(conj_1):
    print(f"O conjunto {conj_2} está incluso no conjunto {conj_1}")
else:
    print(f"O conjunto {conj_2} não está incluso no conjunto {conj_1}")
    
# o issuperset verifica os conjuntos


# Se o conjunto não possui elementos comuns de outro conjunto:

# In[63]:


conj_1 = {"Góes", "Carvalho", "Pires"}
conj_2 = {"Lúcia", "Góes", "Carvalho"}

if conj_1.isdisjoint(conj_2):
    print(f"O conjunto {conj_2} não possui elementos comuns ao conjunto {conj_1}")
else:
    print(f"O conjunto {conj_2} possui elementos comuns ao conjunto {conj_1}")


# # Dicionários

# In[64]:


dicionario = {"Nome": "Katharine Pires",
             "Idade": 21,
             "Ocupação": "Cientista de Dados"}

print(dicionario)


# In[67]:


print(f"A aluna é uma {dicionario['Ocupação']}")
print(f"A aluna tem {dicionario['Idade']} anos")


# In[68]:


dicionario['Curso'] = "Ciências Econômicas"
print(dicionario)


# In[69]:


del dicionario["Curso"]
print(dicionario)


# Se usar `dicionario.clear()` apaga todos os elementos do dicionário, ele fica vazio. Para apagar também o dicionário, se usa o `del dicionario`.

# In[70]:


print(f"Itens do dicionário: {dicionario.items()}")
print(f"Chaves do dicionário: {dicionario.keys()}")
print(f"Valores do dicionário: {dicionario.values()}")


# Verificando se chave existe:

# In[71]:


"Idade" in dicionario


# In[72]:


"Julia" in dicionario


# In[73]:


loja = {"Notebook": 1550.55,
       "Celular": 500.55,
       "Mousepad": 50.0,
       "Monitor": 1458.48}

while True:
    compra = input("Informe o produto deseajdo: ")
    if compra == "cancelar":
        break
    if compra in loja:
        print("Temos",compra,"em estoque e custa:",loja[compra])
    else:
        print("Não temos",compra,"no estoque ou não vendemos")
              
    


# In[74]:


copia = loja.copy()
print(loja, copia)


# In[75]:


loja.update(dicionario)
print(loja)


# #### Desafios:
# 1º - Set

# In[76]:


palavras = []

while True:
    diga = input("Informe palavras: ")
    if diga == "0":
        break
    else:
        palavras.append(diga)
    
for conj in palavras:
    conj = set(palavras)
    
print("As palavras foram as:",conj)


# 2º - Estoque de produtos

# In[77]:


estoque = {"1": ["Teclado", 300, 166.71],
          "2": ["Mouse", 125, 80.57],
          "3": ["Processador", 25, 875.64],
          "4": ["Cooler", 70, 35.14]}

print("O estoque atual é: ")
print("Código | Produto | Quantidade | Valor")

for codigo in estoque:
    print(codigo,"|",estoque[codigo][0],"|",estoque[codigo][1],"|",estoque[codigo][2])

while True:
    acao = input("Informe a opção desejada: \n"
                "(1) Registrar entrada de produro \n"
                "(2) Registrar saída de produto \n"
                "(3) Sair do sistema \n"
                "Selecionado: ")
    if acao == "3":
        break
    else:
        codigo = input("Informe o código do produto: ")
        if acao == "1":
            qtd = int(input("Informe a quantidade de entrada: "))
            estoque[codigo][1] += qtd
        elif acao == "2":
            qtd = int(input("Informe a quantidade de saída: "))
            if qtd <= estoque[codigo][1]:
                 estoque[codigo][1] -= qtd
            else:
                print("Não há quantidade suficiente de estoque")       


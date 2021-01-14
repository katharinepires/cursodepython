#!/usr/bin/env python
# coding: utf-8

# # Funções

# In[1]:


def soma():
    num1 = 10
    num2 = 15
    soma = num1 + num2
    print(f"O resultado final é {soma}")


# In[2]:


soma()


# In[3]:


def media(ava1,ava2,ava3):
    media = (ava1 + ava2 + ava3) / 3
    print(f"O resultado final do aluno é: {media:.2f}")


# In[4]:


media(9.5,8.4,2.7)


# In[5]:


def juros(pv,i):
    fv = ((i/100) + 1)*pv 
    return fv


# In[6]:


print(f"O valor futuro a ser pago com juros é: {juros(1000,20)}")


# In[7]:


def juros_comp(i,n,pv):
    fv = pv*((i/100) + 1)**n
    return fv

print(f"O valor futuro com juros será: R${juros_comp(15,3,5585):,.2f}")


# In[8]:


def maior_valor(valores):
    return max(valores)

def pegar_numeros():
    lista_num = []
    
    while True:
        num = int(input("Informe um número: "))
        if num == 0:
            break
        else:
            lista_num.append(num)
    
    return maior_valor(lista_num)
            
print(f"O maior valor informado foi: {pegar_numeros()}")


# In[9]:


def lucro(receita,custo, imprime = False):
    resultado = receita - custo
    if imprime:
        print(f"O lucro obtido foi: R${resultado:,.2f}")
    return resultado

l = lucro(25000,15000)


# In[10]:


l = lucro(25000,15000, True)


# In[11]:


def adicao(n1,n2):
    return n1 + n2
def multiplicacao(n1,n2):
    return n1*n2
def calcular(funcao,n1,n2):
    return funcao(n1,n2)

total_soma = calcular(adicao,50,25)
multi = calcular(multiplicacao,5,5)
print(f"O resultado da adição é: {total_soma}")
print(f"O resultado da multiplicacao é: {multi}")


# In[12]:


lista = [14,6,99]

def soma(val1,val2, imprime = False):
    resul = val1 + val2
    if imprime:
        print(f"O resultado da soma é: {resul}")
    return resul

soma(lista[1],lista[2])


# In[13]:


soma(lista[1],lista[2], True)


# In[14]:


soma(*lista) #desempacota e usa todos os elementos da lista


# In[15]:


def soma(imprime,*valores): #* recebe vários valores
    total = 0
    for valor in valores:
        total += valor
    if imprime:
        print(f"A média é: {total}")
    return total

x = soma(True, 15,15,20,48)


# In[16]:


x = soma(False, 15,15)


# In[17]:


def soma(*valores):
    total = 0
    for valor in valores:
        total += valor
    return total

def media(*valores):
    total = soma(*valores)
    return total / len(valores)
print(f"A média é {media(8.6,6.4,10,8.6):.2f}")


# A aula 056 mostrou que posso salvar essas últimas linhas de códigos contendo as funções em formato `.py` e abrir um outro script e realizar o comando:
# 
# `import funcao
# soma = funcao.soma(10,3,6,2,18)
# media = funcao.media(5.4,8.5,9.4,7.3)
# print("A média é:",media)` 
# 
# O resultado será o mesmo.

# In[18]:


import sys #localiza os módulos
print(sys.path)


# ### Funções Recursivas:

# In[19]:


def fatorial(x):
    if x <= 1:
        return 1
    else:
        return (x*fatorial(x-1))

num = int(input("Informe um número: "))
print(f"O fatorial de {num} é {fatorial(num)}")


# ### Validação entrada de dados:

# In[20]:


def validar_resposta(numero, inicio, fim):
    if numero.isdigit():
        if int(numero) < int(inicio) or int(numero) > int(fim):
            print("Número inválido! Digite um valor entre",inicio,"e",fim,".")
        else:
            return True
    else:
        print("Digite um valor válido. Insira um número inteiro entre",inicio,"e",fim,".")
    
while True:
    num = input("Informe um valor entre 1 e 10: ")
    if validar_resposta(num, 1,10):
        break
        


# In[21]:


def validar_tamanho(texto, maximo):
    if len(texto) > maximo:
        print("Tamanho máximo foi excedido. Tente novamente dentro do permitido de",maximo,"caracteres")
        print("Foram digitados",len(texto),"caracteres.")
    else:
        return True
    
while True:
    tex = input("Escreva um texto aqui: ")
    if validar_tamanho(tex,25):
        print("Total de",len(tex),"caracteres digitados.")
        break


# In[22]:


def validar_palavra(texto, lista):
    if texto.upper() in lista:
        return True
    else:
        print("Texto inválido. Tente novamente!")
        for item in lista:
            print(item)
            
while True:
    palavras = ["CELULAR", "CARRO", "CINEMA", "CAMA"]
    t = input("Informe uma palavra: ")
    if validar_palavra(t, palavras):
        break


# ### Expressões `lambda`:

# In[23]:


multiplica = lambda x:x*5
multiplica(5)


# In[24]:


a = lambda x: x**2
print(a(10))


# In[25]:


b = a(9)
print(b)


# In[26]:


def doido(n):
    return lambda x: x + n

somar1 = doido(10)
somar2 = doido(15)

pior_ainda1 = 5
pior_ainda2 = somar2(pior_ainda1)
print(pior_ainda2)


# In[27]:


s = lambda lista: sum(lista)
print(s([50,50,25,50]))


# In[28]:


curso = lambda a = "Katharine", b = "Góes", c = "Caravalho", d = "Pires":a+" "+b+" "+c+" "+d
print(curso())


# In[29]:


def nome():
    completo = lambda nome, sobrenome: nome + " " + sobrenome
    return completo

meu_nome = nome()

print("Meu nome compelto é:",meu_nome("Vera Lúcia", "Carvalho"))


# In[30]:


tabuada = [
    lambda x: f"{x}x1 = " + str(x * 1),
    lambda x: f"{x}x2 = " + str(x * 2),
    lambda x: f"{x}x3 = " + str(x * 3),
    lambda x: f"{x}x4 = " + str(x * 4),
    lambda x: f"{x}x5 = " + str(x * 5),
    lambda x: f"{x}x6 = " + str(x * 6),
    lambda x: f"{x}x7 = " + str(x * 7),
    lambda x: f"{x}x8 = " + str(x * 8),
    lambda x: f"{x}x9 = " + str(x * 9),
    lambda x: f"{x}x10 = " + str(x * 10)
]

num = int(input("Qual número quer ver a tabuada? "))
for x in tabuada:
    print(f"{x(num)}")


# ### Função `type`:

# In[31]:


def validar_type(lista):
    lista_strings = []
    lista_dicionario = []
    lista_lista = []
    soma_inteiros = 0
    qtd_inteiros = 0
    
    for item in lista:
        if type(item) == int:
            soma_inteiros += item
            qtd_inteiros += 1
        elif type(item) == str:
            lista_strings.append(item)
        elif type(item) == dict:
            lista_dicionario.append(item)
        elif type(item) == list:
            lista_lista.append(item)
        else:
            print(f"O tipo {type(item)} não é reconhecido.")
    
    if soma_inteiros > 0:
        print(f"Foram encontrados {qtd_inteiros} números inteiros.")
        print(f"Realizando a soma, o resultado é: {soma_inteiros}.")
            
    if len(lista_strings) > 0:
        print(f"Foram encontrados {len(lista_strings)} caracteres. São eles: ")
        for i in lista_strings:
            print(i)
            
    if len(lista_dicionario) > 0:
        print(f"Foram encontrados {len(lista_dicionario)} dicionários. São eles: ")
        for i in lista_dicionario:
            print(f"Chave: {i.keys()}")
            print(f"Valores: {i.values()}")
            
    if len(lista_lista) > 0:
        retorno = ""
        print(f"Foram encontrados {len(lista_lista)} lsitas. São elas: ")
        for lista in lista_lista:
            for i in lista:
                retorno = retorno + str(i) + ","
    print(retorno[0:-2]) # -2 para tirar as duas virgulas finais


# In[32]:


lista = [14,6,99,["Oi", "tudo","bem","?"],5,8,{"1": "Yaris", "2": "HB20"}, ["Quero", "um", "emprego"],
         "Katharine", {"Curso": "Ciências Econômicas", "Ocupação": "Cientista de Dados"}, [23,3,1], "Vera",
        [13,4,70], "Claudemir", {"Campus": "Piedade", "Faculdade": "Faculdade de Economia da UFBA"}]

validar_type(lista)


# ### Função `.map()`:

# In[33]:


def quadrada(numero):
    return f"O quadrado de {numero} é: {numero**2}"

l = [0,1,2,3,4,5,6,7,8,9,10]
calculo = map(quadrada,l)

for n in calculo:
    print(n)


# In[34]:


quadrado = lambda x: f"O quadrado de {x} é: {x**2}"
l = [0,1,2,3,4,5,6,7,8,9,10]
calculo = map(quadrado,l)

for n in calculo:
    print(n)


# In[35]:


quadrado = lambda x, y: f"A soma de {x} + {y} é: {x + y}"
l = [0,1,2,3,4,5,6,7,8,9,10]
l2 = [10,9,8,7,6,5,4,3,2,1,0]
calculo = map(quadrado,l,l2)

for n in calculo:
    print(n)


#!/usr/bin/env python
# coding: utf-8

# # Estruturas Condicionais:

# In[1]:


ava1 = float(input("Informe a nota da AVA1: "))
ava2 = float(input("Informe a nota da AVA2: "))
media = (ava1 + ava2) / 2

if media < 7:
    print(f'Aluno foi REPROVADO com média {media}')
else:
    print(f'Aluno foi APROVADO com média {media}')


# In[2]:


ava1 = float(input("Informe a nota da AVA1: "))
ava2 = float(input("Informe a nota da AVA2: "))
media = (ava1 + ava2) / 2

if media < 3:
    print(f'Aluno está REPROVADO com média {media:.2f}')
elif media > 3 and media < 7:
    print(f'Aluno está RECUPERAÇÃO com média {media:.2f}')
else:
    print(f'Aluno está APROVADO com média {media:.2f}')


# #### Desafio:

# In[3]:


perg1 = float(input("Informe um número: "))
perg2 = float(input("Informe outro número: "))
perg3 = float(input("Informe mais um número: "))
resp1 = float(input(f"Qual o resultado de {perg1} + {perg2}? "))

if resp1 == perg1 + perg2:
    print("Parabens! Resposta correta.")
else:
    print("Errou! A resposta correta é:", perg1 + perg2)
    
resp2 = float(input(f"Qual o resultado de {perg3} - {perg2}? "))

if resp2 == perg3 - perg2:
    print("Parabens! Resposta correta.")
else:
    print("Errou! A resposta correta é:", perg3 - perg2)
    
resp3 = float(input(f"Qual o resultado de {perg1} x {perg2} x {perg3}? "))

if resp3 == perg1 * perg2 * perg3:
    print("Parabens! Resposta correta.")
else:
    print("Errou! A resposta correta é:", perg1 * perg2 * perg3)
    
resp4 = float(input(f"Qual o resultado de {perg1} / {perg2}? "))

if resp4 == perg1 / perg2:
    print("Parabens! Resposta correta.")
else:
    print("Errou! A resposta correta é:", perg1 / perg2)


# In[4]:


num = int(input("Digite um número: "))
resto = num % 2

if resto == 0:
    print(f"O número {num} é PAR")
else:
    print(f"O número {num} é IMPAR")


# # Estruturas de repetição

# `for` refêrencia `in` sequência: onde referência é a variável que vai receber um valor da sequência a cada interação.

# In[5]:


numero = [1,3,5,7]

for num in numero:
    print(num)


# In[6]:


frutas = ["Maça", "Laranja", "Tangerina", "Uva"]

for fruta in frutas:
    print('Fruta: ',fruta)


# In[7]:


for letra in "Katharine":
    print(letra)


# In[8]:


for num in range(0,10):
    if num % 2 == 0:
        print(f"{num} é PAR")
    else:
        print(f"{num} é IMPAR")


# In[9]:


par = 0 
impar = 0

for num in range(0,10):
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print(f"Temos {par} números PARES")
print(f"Temos {impar} números IMPARES")


# In[10]:


num = [[], []]
resto = 0

for c in range(1,11):
    resto = int(input(f"Digite o {c}.o número: "))
    if resto % 2 == 0:
        num[0].append(resto)
    else:
        num[1].append(resto)
        
        
print("Temos a lista: ",num)
num[0].sort()
num[1].sort()
print("Lista com as números pares: ",num[0])
print("Lista com as números impares: ",num[1])


# #### `while`:

# In[11]:


x = 0
while x < 10:
    print(x)
    x = x + 1


# In[12]:


x = 0
while x < 5:
    x = x + 1
    print(x)
else:
    print("ESGOTADO")


# In[13]:


par = 0
quantidade = 5
while par < quantidade:
    par = par + 1
    print(par)


# #### Desafio:
# 1º - Você gosta de Python?

# In[14]:


while True:
    resp = input("Você gosta de Python? ")
    if resp.upper() == "SIM":
        print("Resposta correta!")
        break
    else:
        print("Resposta errada! Tente mais uma vez.")


# 2º - Tabuada

# In[15]:


n = int(input("Digite qual número você gostaria de ver a tabuada: "))

for num in range(1,11):
    print("A tabuada de", n, "é: ", n, "x", num, "=", n*num)


# 3º - Treinar Tabuada

# In[16]:


treinar = int(input("Qual tabuada você quer treinar? "))
acertos = 0
erros = 0

for n in range(1,11):
    perg = int(input(f"{treinar} x {n} é: "))
    if perg == (treinar*n):
        print("PARABÉNS! Você acertou.")
        acertos = acertos + 1
    else:
        print("Puts... Você errou. O resultado corretor é: ", treinar*n)
        erros = erros + 1
        
print("Voce acertou",acertos, 'e errou', erros)


#!/usr/bin/env python
# coding: utf-8

# # Conceitos básicos:

# In[1]:


X = 10
Y = 25
soma = X + Y #soma recebe x + y, esse é o jeito correto de ler
print("O resultado da adição entre", X, "e", Y, 'é igual a', soma)


# In[2]:


100%2


# In[3]:


100%3


# ### Variáveis numéricas:
# - *int* => significa números inteiros
# - *float* => significa números de ponto flutuantes: 1.28
# - *complex* => significa números complexos: 4j

# In[4]:


inteiro = 20
flutuante = 14.06
complexo = 4j + 5 

print("O resultado de",inteiro, "+", 50, "é igual a:",inteiro + 50)
print("O resultado de",flutuante, "+", 0.99, "é igual a:",flutuante + 0.99)
print("O resultado de",complexo,"+ (20 - 2j + 3) é igual a:",complexo + 20 - 2j + 3)


# ### Variáveis tipo lógico:
# Também conhecidas como boleanas
# - *true* 
# - *false*

# In[5]:


chuva = True
nao_chuva = False

print(chuva)
print(nao_chuva)


# In[6]:


p = 14
k = 6

print("p é diferente de k:", p != k)
print("p é igual a k:", p == k)
print("p é maior ou igual a k:", p >= k)
print("p é menor ou igual a k:",p <= k)
print("p é maior que k:",p > k)
print("p é menor que k:",p < k)


# In[7]:


a = True
b = False

print("negativo de a é:",not a)
print("negativo de b é:",not b)


# In[8]:


c = not True
d = not False

print("c é:",c)
print("d é:",d)


# In[9]:


log1 = (p < k)
log2 = (p == k)
log3 = (p >= k)
log4 = (p != k)

print(log1 and log2) #ambos tem que ser atendidos
print(log3 and log4)
print(log3 or log2) #pelo menos um tem que atender a solicitação
print(log1 or log4)


# ordem das variáveis lógicas: ``not``, `and`, `or`. 

# ### Variáveis tipo string:
# Variáveis com caracteres, textos

# In[10]:


frase = "Olá, quero muito um emprego."
len(frase)


# Para acessar a posição de cada caractere, basta usar o índice:

# In[11]:


frase[3]


# In[12]:


frase[10]


# In[13]:


frase[20]


# Python é uma liguaguem de tipagem forte

# In[14]:


a = 10
f = "Roi, Letícia, né?!"

soma = a + f
print("O resultado é:",soma)


# In[15]:


soma = str(a) + f
print("O resultado depois de transfromado em string é:",soma)


# ### Entrada de dados:

# In[16]:


input("Informe o teu nome: ")


# In[17]:


idade = input("Digite a sua idade: ")
print(f"IDADE:{idade}")


# In[18]:


nome = input("Informe o teu nome: ")
print("NOME:",nome)


# In[19]:


resp = input("Quanto é 1 + 1?\n"
            "a) 11\n"
            "b) 2\n"
            "c) 1,1\n"
            "d) 1\n"
            "RESPOSTA: ")


# In[20]:


ano = 2021
nascimento = int(input("Digite o ano de seu nascimento: "))
idade = ano - nascimento
print("Então sua idade é",idade,"anos!")


# In[21]:


ano = int(input("Digite o ano desejado: "))
nascimento = int(input("Digite o ano de seu nascimento: "))
idade = ano - nascimento
print("Então em",ano,"sua idade será",idade,"anos!")


# In[22]:


juros = float(input("Digite a taxa de juros: "))
emprestimo = float(input("Digite o valor a ser emprestado: "))
fv = (1 + (juros/100)) * emprestimo
print("Então no vencimento você pagará",fv)


# ### Mais sobre `strings`:

# In[23]:


a = "Olá, meu nome é "
b = "Katharine Pires. E o seu?"
concat = a + b
print(concat)


# In[24]:


c = "agua "
multi = c * 5
print(multi)


# ### Composição ou Interpolação:
# Combinar e colocar `strings` e até dados dentro de outra `string`
# - *%s* => string
# - *%d* => inteiro
# - *%f* => real
# - *%%* => porcentagem

# In[25]:


cinema = "Bela Vista"
frase = "Vamos ao %s assistir Mulher Maravilha" % cinema
print(frase)


# In[26]:


pagar = 150
frase = "Passe no Bootcamp e tive que pagar %d para a matrícula" % pagar
print(frase)


# In[27]:


taxa = 2.0
frase = "O copom deve se reunir e manter a SELIC em %.2f%% ao ano" % taxa
print(frase)


# In[28]:


frase = 'Fomos ao {} e pagamos mais de R${} só em comida, isso é culta da SELIC a {} ao ano!'.format(cinema, pagar, taxa)
print(frase)


# In[29]:


frase = "Estou pensando em comprar um {1} novo porque o nosso já está ruim".format('carro','moto','casa')
print(frase)


# In[30]:


f"paguei R${pagar} de matrícula!"


# In[31]:


f"Fui ao {cinema} com minha amiga!"


# Fatiamento de `string`: string[x:y:z] onde **x** é o incício da posição, **y** é o fim da posição e o **z** é o salto

# In[32]:


frase[2:11:2]


# In[33]:


frase[5:16]


# In[34]:


frase[:]


# In[35]:


frase[::-1]


# In[36]:


frase.index('c')


# In[37]:


frase[18]


# In[38]:


frase.index('moto')


# In[39]:


frase[29]


# Achando um email:

# In[40]:


email = "katharinepires@outlook.com"
print(email.index('.com'))


# In[41]:


print(email.index('@'))


# In[42]:


arroba = email.index('@')
print("NOME DE USUÁRIO: ",email[0:arroba])


# In[43]:


ponto = email.index('.')
print('O provedor de email é: ',email[arroba+1:ponto]) #+1 para não sair o @


# In[44]:


outro = "kkathy1999.kp@gmail.com"
usuario, provedor = outro.split('@')
print('Nome de usuário:',usuario)
print('Provedor:',provedor)


# In[45]:


ponto = provedor.index('.')
print('Nome de usuário:',usuario)
print('Provedor:',provedor[:ponto])


# #### Desafios:
# 1º - Valor da compra

# In[46]:


valor = float(input('Qual valor mensal da parcela: '))
parcela = int(input('Em qauntas parcelas serão: '))
total = valor * parcela
print(f'O valor total da compra é: {total:,.2f}')


# 2º - Comparar Strings

# In[47]:


texto1 = "Pizza de Queijo"
texto2 = "Pizza de Frango com Requeijão"
print('O tamanho do primeiro texto é:',len(texto1))
print('O tamanho do segundo texto é:',len(texto2))


# In[48]:


print('Os textos possuem as mesmas quantidades de caracetres?',len(texto1) == len(texto2))
print('Os textos são iguais?',texto1 == texto2)


# 3º - Árvore de natal

# In[49]:


print(" "*10 + "x")
print(" "*10 + "X")
print(" "*9 + "X"*3)
print(" "*8 + "X"*5)
print(" "*7 + "X"*7)
print(" "*6 + "X"*9)
print(" "*5 + "X"*11)
print(" "*4 + "X"*13)
print(" "*3 + "X"*15)
print(" "*9 + "X"*3)
print(" "*9 + "X"*3)
print(" "*9 + "X"*3)


# In[50]:


salario = float(input("Digite o seu slário: "))
aumento = float(input("Digite o valor do aumento: "))
fv = (1 + (aumento/100)) * salario
print(f"Seu salário com o aumento de {aumento}% será de R${fv:,.2f}")


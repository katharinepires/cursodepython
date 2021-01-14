#!/usr/bin/env python
# coding: utf-8

# # Acessando arquivos:
# Não é necessário importar bibliotecas, basta apenas informar se será para leitura ou escrita. 

# ### Escrevendo um arquivo com a função `write`:

# In[1]:


arquivo1 = open("arquivo1_teste.txt", "w")
arquivo1.write("Olá, mundo! Este é o meu primeiros aqruivo escrito no python. \n")
arquivo1.write("Vou escrever a canção do meu filme preferido: Uma vez num sonho, da Bela Adormecida: \n")
arquivo1.write("Foi você o sonho bonito que eu sonhei \n")
arquivo1.write("Foi você eu lembro tão bem você na linda visão \n")
arquivo1.write("E me fez sentir que o meu amor nasceu então \n")
arquivo1.write("E aqui está você, somente você a mesma visão \n")
arquivo1.write("Aquela do sonho que eu sonhei... \n")
arquivo1.close()


# Agora se eu usar novamente o comando, ele irá apagar o que já tinha e escrever o que tem de novo:

# In[2]:


arquivo1 = open("arquivo1_teste.txt", "w")
arquivo1.write("Olá, mundo! Este é o meu segundo aqruivo escrito no python. \n")
arquivo1.write("Antes escrevi a canção do meu filme preferido: Uma vez num sonho, da Bela Adormecida: \n")
arquivo1.close()


# Usando o "a", ele não apaga o que tinha antes, so adiciona o que foi alterado:

# In[3]:


arquivo1 = open("arquivo1_teste.txt", "a")
arquivo1.write("Olá, mundo! Este é o meu terceiro aqruivo escrito no python. \n")
arquivo1.write("Antes escrevi a canção do meu filme preferido: Uma vez num sonho, da Bela Adormecida: \n")
arquivo1.write("Foi você o sonho bonito que eu sonhei \n")
arquivo1.write("Foi você eu lembro tão bem você na linda visão \n")
arquivo1.write("E me fez sentir que o meu amor nasceu então \n")
arquivo1.write("E aqui está você, somente você a mesma visão \n")
arquivo1.write("Aquela do sonho que eu sonhei... \n")
arquivo1.close()


# E para apernas ler, basta usar o comando "r":

# In[4]:


arquivo1 = open("arquivo1_teste.txt", "r")
print(arquivo1.read())
arquivo1.close()


# Lendo o arquivo linha a linha:

# In[5]:


arquivo1 = open("arquivo1_teste.txt", "r")
print(arquivo1.readline())
print(arquivo1.readline())
arquivo1.close()


# In[6]:


arquivo1 = open("arquivo1_teste.txt", "r")
print(arquivo1.readline(15)) #primeiros ccaracteres
arquivo1.close()


# In[7]:


arquivo1 = open("arquivo1_teste.txt", "r")
print(arquivo1.readline(15)) #primeiros ccaracteres
print(arquivo1.readline())
arquivo1.close()


# Retornando lista:

# In[8]:


arquivo1 = open("arquivo1_teste.txt", "r")
linhas = arquivo1.readlines()
print(linhas)
print(linhas[5]) #item 5 da lista
arquivo1.close()


# In[9]:


arq = open("arquivo1_teste.txt", "r")
for arquivo in arq.readlines():
    print(arquivo)
arq.close()


# In[10]:


arquivo2 = open("arquivo2_teste.txt", "w")
linhas_ = ["Temos as semanas: \n", "5ª SEMANA DE JULHO, 25/07/2021 até 01/08/2021 (N° 31/2021) \n", 
          "SEMANA DE JUNHO, DIA 20/06/2021 até 27/06/2021 (N° 26/2021) \n", 
           "Ainda falta a terceira semana para escolhermos \n"]
arquivo2.writelines(linhas_)
arquivo2.close()


# Usando o `with`: a vantagem dele é que ele automaticamente fecha o arquivos abertos depois de finalziado o seu uso.

# In[11]:


with open("arquivo2_teste.txt", "a") as arqui:
    arqui.write("Vamos ver se conseguimos marcar para a mesma semana que tia Cláudia!")


# Se não usado o "r", ele já colocar como padrão que será leitura:

# In[12]:


with open("arquivo2_teste.txt") as a:
    for linha in a:
        print(linha)


# In[13]:


with open("te_vivo.txt", "r") as musica:
    for letra in musica:
        palavras = letra.split()
        print(palavras)


# In[14]:


with open("te_vivo.txt", encoding = "utf-8") as musica:
    for letra in musica:
        palavras = letra.split()
        print(palavras)


# In[15]:


with open("te_vivo.txt", encoding = "utf-8") as musica:
    for letra in musica:
        palavras += letra.split()
print(palavras)


# Sistema para encontrar palavras dentro da música:

# In[16]:


palavra = []
with open("te_vivo.txt", encoding = "utf-8") as musica:
    for letra in musica:
        letra = letra.replace(",", "")
        palavras += letra.upper().split()
print(palavras)


# In[17]:


while True:
    palavra = input("Informe uma palavra ('sair' finaliza o programa): ")
    
    if palavra.upper() == "SAIR":
        break
    elif palavra.upper() in palavras:
        print(f"A palavra {palavra} está na música")
        print(f"Ela aparece {palavras.count(palavra.upper())} vezes!")
    else:
        print(f"A palavra {palavra} não faz parte da música")


# ### Lidando com diretórios e pastas:

# In[18]:


#identificando o diretório atual:
import os
print(os.getcwd())


# In[19]:


#criando diretórios:
os.mkdir("Chatbot do Messenger")


# In[20]:


#criando vários diretórios:
os.makedirs("Teste1/Teste2")


# In[21]:


#navegando em diretórios:
os.chdir("Teste1")
print("Pasta atual: ",os.getcwd())


# In[22]:


#para voltar diretório:
os.chdir("..")
print("Pasta atual: ",os.getcwd())


# In[23]:


#renomeando os diretórios:
os.rename("Chatbot do Messenger", "Lembrar de Excluir")


# In[24]:


#renomar o que não está no caminho atual:
os.rename("Teste1/Teste2", "Teste1/APAGAR")


# In[25]:


#renomeando arquivos:
os.rename("arquivo1_teste.txt", "mudou_nome.txt")


# In[26]:


#usando o rename para mover os arquivos:
os.rename("mudou_nome.txt", "Teste1/mudou_nome.txt")


# In[27]:


#listando diretórios e arquivos:
print(os.listdir("C:\Windows\Fonts"))


# In[28]:


#identificando se é diretório e arquivo:
for obj in os.listdir("."):
    if os.path.isdir(obj):
        print(obj, "é um diretório!")
    elif os.path.isfile(obj):
        print(obj, "é um arquivo!")


# In[29]:


diretorios = []
arquivos = []

for obj in os.listdir("."):
    if os.path.isdir(obj):
        diretorios.append(obj)
    elif os.path.isfile(obj):
        arquivos.append(obj)
        
print("Diretórios:",diretorios)
print("Arquivos:",arquivos)


# In[30]:


#verificando a existencia de um aquivo ou diretório:
import os.path

while True:
    nome = input("Informe o nome do arquivo ou do diretório: ")
    if nome.upper() == "SAIR":
        break
    if os.path.exists(nome):
        print(nome,"existe")
        if os.path.isdir(nome):
            print(nome,"é um diretório.")
        elif os.path.isfile(nome):
            print(nome,'é um arquivo.')
    else:
        print(nome,"não existe")


# In[31]:


#obtendo informações sobre o arquivo:
import time

while True:
    nome = input("Informe o nome do arquivo: ")
    if nome.upper() == "SAIR":
        break
    print("Nome:",nome)
    print("Tamanho:",os.path.getsize(nome),"bytes")
    print("Data de criação:",time.ctime(os.path.getctime(nome)))
    print("Data de modificação:",time.ctime(os.path.getmtime(nome)))
    print("Data de acesso:",time.ctime(os.path.getatime(nome)))


# In[32]:


#acessando subdiretórios recursivamente:
for raiz, diretorios, arquivos in os.walk("C:\\Users\\Katharine\\Documents"
                                          "\\curso_python"
                                          "\\conceitos_basicos"):
    print("\nCaminho completo:",raiz)
    for diret in diretorios:
        print(f"{diret}")
    for arq in arquivos:
        print(f"{arq}")


# Excluindo arquivos e diretórios:

# In[33]:


excloi = open("excloi_esse.txt", "w")
excloi.write("Esse aqui é só para aprender a exluir arquivos e diretórios")
excloi.close()


# In[34]:


os.remove("excloi_esse.txt")


# In[35]:


os.rmdir("Lembrar de Excluir") #apenas para diretórios vazios


# In[36]:


import shutil
shutil.rmtree("Teste1")


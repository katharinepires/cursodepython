#!/usr/bin/env python
# coding: utf-8

# # Exceções com o `try`:

# In[1]:


valor = input("Informe um valor: ")
soma = int(valor) - 21
resultado = soma / int(valor)
print(f"O resultado foi {resultado}")


# Aqui o erro está porque não se pode dividir por zero, vamos usar o `try` para melhorar:

# In[2]:


valor = input("Informe um valor: ")

try:
    soma = int(valor) - 21
    resul = soma / int(valor)
except:
    print("Ocorreu um erro")


# In[3]:


valor = input("Informe um valor: ")

try:
    soma = int(valor) - 21
    resul = soma / int(valor)
except ZeroDivisionError:
    print("Ocorreu um erro, não se pode dividir o valor por 0.")
except ValueError:
    print("Ocorreu um erro. Valor informado inválido.")


# In[4]:


valor = input("Informe um valor: ")

try:
    soma = int(valor) - 21
    resul = soma / int(valor)
except ZeroDivisionError:
    print("Ocorreu um erro, não se pode dividir o valor por 0.")
except ValueError:
    print("Ocorreu um erro. Valor informado inválido.")


# In[5]:


valor = input("Informe um valor: ")

try:
    soma = int(valor) - 21
    resul = soma / int(valor)
except ZeroDivisionError:
    print("Ocorreu um erro, não se pode dividir o valor por 0.")
except ValueError:
    print("Ocorreu um erro. Valor informado inválido.")
else:
    print("Parabéns! Informação válida recebida com sucesso!")


# In[6]:


valor = input("Informe um valor: ")

try:
    soma = int(valor) - 21
    resul = soma / int(valor)
except ZeroDivisionError:
    print("Ocorreu um erro, não se pode dividir o valor por 0.")
except ValueError:
    print("Ocorreu um erro. Valor informado inválido.")
finally:
    print("Executando... Mesmo na ocorrência de erros!")


# Realizando o uso de `except`, o código roda mesmo na ocorrência de erro:

# In[7]:


valor = input("Informe um valor: ")

try:
    soma = int(valor) - 21
    resul = soma / int(valor)
except ZeroDivisionError:
    print("Ocorreu um erro, não se pode dividir o valor por 0.")
except ValueError:
    print("Ocorreu um erro. Valor informado inválido.")
finally:
    print("Executando... Mesmo na ocorrência de erros!")

x = 2021
y = 1999
z = x - y
print(f"Eu tenho {z} anos!")


# In[8]:


valor = input("Informe um valor: ")

try:
    soma = int(valor) - 21
    resul = soma / int(valor)
    
    print(f"A soma é {soma}")
    print(f"O resultado final é {resul}")
except Exception as a:
    print("Ocorreu o erro:",a)


# Criando/forçando uma exceção:

# In[12]:


def converter_string(a):
    if a not in ("0","1","2","3","4","5","6","7","8","9","10"):
        raise ValueError("Erro: informe um valor entre 0 e 10!")
    return int(a)


# In[13]:


num = input("Informe um número: ")
taxa = ((converter_string(num)/100) + 1)
print(taxa)


# In[14]:


num = input("Informe um número: ")
taxa = ((converter_string(num)/100) + 1)
print(f"A uma taxa de {num}% ao ano você pagará R${taxa*2545:,.2f}.")


# Usando o TraceBack para identificar exceção:

# In[15]:


import traceback

try:
    nome_arquivo = input("Informe o nome do arquivo: ").strip()
    arquivo = open(nome_arquivo)
except:
    trace = traceback.format_exc()
    
    print("Ocorreu um erro: \n", trace)
    open("trace.log","a").write(trace) #cria um arquivo informado o erro


# In[16]:


valor = input("Informe um valor: ")

try:
    soma = int(valor)
    resul = 10 / int(valor)
    
    print(f"A subtração é {soma}")
    print(f"O resultado final é {resul}")
except:
    x = 10/0
    print("ERROOU!!")


# Ocorrendo o segundo erro, ele também mostra: `During handling of the above exception, another exception occurred:`

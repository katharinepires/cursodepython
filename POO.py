#!/usr/bin/env python
# coding: utf-8

# # Programação Orientada a Objetos

# ### Classe de objeto:

# In[1]:


class Heroi:
    voa = False
    possui_arma = False
    lanca_teia = False
    forca = False
    frase_comum = ""
    
    def falar(self):
        print(self.frase_comum)
    
    def detalhar(self):
        if self.voa:
            print("O heroi voa")
        if self.possui_arma:
            print("O herio possui uma arma")
        if self.lanca_teia:
            print("O heroi lança teia")
        if self.forca:
            print("O heroi é super forte")


# In[2]:


homem_aranha = Heroi()
homem_aranha.lanca_teia = True
print(homem_aranha.voa)
print(homem_aranha.lanca_teia)


# In[3]:


he_man = Heroi()
he_man.possui_arma = True
he_man.forca = True
he_man.frase_comum = "Eu tenho a força!"
he_man.falar()


# In[4]:


homem_aranha.detalhar()
he_man.detalhar()


# In[5]:


class Heroi:
    def __init__(self, voa, possui_arma, lanca_teia, forca, frase_comum):
        print("O __init__ está executando ...")
        self.voa = voa
        self.possui_arma = possui_arma
        self.lanca_teia = lanca_teia
        self.forca = forca
        self.frase_comum = frase_comum
        
    def falar(self):
        print(self.frase_comum)
    
    def detalhar(self):
        if self.voa:
            print("O heroi voa")
        if self.possui_arma:
            print("O herio possui uma arma")
        if self.lanca_teia:
            print("O heroi lança teia")
        if self.forca:
            print("O heroi é super forte")


# In[6]:


super_homem = Heroi(True, False, False, True,"")
super_homem.detalhar()


# In[7]:


class Pessoa():
    especie = "Humano"
    
print(Pessoa.especie)
Pessoa.vivo = True
print(Pessoa.vivo)

homem = Pessoa()
print(homem.especie)
print(homem.vivo)
    
Pessoa.vivo = False
print(homem.vivo)
    
homem.nome = "Katharine"
homem.sobrenome = "Pires"
print(homem.nome, homem.sobrenome)


# ### Sobreamento:
# Python não acha o objeto e continua buscando até na classe ou até chegar no fim da herança

# In[8]:


class Ponto():
    x = 10
    y = 7
p = Ponto()    

print(p.x) #10 por causa da classe 
print(p.y) #7 por causa da classe
p.x = 12 #p obtem seu próprio atributo "x"
print(p.x) #instância
print(Ponto.x) #ainda será 10 pq nada foi alterado
del p.x #excluindo a instância 
print(p.x) #será retornado 10 da classe
p.z = 14
print(p.z) #será 14
#mas Ponto.z dá erro pois o objeto não tem o atributo "z"


# ### `self`:

# In[9]:


class Quadrado():
    lados = 4
    def area(self): #referencia a intância
        return self.lados ** 2
quadrado = Quadrado()
print(quadrado.area())


# In[10]:


print(Quadrado.area(quadrado)) 


# In[11]:


quadrado.lados = 5
print(quadrado.area())


# In[12]:


class Calculo():
    def calcular_total(self, quantidade, desconto):
        return (self.preco * desconto - quantidade)
    
calc = Calculo()
calc.preco = 15
calc.quantidade = 5
calc.desconto = 15
print(calc.calcular_total(calc.quantidade,calc.desconto))


# In[13]:


print(calc.calcular_total(15,10))


# In[14]:


print(Calculo.calcular_total(calc, 15, 10))


# ### Herança

# In[15]:


class Classe_base():
    def __init__(self, valor1, valor2):
        print("__init__ está sendo executado ...")
        self.valor1 = valor1
        self.valor2 = valor2
    def somar(self):
        return self.valor1 + self.valor2
    def subtrair(self):
        return self.valor1 - self.valor2


# In[16]:


class Derivada1(Classe_base):
    def __init__(self, valor1, valor2):
        print("Método __init__ da classe Derivada1.")
        self.valor1 = valor1
        self.valor2 = valor2
        super().__init__(valor1, valor2) #contrutor da classe base, classe mãe
    def imprimir(self, texto):
        print(texto)


# In[17]:


class Derivada2(Classe_base):
    def multiplicar(self, valor1, valor2):
        return valor1 * valor2


# In[18]:


class Teste():
    calculo = Derivada1(10,25)
    resultado = calculo.somar()
    print(resultado)
    resultado = calculo.subtrair()
    print(resultado)
    calculo.imprimir("Que negócio meio louco!")
    
    calc = Derivada2(70,85)
    resultado = calc.multiplicar(20,10)
    print(resultado)
    resultado = calc.somar()
    print(resultado)


# In[19]:


class Pai():
    def __init__(self):
        print("Construindo a classe Pai")

class Filha(Pai):
    def __init__(self):
        Pai.__init__(self)

filha = Filha()


# In[20]:


class Mae():
    def __init__(self):
        print("Construindo a classe Mãe")
        
class Filha(Mae):
    def __init__(self):
        Pai.__init__(self)

filha = Filha() #ficou fixado o __init__ da classe Pai


# In[21]:


class Filha(Mae):
    def __init__(self):
        super().__init__() #executa a classe base, independente qual seja

filha = Filha()


# In[22]:


class Veiculo():
    def __init__(self, motor,rodas):
        self.motor = motor
        self.rodas = rodas
    def ligar(self):
        if self.motor:
            print("O veículo está ligado!")
        else:
            print("O veículo não tem motor.")
    def desligar(self):
        if self.motor:
            print("O veículo está desligado!")
        else:
            print("O veículo não tem motor.")
    def andar(self):
            print("O veículo está andando!")
    def parado(self):
            print("O veículo está parado!")      


# In[23]:


class Carro(Veiculo):
    def __init__(self, rodas):
        Veiculo.__init__(self, True, rodas)
class Bike(Veiculo):
    guidao = True
    def __init__(self,rodas):
        Veiculo.__init__(self, False, rodas)
    def empinar(self):
        print("A bike empinou!")


# In[24]:


bike = Bike(2)
print(bike.guidao)
print(bike.rodas)
bike.ligar()
bike.andar()
bike.empinar()
bike.parado()
bike.desligar()


# In[25]:


carro = Carro(4)
print(carro.rodas)
carro.ligar()
carro.andar()
carro.parado()
carro.desligar()


# ### Herança Múltipla:

# In[26]:


class Terrestre(object):
    anda_terra = True
    def __init__(self, velocidade):
        self.velocidade = velocidade
class Carro(Terrestre):
    rodas = 4
    def __init__(self, velocidade_terra, portas):
        self.portas = portas
        super().__init__(velocidade_terra)
class Aquatico(object):
    anda_agua = True
    def __init__(self, velocidade):
        self.velocidade = velocidade
class Barco(Aquatico):
    def __init__(self, velocidade_agua, helices):
        self.helices = helices
        super().__init__(velocidade_agua)
class Anfibio(Carro, Barco):
    def __init__(self, velocidade_terra, velocidade_agua, portas, helices):
        self.velocidade_agua = velocidade_agua
        self.velocidade_terra = velocidade_terra
        self.portas = portas
        self.helices = helices
        Carro.__init__(self, velocidade_terra, portas)
        Barco.__init__(self, velocidade_agua, helices)


# In[27]:


meu_bicho = Anfibio(50,100,4,1)
print(meu_bicho.velocidade_terra)
print(meu_bicho.portas)
print(meu_bicho.velocidade_agua)
print(meu_bicho.helices)
print(meu_bicho.anda_agua)
print(meu_bicho.anda_terra)
print(meu_bicho.rodas)


# In[28]:


class Terrestre(object):
    anda_terra = True
    def __init__(self, velocidade):
        self.velocidade = velocidade
class Carro(Terrestre):
    rodas = 4
    def __init__(self, velocidade_terra, portas, **kwargs):
        self.portas = portas
        super().__init__(velocidade_terra)
class Aquatico(object):
    anda_agua = True
    def __init__(self, velocidade):
        self.velocidade = velocidade
class Barco(Aquatico):
    def __init__(self, velocidade_agua, helices):
        self.helices = helices
        super().__init__(velocidade_agua)
class Anfibio(Carro, Barco):
    def __init__(self, velocidade_terra, velocidade_agua, portas, helices):
        self.velocidade_agua = velocidade_agua
        self.velocidade_terra = velocidade_terra
        self.portas = portas
        self.helices = helices
        super().__init__(velocidade_terra = velocidade_terra, velocidade_agua = velocidade_agua,
                        portas = portas, helices = helices)


# In[29]:


meu_bicho = Anfibio(50,100,4,1)
print(meu_bicho.velocidade_terra)
print(meu_bicho.portas)
print(meu_bicho.velocidade_agua)
print(meu_bicho.helices)
print(meu_bicho.anda_agua)
print(meu_bicho.anda_terra)
print(meu_bicho.rodas)


# ### Polimorfismo:

# In[30]:


class Dog():
    def som(self):
        print("Au au au")
class Gato():
    def som(self):
        print("Miau miau")
        
def emitir_som(animal):
    animal.som()

doguinho = Dog()
gato = Gato()
emitir_som(doguinho)
emitir_som(gato)


# In[31]:


class Porta():
    def fechar(self):
        print("A porta está fechada!")
    def abrir(self):
        print("A porta está aberta!")
class Janela():
    def fechar(self):
        print("A janela está fechada!")
    def abrir(self):
        print("A janela está aberta!")  

def abertura(o_que_abrir):
    o_que_abrir.abrir()
def fechamento(o_que_fechar):
    o_que_fechar.fechar()
    
janela = Janela()
porta = Porta()
abertura(porta)
abertura(janela)
fechamento(janela)
fechamento(porta)


# In[32]:


class Animal(object):
    def emitir_som(self):
        raise NotImplementedError("Método não emitido.")
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au au")
class Gatos(Animal):
    print("Miau miau")
class Girafa(Animal):
    def comer(self):
        print("A Gifara está comendo")

def barulho(animal):
    animal.emitir_som()
    
dog = Cachorro()
gatinho = Gatos()
girafa = Girafa()

barulho(dog)
barulho(gatinho)
barulho(girafa)


# In[33]:


class Animal(object):
    def emitir_som(self):
        print("Som desconhecido.")
class Girafa(Animal):
    def comer(self):
        print("A Gifara está comendo")

def barulho(animal):
    animal.emitir_som()
    
girafa = Girafa()
barulho(girafa)


# ### Classe Aberta: 
# Qualquer coisa, assista a aula 073

# ### Encapsulamento:
# é uma maneira de deixar os objetos com suas informações privadas e inalteradas. Para manipular as informações, se usa `get` e o `set`.

# In[34]:


class Carro(object):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
    def get_modelo(self):
        return self._modelo
    def set_modelo(self, modelo):
        self._modelo = modelo

carro = Carro("Ford", "Ranger")
print(carro._marca) #o _marca, apesar de poder ser acessado, indica que é não público


# In[35]:


carro._marca = "Fiat"
print(carro._marca)


# In[36]:


carro.set_modelo("Uno") #correto é usar dessa maneira e não as de cima, pois o _maraca é não público
print(carro.get_modelo()) #correto


# In[37]:


class Carro(object):
    marca = "Toyota"
    __modelo = "Yaris"
    
carro = Carro()
print(dir(carro)) #dir retorna em lista os atributos do objeto


# `print(carro.)` no PyCharm não aparece a opção de completar com o `__modelo`, em teoria é privado.

# In[38]:


class Carro(object):
    marca = "Toyota"
    __modelo = "Yaris"
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo
    
carro = Carro()
print(carro.marca)


# In[39]:


carro.marca = "Hyundai"
print(carro.marca)


# In[40]:


carro.set_modelo("HB20")
print(carro.get_modelo())


# In[41]:


carro._Carro__modelo = "Tucson"
print(carro.get_modelo())


# In[42]:


print(carro.modelo)


# In[43]:


print(carro.__modelo)


# In[ ]:


class Mae(object):
    def __init__(self):
        self.__atributo_privado = 10
        
class Filha(Mae):
    def pegar_atributo_privado(self):
        return self.__atributo_privado
    
filha = Filha()
print(filha.__dict__) #retorna o dicionário dos atributos


# In[ ]:


x = filha.pegar_atributo_privado()
print(x)


# In[44]:


class Mae(object):
    def __init__(self):
        self.__atributo_privado = 10
        
class Filha(Mae):
    def pegar_atributo_privado(self):
        return self._Mae__atributo_privado
    
filha = Filha()
x = filha.pegar_atributo_privado()
print(x)


# `if__name__ == '__main__'`: é usado quando se quer executar parte do código apenas se estiver sendo executada no escopo principal e não de módulo importado da classe.

# In[45]:


class Arquivo1(object):
    def __init__(self):
        print("__name__ :",__name__)
    def somar(self, x, y):
        return x + y
if __name__ == "__main__":
        a = Arquivo1()
        print("A soma arq1 é:",a.somar(55,75))


# `from POO import Arquivo1
# a = Arquivo1()
# print("Agora a soma é: ",a.somar(85,95))` 
# 
# e o resultado será:
# 
# `__name__ : __main__
# Agora a soma é: 180` 

# In[46]:


a = Arquivo1()
print("Agora a soma arq2 é: ",a.somar(85,95))


# ### Propriedades:
# 1º => sem o `@property`:

# In[47]:


class Arrancada(object):
    def __init__(self, metros, segundos):
        self._metros = metros
        self._segundos = segundos
        self._velocidade = self._metros / self._segundos
    def get_velocidade(self):
        print(f"A velocidade foi de {self._velocidade:.2f} metros por segundo")
        
a = Arrancada(100,120)
a.get_velocidade()


# 2º => com o `@property`:

# In[48]:


class Arrancada(object):
    def __init__(self, metros, segundos):
        self._metros = metros
        self._segundos = segundos
        self._velocidade = self._metros / self._segundos
        
    @property
    def velocidade(self):
        print(f"A velocidade foi de {self._velocidade:.2f} metros por segundo")
        
a = Arrancada(100,120)
a.velocidade #é uma função mas foi assinada para ser uma propriedade


# Criando propriedade chamando a função:

# In[49]:


class Arrancada(object):
    def __init__(self, metros, segundos):
        self._metros = metros
        self._segundos = segundos
        self._velocidade = self._metros / self._segundos
    def get_velocidade(self):
        print("Executou get_velocidade")
        return f"A velocidade foi de {self._velocidade:.2f} metros por segundo"
    def set_velocidade(self, velocidade):
        print("Executou set_velocidade")
        self._velocidade = velocidade
    def del_velocidade(self):
        print("Executou del_velocidade")
        del self._velocidade
    velocidade = property(get_velocidade, set_velocidade, del_velocidade, 
                          "Propriedade de velocidade do veículo!")
    
a = Arrancada(100,120)
print(a.velocidade)


# In[50]:


a.velocidade = 200
print(a.velocidade)


# In[51]:


del a.velocidade


# ### Descritores:
# - `__get__` => retorna o valor do atributo
# - `__set__` => informa o valor do atributo, não tem retorno
# - `__delete__` => controla a exclusão 

# In[52]:


class RevelarAcesso(object):
    def __init__(self, initval = None, nome = "val"):
        self.val = initval
        self.nome = nome
    def __get__(self, obj, objtype):
        print("Recuperando",self.nome)
        return self.val
    def __set__(self, obj, val):
        print("Atualizando",self.nome)
        self.val = val


# In[53]:


class MinhaClasse(object):
    x = RevelarAcesso(10, "var 'x'")
    y = 5
    
m = MinhaClasse()
print("x: ",m.x)


# In[54]:


m.x = 20
print("x: ",m.x)


# In[55]:


print("y: ",m.y)


# In[56]:


m.y = 22
print("y: ",m.y)


# In[57]:


class MeuDescritor(object):
    def __init__(self, valor_inicial = None, nome = "my_var"):
        self.valor = valor_inicial
        self.nome = nome
    def __get__(self, instancia, proprietario):
        print("Obtendo: ",self.nome)
        return self.valor
    def __set__(self, instancia, valor):
        print(f"Atribuindo {valor} a {self.nome}");
        self.valor = valor
    
class MinhaClasse(object):
    descritor = MeuDescritor(valor_inicial = '10', nome = "dinheiro")
    normal = 20

classe = MinhaClasse()
print(classe.descritor) #executa o get para imprimrir o valor da linha "obtendo"


# In[58]:


print(classe.normal) #não é descritor


# In[59]:


classe.descritor = 200 #executa o __set__
print(classe.descritor)


# Não permitindo valor negativo:

# In[60]:


class Carro(object):
    def __init__(self, marca, modelo, valor):
        self.modelo = modelo
        self.marca = marca
        self.valor = valor
        if valor < 0:
            raise ValueError("O valor do carro não pode ser negativo")
        else:
            self.valor
    def __str__(self):
        return f"O carro de marca {self.marca} de modelo {self.modelo}, no valor de R${self.valor:,.2f}"


# In[61]:


yaris = Carro("Toyota", "Yaris", 73565.85)
print(yaris)


# In[62]:


yaris = Carro("Toyota", "Yaris", -65.85)
print(yaris)


# Criando descritor que reaproveita os valores negativos:

# In[63]:


class DescritorValor(object):
    def __init__(self):
        self.valor = 0
    def __get__(self, instancia, proprietario):
        return self.valor
    def __set__(self, instancia, valor):
        if valor < 0:
            raise ValueError("O valor do carro não pode ser negativo")
        else:
            self.valor = valor
    def __delete__(self, instancia):
        del self.valor


# In[64]:


class Carro(object):
    valor = DescritorValor()
    def __init__(self, marca, modelo, valor):
        self.modelo = modelo
        self.marca = marca
        self.valor = valor
    def __str__(self):
        return f"O carro de marca {self.marca} de modelo {self.modelo}, no valor de R${self.valor:,.2f}"


# In[65]:


yaris = Carro("Toyota", "Yaris", 73565.85)
print(yaris)


# In[66]:


yaris2 = Carro("Toyota", "Yaris", -65.85)
print(yaris2)


# Acima criamos um descritor que valida se o valor é negativo ou não.

# In[67]:


hb20 = Carro("Hyundai", "HB20", 53500)
print(hb20)


# In[68]:


print(yaris)


# Ficou o valor de 53.500, sendo que esse não era o valor correto, isso acontece por casua que valor é uma propriedade da classe Carro. Abaixo como solucionar:

# In[69]:


class DescritorValor(object):
    def __init__(self):
        self.valor = {}
    def __get__(self, instancia, proprietario):
        return self.valor[instancia]
    def __set__(self, instancia, valor):
        if valor < 0:
            raise ValueError("O valor do carro não pode ser negativo")
        else:
            self.valor[instancia] = valor
    def __delete__(self, instancia):
        del self.valor[instancia]


# In[70]:


class Carro(object):
    valor = DescritorValor()
    def __init__(self, marca, modelo, valor):
        self.modelo = modelo
        self.marca = marca
        self.valor = valor
    def __str__(self):
        return f"O carro de marca {self.marca} de modelo {self.modelo}, no valor de R${self.valor:,.2f}"


# In[71]:


yaris = Carro("Toyota", "Yaris", 73565.85)
print(yaris)


# In[72]:


hb20 = Carro("Hyundai", "HB20", 53500)
print(hb20)


# ### Sobrecarga de operadores:

# In[73]:


class MinhaString(str):
    def __sub__(self, outro):
        print("self: ",self)
        print("outro: ",outro)
        sub = self.replace(outro, "")
        return f"Resultado de '{self}' - '{outro}' é {sub}"

s1 = MinhaString("Olá, mundo cruel!")
s2 = 'cruel'
s3 = s1 - s2
print(s3)


# In[74]:


class MinhaString(str):
    def __add__(self, outro):
        print("self: ",self)
        print("outro: ",outro)
        return f"Resultado de '{self}' + '{outro}' é {self} {outro}"

s1 = MinhaString("Olá, mundo")
s2 = 'cruel!'
s3 = s1 + s2
print(s3)


# ### Metaclasse:
# É a classe de outra classe, ou seja, classe é uma instância da metaclasse.

# In[75]:


type(int) #type é uma metaclasse
# int é uma classe da classe do tipo type


# In[76]:


class MinhaClasse(object):
    pass

print(isinstance(MinhaClasse, type)) # saber se MinhaClasse é uma instancia de type


# In[77]:


def meu_metodo(self):
    return 1

MinhaClasse = type("MinhaClasse", (object,), {"metodo": meu_metodo})

instancia = MinhaClasse()
x = instancia.metodo()
print(x)


# In[78]:


class MinhaClasse:
    def metodo(self):
        return 1
    
instancia = MinhaClasse()
x = instancia.metodo()
print(x)


# In[79]:


def inicia_pessoa(self, nome, sobrenome):
    self.nome = nome
    self.sobrenome = sobrenome

Pessoa = type("Pessoa", (object,), {"__init__": inicia_pessoa, "a": "Teste", "b": 10})
print("type(Pessoa):",type(Pessoa))
print("vars(Pessoa):", vars(Pessoa))

pes = Pessoa("Katharine", "Pires")

print("type(pes):",type(pes))


# In[80]:


print(pes.nome)
print(pes.sobrenome)
print(pes.a)
print(pes.b)


# Criando Metaclasse como se fosse `type()`:

# In[81]:


class Metaclasse(type):
    pass
MinhaMetaclasse = Metaclasse("MinhaMetaclasse", (), {})
instancia = MinhaMetaclasse()
print(type(instancia))


# `instancia` é do tipo `MinhaMetaclasse`.

# Usando o `metaclass` para criar a metaclasse:

# In[82]:


class Metaclasse(type):
    pass

class MinhaMetaclasse(metaclass = Metaclasse):
    pass

instancia = MinhaMetaclasse()
print(type(instancia))


# Usando `__new__`:

# In[83]:


def fabrica_funcoes(nome_metodo, retorno):
    def metodo_criado(self):
        return retorno
    
    metodo_criado.__name__ = nome_metodo
    return metodo_criado

class MetaClasse(type):
    def __new__(mcs, nome, bases, atributos):
        for nome, retorno in (("metodo1", "olá"),("metodo3", 6+99),("metodo4", str(2021-1999)),("metodo2", "oxi")):
            atributos[nome] = fabrica_funcoes(nome, retorno)
        return super().__new__(mcs, nome, bases, atributos)

class Classe(metaclass = MetaClasse):
    pass

print("vars(Classe):",vars(Classe))                             


# In[84]:


mc = Classe()
print(mc.metodo1())
print(mc.metodo2())
print(mc.metodo3())                              
print(mc.metodo4()) 


# ### MetaSingleton:

# In[85]:


class MetaSingleton(type):
    _instancias = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:  
            cls._instancias[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instancias[cls]
class Logger(metaclass = MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1)
print(logger2)


# ### Clase base abstrata:

# In[86]:


from abc import ABCMeta, abstractmethod

class Carro(metaclass = ABCMeta):
    @abstractmethod
    def ligar(self):
        pass
    
class Clio(Carro):
    def __init__(self):
        print("Vou implementar o ligar.")
    def ligar(self):
        print("Uhu!! O Clio ligou!")
        
clio = Clio()
clio.ligar()


# In[87]:


class Carro(metaclass = ABCMeta):
    @abstractmethod
    def ligar(self):
        pass
    
class Clio(Carro):
    def __init__(self):
        print("Não vou implementar o ligar.")
        
clio = Clio()


# Como não foi implementado nenhuma instância, dá erro de que não há metodos abstratos. A seguir vamos ver um exemplo de propriedade abstrata implementada:

# In[88]:


class Carro(metaclass = ABCMeta):
    @property
    @abstractmethod
    def valor(self):
        return "Retorno do valor"
    
    @abstractmethod
    def ligar(self):
        print("Método de ligar da classe Carro implementado")
        pass
    
class Clio(Carro):
    @property
    def valor(self):
        return "Propriedade concreta"
    def ligar(self):
        print("Uhu!! O que Clio pegou!")

clio = Clio()
clio.ligar()
print(clio.valor)


# In[89]:


class Carro(metaclass = ABCMeta):
    @property
    @abstractmethod
    def valor(self):
        return "Retorno do valor"
    
    @abstractmethod
    def ligar(self):
        print("Método de ligar da classe Carro implementado")
        pass
    
class Clio(Carro):
    def ligar(self):
        print("Uhu!! O que Clio pegou!")

clio = Clio()
clio.ligar()
print(clio.valor)


# Dá erro se não há implementação da propriedade abstrata.

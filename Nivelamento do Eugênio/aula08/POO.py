'''

Classes e Objetos

Na programação orientada a objetos, um programa é composto por objetos que se comunicam Um objeto contém dados e ações (métodos) métodos - funções e procedimentos

Classe - define a estrutura do objeto

Objeto - dizemos que um objeto é uma instância de uma classe

'''

# exemplo de classe com um único dado
class UmaClasse:
    x = 5

o1 = UmaClasse() # o1 é um objeto da classe
print(o1.x)
print('---------------')
# ================================

class Pessoa :
    def __init__(self, nome, altura, peso):
        #__init__ é executado toda vez que você cria um objeto
        self.nome = nome
        # self indica que é do próprio objeto
        self.altura = altura
        self.peso = peso

p1 = Pessoa('José', 1.7, 70)
print(f'{p1.nome} tem {p1.altura}m e {p1.peso}kg')
print('---------------')

# ================================

class Carro:
    def __init__(self, marca, modelo, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa

c1 = Carro('VW', 'Gol', 'Branco', 'ABC-1234')
print(f'{c1.marca} {c1.modelo} {c1.cor} {c1.placa}')
print('---------------')

class CarroNovo:
    def __init__(self, placa, velocidade):
        self.velocidade = velocidade
        self.placa = placa

    def __str__(self):
        return f'velocidade:{self.velocidade} placa:{self.placa}'

    def acelerar(self,quanto):
        self.velocidade += quanto

cn = CarroNovo('CCC1234', 0 )

cn.acelerar(30)

print(cn.velocidade)
print("--------------")
print(cn)
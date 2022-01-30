class Pessoa:
    olhos = 2
    def __init__(self,*filhos, nome=None, idade=27):
        self.nome = nome
        self.idade = 27
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self}'

    @staticmethod
    def metodo_estatico():
        return 27

    @classmethod
    def nome_e_atributos_class(cls):
        return f'{cls} - olhos{cls.olhos}'

if __name__ == '__main__' :
    cicero = Pessoa(nome='Cicero')
    renzo = Pessoa(cicero, nome='renzo')
    print(Pessoa.cumprimentar(cicero))
    print(id(cicero))
    print(renzo.cumprimentar())
    print(renzo.nome)
    print(renzo.idade)
    cicero.sobrenome = 'Soares'
    print(cicero.sobrenome)
    for filho in cicero.filhos:
        print(cicero.filhos)
    print(cicero. __dict__)
    print(renzo. __dict__)
    print(Pessoa.olhos)
    print(cicero.olhos)
    print(Pessoa.metodo_estatico(), cicero.metodo_estatico())
    print(Pessoa.nome_e_atributos_class(), cicero.metodo_estatico())
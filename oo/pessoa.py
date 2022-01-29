class Pessoa:
    def __ini__(self, nome=None, idade=27):
        self.nome = nome
        self.idade = 27

    def cumprimentar(self):
        return f'Olá {self}'

if __name__ == '__main__' :
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Cicero'
    print(p.nome)

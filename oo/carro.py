NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
        rotacao_a_direita_dct = {
            NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE
        }
        rotacao_a_esquerda_dct = {
            NORTE:OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE
        }
        def __init__(self):
            self.valor = NORTE

class Motor:
        def __init__(self):
            self.velocidade = 0

        def acelerar(self):
            self.velocidade += 1

        def frear(self):
            self.velocidade -=2
            self.velocidade = max(0, self.velocidade)


            motor = Motor()
            motor.velocidade
            0
            motor.acelerar()
            motor.velocidade
            1
            motor.acelerar()
            motor.velocidade
            2
            motor.acelerar()
            motor.velocidade
            3
            motor.frear()
            motor.velocidade
            1
            motor.frear()
            motor.velocidade
            0
            direcao = Direcao()
            direcao.valor
            'Norte'
            direcao.girar_a_direita()
            direcao.valor
            'Leste'
            direcao.girar_a_direita()
            direcao.valor
            'Sul'
            direcao.girar_a_direita()
            direcao.valor
            'Oeste'
            direcao.girar_a_direita()
            direcao.valor
            'Norte'
            direcao.girar_a_esquerda()
            direcao.valor
            'Norte'
            direcao.girar_a_esquerda()
            direcao.valor
            'Oeste'
            direcao.girar_a_esquerda()
            direcao.valor
            'Sul'
            direcao.girar_a_esquerda()
            direcao.valor
            'Leste'
            direcao.girar_a_esquerda()
            direcao.valor
            'Norte'

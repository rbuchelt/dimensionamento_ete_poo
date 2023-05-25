class PerdaCargaGradeamento:
    def __init__(self, v, v0):
        """
        Cálculo da perda de carga no gradeamento
        :param v: Velocidade de saída do efluente no gradeamento
        :param v0: Velocidade de entrada do efluente no gradeamento
        """
        self.v = v
        self.v0 = v0

    def calcular_perda_carga(self):
        dH = 1.43 * ((self.v ** 2) - (self.v0 ** 2)) / (2 * 9.81)
        return dH


class SecaoTransversalGradeamento:
    def __init__(self, Qmax, v, a, t):
        """
        Cálculo da seção transversal do gradeamento
        :param Qmax: Vazão máxima do efluente
        :param v: Velocidade de entrada do efluente
        :param a: espaçamento entre as barras
        :param t: espessura das barras
        """
        self.Qmax = Qmax
        self.v = v
        self.a = a
        self.t = t

    def calcular_espacamento(self):
        """
        Au: Área útil do gradeamento
        S: Área da seção transversal do canal até o nível da água.
        """

        Qmax = self.Qmax / 1000
        Au = Qmax / self.v

        a = self.a/100
        t = self.t/100

        S = Au * (a + t)/a

        return S

class Desarenador:
    def __init__(self, Q, h):
        """
        :param Q: Vazão do projeto
        :param h: Altura da calha do desarenador
        """
        self.Q = Q
        self.h = h

    def calculo_desarenador(self):

        """
        O cálculo do desarenador retorna tanto a largura quando o comprimento do desarenador

        O comprimento da caixa de areia (L) é determinado considerando-se a velocidade dos efluentes de 0,3 m/s e a
        velocidade de sedimentação de 2cm/s.

        Recimenda-se L = 22.5*H ou 25*H

        O código retorna os dois parâmetros recomendados para L e o valor a ser utilizado deve ser escolhido pelo
        projetista
        """

        Q = self.Q / 1000

        b = Q / (0.3*self.h)

        L1 = 22.5 * b

        L2 = 25 * b

        return b, L1, L2

class TanqueEqualizacao:
    def __init__(self, V1, V2):
        """
        :param V1: Menor volume diário no tanque
        :param V2: Maior volume diário no tanque
        """
        self.V1 = V1
        self.V2 = V2

    def calculo_volume_equalizacao(self):
        """
        O calculo do volume do tanque de equalização é obtido por V1 e V2 onde a diferença entre os dois é o volume
        do tanque.

        Os valores de V1 e V2 é obtido pelas maiores diferenças de entrada e saídas acumuladas durante as 24 horas do
        dia.

        O cálculo ainda considera uma margem de segurança de 25%, portanto multiplica-se o volume obtido por 1.25.
        """

        Veq = (self.V2 - self.V1) * 1.25

        return Veq


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
        self.Q = Q
        self.h = h

    def calculo_desarenador(self):

        Q = self.Q / 1000

        b = self.Q / (0.3*self.h)

        L1 = 22.5 * b

        L2 = 25 * b

        return b, L1, L2

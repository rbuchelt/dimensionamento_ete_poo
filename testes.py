import unittest
from tratamento_preliminar import *

class TestPerdaCargaGradeamento(unittest.TestCase):
    def test_calcular_perda_carga(self):
        # Caso de teste 1
        v = 10
        v0 = 5
        perda = PerdaCargaGradeamento(v, v0)
        resultado = perda.calcular_perda_carga()
        self.assertAlmostEqual(resultado, 5.466, places=3)

        # Caso de teste 2
        v = 8
        v0 = 2
        perda = PerdaCargaGradeamento(v, v0)
        resultado = perda.calcular_perda_carga()
        self.assertAlmostEqual(resultado, 4.373, places=3)


class TestSecaoTransversalGradeamento(unittest.TestCase):
    def test_calcular_espacamento(self):
        # Caso de teste 1
        Qmax = 2000
        v = 10
        a = 50
        t = 20
        gradeamento = SecaoTransversalGradeamento(Qmax, v, a, t)
        resultado = gradeamento.calcular_espacamento()
        self.assertAlmostEqual(resultado, 0.28, places=2)

        # Caso de teste 2
        Qmax = 1500
        v = 8
        a = 40
        t = 15
        gradeamento = SecaoTransversalGradeamento(Qmax, v, a, t)
        resultado = gradeamento.calcular_espacamento()
        self.assertAlmostEqual(resultado, 0.2578, places=2)

class TestDesarenador(unittest.TestCase):
    def test_calcular_desarenador(self):
        # Caso de teste 1
        Q = 120
        h = 1

        desarenador = Desarenador(Q, h)
        resultado = desarenador.calculo_desarenador()
        self.assertAlmostEqual(resultado, (0.4,9.0,10.0), places=2)

        # Caso de teste 2
        Q = 250
        h = 0.5
        desarenador = Desarenador(Q, h)
        resultado = desarenador.calculo_desarenador()
        self.assertAlmostEqual(resultado, (1.6666666666666667, 37.5, 41.66666666666667), places=2)


if __name__ == '__main__':
    unittest.main()


"""
Testes unitários para a Calculadora de IMC.
Valida todas as regras de negócio definidas.
"""

import pytest
from src.calculadora_imc import CalculadoraIMC


class TestValidacoes:
    """Testes para validação de entradas (RN01 e RN02)."""
    
    def setup_method(self):
        """Configura a calculadora antes de cada teste."""
        self.calc = CalculadoraIMC()
    
    def test_peso_zero_deve_lancar_erro(self):
        """RN01: Peso zero deve lançar ValueError."""
        with pytest.raises(ValueError, match="Peso deve ser maior que zero"):
            self.calc.calcular_imc(peso=0, altura=1.75)
    
    def test_peso_negativo_deve_lancar_erro(self):
        """RN01: Peso negativo deve lançar ValueError."""
        with pytest.raises(ValueError, match="Peso deve ser maior que zero"):
            self.calc.calcular_imc(peso=-10, altura=1.75)
    
    def test_altura_zero_deve_lancar_erro(self):
        """RN02: Altura zero deve lançar ValueError."""
        with pytest.raises(ValueError, match="Altura deve ser maior que zero"):
            self.calc.calcular_imc(peso=70, altura=0)
    
    def test_altura_negativa_deve_lancar_erro(self):
        """RN02: Altura negativa deve lançar ValueError."""
        with pytest.raises(ValueError, match="Altura deve ser maior que zero"):
            self.calc.calcular_imc(peso=70, altura=-1.75)


class TestCalculoIMC:
    """Testes para o cálculo do IMC (RN03)."""
    
    def setup_method(self):
        """Configura a calculadora antes de cada teste."""
        self.calc = CalculadoraIMC()
    
    def test_calculo_imc_correto(self):
        """RN03: Verifica se o cálculo do IMC está correto."""
        # IMC = 70 / (1.75^2) = 70 / 3.0625 = 22.857... ≈ 22.86
        imc = self.calc.calcular_imc(peso=70, altura=1.75)
        assert imc == 22.86
    
    def test_imc_arredondamento(self):
        """RN03: Verifica se o IMC é arredondado para 2 casas."""
        # IMC = 80 / (1.80^2) = 80 / 3.24 = 24.691... ≈ 24.69
        imc = self.calc.calcular_imc(peso=80, altura=1.80)
        assert imc == 24.69


class TestClassificacaoIMC:
    """Testes para classificação do IMC (RN04)."""
    
    def setup_method(self):
        """Configura a calculadora antes de cada teste."""
        self.calc = CalculadoraIMC()
    
    def test_classificacao_abaixo_peso(self):
        """RN04: IMC < 18.5 deve ser 'Abaixo do peso'."""
        assert self.calc.classificar_imc(17.0) == "Abaixo do peso"
        assert self.calc.classificar_imc(18.4) == "Abaixo do peso"
    
    def test_classificacao_peso_normal(self):
        """RN04: IMC entre 18.5 e 24.9 deve ser 'Peso normal'."""
        assert self.calc.classificar_imc(18.5) == "Peso normal"
        assert self.calc.classificar_imc(22.0) == "Peso normal"
        assert self.calc.classificar_imc(24.9) == "Peso normal"
    
    def test_classificacao_sobrepeso(self):
        """RN04: IMC entre 25.0 e 29.9 deve ser 'Sobrepeso'."""
        assert self.calc.classificar_imc(25.0) == "Sobrepeso"
        assert self.calc.classificar_imc(27.5) == "Sobrepeso"
        assert self.calc.classificar_imc(29.9) == "Sobrepeso"
    
    def test_classificacao_obesidade_grau_1(self):
        """RN04: IMC entre 30.0 e 34.9 deve ser 'Obesidade Grau I'."""
        assert self.calc.classificar_imc(30.0) == "Obesidade Grau I"
        assert self.calc.classificar_imc(32.0) == "Obesidade Grau I"
        assert self.calc.classificar_imc(34.9) == "Obesidade Grau I"
    
    def test_classificacao_obesidade_grau_2(self):
        """RN04: IMC entre 35.0 e 39.9 deve ser 'Obesidade Grau II'."""
        assert self.calc.classificar_imc(35.0) == "Obesidade Grau II"
        assert self.calc.classificar_imc(37.0) == "Obesidade Grau II"
        assert self.calc.classificar_imc(39.9) == "Obesidade Grau II"
    
    def test_classificacao_obesidade_grau_3(self):
        """RN04: IMC >= 40.0 deve ser 'Obesidade Grau III'."""
        assert self.calc.classificar_imc(40.0) == "Obesidade Grau III"
        assert self.calc.classificar_imc(45.0) == "Obesidade Grau III"
    
    def test_limites_das_faixas(self):
        """RN04: Testa valores exatos nos limites das faixas."""
        # Testa os valores limítrofes (boundary values)
        assert self.calc.classificar_imc(18.49) == "Abaixo do peso"
        assert self.calc.classificar_imc(18.5) == "Peso normal"
        assert self.calc.classificar_imc(24.99) == "Peso normal"
        assert self.calc.classificar_imc(25.0) == "Sobrepeso"
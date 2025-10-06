"""
Calculadora de IMC (Índice de Massa Corporal)
Implementa cálculo e classificação do IMC conforme padrão OMS.
"""

class CalculadoraIMC:
    """Classe responsável por calcular e classificar o IMC."""
    
    def calcular_imc(self, peso: float, altura: float) -> float:
        """
        Calcula o Índice de Massa Corporal (IMC).
        
        Args:
            peso (float): Peso em quilogramas
            altura (float): Altura em metros
            
        Returns:
            float: IMC calculado (arredondado para 2 casas decimais)
            
        Raises:
            ValueError: Se peso ou altura forem <= 0
        """
        # RN01: Validação de Peso
        if peso <= 0:
            raise ValueError("Peso deve ser maior que zero")
        
        # RN02: Validação de Altura
        if altura <= 0:
            raise ValueError("Altura deve ser maior que zero")
        
        # RN03: Cálculo do IMC
        imc = peso / (altura ** 2)
        return round(imc, 2)
    
    def classificar_imc(self, imc: float) -> str:
        """
        Classifica o IMC conforme tabela da OMS.
        
        Args:
            imc (float): Valor do IMC
            
        Returns:
            str: Classificação do IMC
        """
        # RN04: Classificação do IMC
        if imc < 18.5:
            return "Abaixo do peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        elif imc < 35:
            return "Obesidade Grau I"
        elif imc < 40:
            return "Obesidade Grau II"
        else:
            return "Obesidade Grau III"
    
    def calcular_e_classificar(self, peso: float, altura: float) -> dict:
        """
        Calcula o IMC e retorna com sua classificação.
        
        Args:
            peso (float): Peso em quilogramas
            altura (float): Altura em metros
            
        Returns:
            dict: Dicionário com IMC e classificação
        """
        imc = self.calcular_imc(peso, altura)
        classificacao = self.classificar_imc(imc)
        
        return {
            "imc": imc,
            "classificacao": classificacao
        }
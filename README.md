# 📊 Calculadora de IMC - Projeto de Testes Unitários

## 📝 Sobre o Projeto

Este projeto implementa uma **Calculadora de Índice de Massa Corporal (IMC)** com uma suíte completa de testes unitários automatizados. O objetivo é demonstrar boas práticas de desenvolvimento orientado a testes (TDD) e validação de regras de negócio.

### 🎯 Objetivo Educacional

Demonstrar a aplicação de testes unitários para validar regras de negócio, garantindo:
- ✅ Alta cobertura de código
- ✅ Validação de entradas
- ✅ Correção dos cálculos
- ✅ Classificações conforme padrão OMS

---

## 🏗️ Estrutura do Projeto

```
imc_calculator/
│
├── src/
│   ├── __init__.py
│   └── calculadora_imc.py      
│
├── tests/
│   ├── __init__.py
│   └── test_calculadora_imc.py
│
├── requirements.txt             
└── README.md                 
```

---

## 📋 Regras de Negócio Testadas

### RN01 - Validação de Peso
**Descrição:** O peso deve ser um número positivo maior que zero.

**Critérios de Aceitação:**
- ✓ Peso = 0 → Deve lançar ValueError
- ✓ Peso < 0 → Deve lançar ValueError
- ✓ Peso > 0 → Deve ser aceito

**Testes Implementados:**
- `test_peso_zero_deve_lancar_erro`
- `test_peso_negativo_deve_lancar_erro`

---

### RN02 - Validação de Altura
**Descrição:** A altura deve ser um número positivo maior que zero.

**Critérios de Aceitação:**
- ✓ Altura = 0 → Deve lançar ValueError
- ✓ Altura < 0 → Deve lançar ValueError
- ✓ Altura > 0 → Deve ser aceita

**Testes Implementados:**
- `test_altura_zero_deve_lancar_erro`
- `test_altura_negativa_deve_lancar_erro`

---

### RN03 - Cálculo do IMC
**Descrição:** O IMC é calculado pela fórmula: **IMC = peso / (altura²)**

**Critérios de Aceitação:**
- ✓ Resultado deve ser arredondado para 2 casas decimais
- ✓ Fórmula aplicada corretamente

**Testes Implementados:**
- `test_calculo_imc_correto`
- `test_imc_arredondamento`

---

### RN04 - Classificação do IMC (OMS)
**Descrição:** O IMC deve ser classificado conforme tabela da Organização Mundial da Saúde.

**Tabela de Classificação:**

| Faixa de IMC | Classificação |
|--------------|---------------|
| < 18.5       | Abaixo do peso |
| 18.5 - 24.9  | Peso normal    |
| 25.0 - 29.9  | Sobrepeso      |
| 30.0 - 34.9  | Obesidade Grau I |
| 35.0 - 39.9  | Obesidade Grau II |
| ≥ 40.0       | Obesidade Grau III |

**Testes Implementados:**
- `test_classificacao_abaixo_peso`
- `test_classificacao_peso_normal`
- `test_classificacao_sobrepeso`
- `test_classificacao_obesidade_grau_1`
- `test_classificacao_obesidade_grau_2`
- `test_classificacao_obesidade_grau_3`
- `test_limites_das_faixas` (testa valores limítrofes)

---

## 🚀 Como Executar

### 1. Clonar o Repositório
```bash
git clone <seu-repositorio>
cd imc_calculator
```

### 2. Criar Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar os Testes
```bash
# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=src --cov-report=html

# Executar com verbose
pytest -v
```

---

## 📊 Cobertura de Testes

O projeto visa **100% de cobertura** das funcionalidades críticas:

- ✅ Validações de entrada: 100%
- ✅ Cálculo do IMC: 100%
- ✅ Classificações: 100%
- ✅ Casos limite (edge cases): 100%

Para visualizar o relatório de cobertura:
```bash
pytest --cov=src --cov-report=html
open htmlcov/index.html
```

---

## 🧪 Exemplo de Uso

```python
from src.calculadora_imc import CalculadoraIMC

# Criar instância da calculadora
calc = CalculadoraIMC()

# Calcular IMC
imc = calc.calcular_imc(peso=70, altura=1.75)
print(f"IMC: {imc}")  # IMC: 22.86

# Obter classificação
classificacao = calc.classificar_imc(imc)
print(f"Classificação: {classificacao}")  # Classificação: Peso normal
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **pytest** - Framework de testes
- **pytest-cov** - Relatório de cobertura

---

## 📈 Métricas de Qualidade

| Métrica | Valor |
|---------|-------|
| Cobertura de Código | 100% |
| Testes Implementados | 13 |
| Regras de Negócio | 4 |
| Tempo de Execução | < 1s |

---

## 👥 Autor

Desenvolvido por Heleno Nogueira para estudo de testes unitários e qualidade de software.

from src.calculadora_imc import CalculadoraIMC

# Criar instância da calculadora
calc = CalculadoraIMC()

# TESTE 1: Calcular seu IMC
print("=" * 50)
print("TESTE 1: Calculando IMC")
print("=" * 50)

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

try:
    resultado = calc.calcular_e_classificar(peso, altura)
    print(f"\n✅ Resultado:")
    print(f"   IMC: {resultado['imc']}")
    print(f"   Classificação: {resultado['classificacao']}")
except ValueError as e:
    print(f"\n❌ Erro: {e}")

# TESTE 2: Vários exemplos
print("\n" + "=" * 50)
print("TESTE 2: Exemplos de diferentes classificações")
print("=" * 50)

exemplos = [
    (50, 1.70, "Abaixo do peso"),
    (70, 1.75, "Peso normal"),
    (85, 1.75, "Sobrepeso"),
    (95, 1.75, "Obesidade Grau I"),
    (110, 1.75, "Obesidade Grau II"),
    (130, 1.75, "Obesidade Grau III"),
]

for peso, altura, esperado in exemplos:
    resultado = calc.calcular_e_classificar(peso, altura)
    status = "✅" if resultado['classificacao'] == esperado else "❌"
    print(f"{status} Peso: {peso}kg, Altura: {altura}m → IMC: {resultado['imc']} ({resultado['classificacao']})")

# TESTE 3: Testando erros
print("\n" + "=" * 50)
print("TESTE 3: Testando validações de erro")
print("=" * 50)

testes_erro = [
    (0, 1.70, "Peso zero"),
    (-10, 1.70, "Peso negativo"),
    (70, 0, "Altura zero"),
    (70, -1.70, "Altura negativa"),
]

for peso, altura, descricao in testes_erro:
    try:
        calc.calcular_imc(peso, altura)
        print(f"❌ {descricao}: DEVERIA ter dado erro!")
    except ValueError as e:
        print(f"✅ {descricao}: Erro capturado corretamente - '{e}'")
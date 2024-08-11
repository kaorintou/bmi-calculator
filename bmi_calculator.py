def calculate_bmi(weight, height):
    """Calcula o IMC (Índice de Massa Corporal) dado o peso em kg e altura em metros."""
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    """Retorna a categoria do IMC dado o valor do IMC."""
    if bmi < 18.5:
        return "Baixo peso"
    elif 18.5 <= bmi <= 24.9:
        return "Peso normal"
    elif 25 <= bmi <= 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    print("Calculadora de IMC")
    while True:
        try:
            weight = float(input("Digite seu peso em kg: "))
            height = float(input("Digite sua altura em metros: "))
            bmi = calculate_bmi(weight, height)
            category = categorize_bmi(bmi)
            print(f"Seu IMC é {bmi:.2f}. Categoria: {category}")
        except ValueError:
            print("Por favor, insira um valor válido para peso e altura.")
        
        another = input("Deseja calcular novamente? (s/n): ").strip().lower()
        if another != 's':
            break

if __name__ == "__main__":
    main()

def calcular_cartucho():
    valor = float(input("Valor do cartucho: "))
    qtd = int(input("Quantidade usada: "))
    return valor * qtd


def calcular_tinta():
    valor = float(input("Valor da tinta: "))
    ml_total = float(input("ML do frasco: "))
    ml_usado = float(input("ML usado: "))
    return (valor / ml_total) * ml_usado


def calcular_luva():
    valor = float(input("Valor da caixa de luvas: "))
    qtd = int(input("Quantidade na caixa: "))
    usado = int(input("Quantidade usada: "))
    return (valor / qtd) * usado


def calcular_mascara():
    valor = float(input("Valor da caixa de máscaras: "))
    qtd = int(input("Quantidade na caixa: "))
    usado = int(input("Quantidade usada: "))
    return (valor / qtd) * usado


def calcular_batoque():
    valor = float(input("Valor do pacote: "))
    qtd = int(input("Quantidade no pacote: "))
    usado = int(input("Quantidade usada: "))
    return (valor / qtd) * usado


def calcular_isufilme():
    valor = float(input("Valor do rolo: "))
    metros = float(input("Metros no rolo: "))
    usado = float(input("CM usado: "))
    return (valor / (metros * 100)) * usado


def calcular_lamina():
    valor = float(input("Valor do pacote: "))
    qtd = int(input("Quantidade no pacote: "))
    usado = int(input("Quantidade usada: "))
    return (valor / qtd) * usado


def calcular_papel_hectografico():
    valor = float(input("Valor do pacote: "))
    qtd = int(input("Quantidade de folhas: "))
    usado = int(input("Folhas usadas: "))
    return (valor / qtd) * usado


def calcular_transfer():
    valor = float(input("Valor do produto: "))
    ml_total = float(input("ML total: "))
    ml_usado = float(input("ML usado: "))
    return (valor / ml_total) * ml_usado


def calcular_vaselina():
    valor = float(input("Valor do pote: "))
    ml_total = float(input("ML total: "))
    ml_usado = float(input("ML usado: "))
    return (valor / ml_total) * ml_usado


def calcular_bandagem():
    valor = float(input("Valor do rolo: "))
    total = float(input("CM total: "))
    usado = float(input("CM usado: "))
    return (valor / total) * usado


def calcular_palito():
    valor = float(input("Valor do pacote: "))
    qtd = int(input("Quantidade: "))
    usado = int(input("Quantidade usada: "))
    return (valor / qtd) * usado


def calcular_alcool():
    valor = float(input("Valor: "))
    ml_total = float(input("ML total: "))
    borrifadas = int(input("Quantidade de borrifadas: "))
    usado = borrifadas * 1.2
    return (valor / ml_total) * usado


def main():
    print("===== CALCULADORA DE CUSTO =====")

    print("1 - Custo total")
    print("2 - Cartucho")
    print("3 - Tinta")
    print("4 - Luva")
    print("5 - Máscara")
    print("6 - Batoque")
    print("7 - Insulfilme")
    print("8 - Lâmina")
    print("9 - Papel hectográfico")
    print("10 - Transfer")
    print("11 - Vaselina")
    print("12 - Bandagem")
    print("13 - Palito")
    print("14 - Álcool")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        total = 0

        total += calcular_cartucho()
        total += calcular_tinta()
        total += calcular_luva()
        total += calcular_mascara()
        total += calcular_batoque()
        total += calcular_isufilme()
        total += calcular_lamina()
        total += calcular_papel_hectografico()
        total += calcular_transfer()
        total += calcular_vaselina()
        total += calcular_bandagem()
        total += calcular_palito()
        total += calcular_alcool()

        lucro = total * 2
        preco_final = total + lucro

        print("\n===== RESULTADO =====")
        print("CUSTO: R$", round(total, 2))
        print("LUCRO: R$", round(lucro, 2))
        print("PREÇO FINAL: R$", round(preco_final, 2))

    elif opcao == 2:
        print("Custo:", calcular_cartucho())

    elif opcao == 3:
        print("Custo:", calcular_tinta())

    elif opcao == 4:
        print("Custo:", calcular_luva())

    elif opcao == 5:
        print("Custo:", calcular_mascara())

    elif opcao == 6:
        print("Custo:", calcular_batoque())

    elif opcao == 7:
        print("Custo:", calcular_isufilme())

    elif opcao == 8:
        print("Custo:", calcular_lamina())

    elif opcao == 9:
        print("Custo:", calcular_papel_hectografico())

    elif opcao == 10:
        print("Custo:", calcular_transfer())

    elif opcao == 11:
        print("Custo:", calcular_vaselina())

    elif opcao == 12:
        print("Custo:", calcular_bandagem())

    elif opcao == 13:
        print("Custo:", calcular_palito())

    elif opcao == 14:
        print("Custo:", calcular_alcool())

    else:
        print("Opção inválida")


if __name__ == "__main__":
    main()

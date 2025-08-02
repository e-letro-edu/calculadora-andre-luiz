def porcentagem_em_decimal(I):
    return  float(I/100)


def calculo_emprestimo():
    VP=float(input("Digite valor presente:R$ "))
    I=float(input("Digite a taxa: "))
    N=int(input("Digite o intervalo: "))

    taxa_decimal = porcentagem_em_decimal(I)

    VF = VP*(1+taxa_decimal)**N
    try:
        print(f"Valor final do emprestimo: R$ ",round(VF,2))
        print(f"Valor da parcela R$ ", round(VF/N,2))
    except ZeroDivisionError:
        return "Periodo não pode ser zero"
   


print("Efetuar simulação \n")
calculo_emprestimo()




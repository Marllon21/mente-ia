def calculadora():
    # Operações básicas
    soma = 5 + 3
    subtracao = 10 - 4
    multiplicacao = 7 * 2
    divisao = 8 / 2
    
    return {
        "soma": soma,
        "subtracao": subtracao,
        "multiplicacao": multiplicacao,
        "divisao": divisao
    }

resultados = calculadora()
print(resultados)
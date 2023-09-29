def dividir(dividendo, divisor):
    # print(divisor.resultado)
    return dividendo / divisor


def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f"O resultado da divisao de 10 por {divisor} é {resultado}")
    
# try:
#     testa_divisao(0)
# except AttributeError as E:
#     print(E.__class__.__bases__)
# except ZeroDivisionError as E:
#         print(E.__class__.__bases__)

# try:
#     testa_divisao(0)
# except Exception as E:
#     print(E.__class__)

try:
    testa_divisao(0)
except ZeroDivisionError as E:
    print("Erro de divisão por zero")
except Exception as E:
    print("Tratamento genérico")
    
print("Programa encerrado")

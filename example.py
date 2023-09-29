# print("Olá mundo")

# print("Olá mundo"))

# print "Olá mundo"

# if True:
# print("Olá mundo")

# if True:
#  print("Olá mundo")

# frase = "Olá mundo"
# print(frase.ola)

# frase = "Olá mundo"
# print(frase)

def dividir(dividendo, divisor):
    # print(divisor.resultado)
    return dividendo / divisor


def testa_divisao(divisor):
    try:
        # teste = 'teste'
        # teste.ola()
        resultado = dividir(10, divisor)
        print(f"O resultado da divisao de 10 por {divisor} é {resultado}")
    except ZeroDivisionError:
        print("Erro de divisão por zero tratado")
    # except AttributeError:
    #     print("Erro de atributo tratado")

# testa_divisao(2)
try:
    testa_divisao(0)
except AttributeError:
    print("Erro de atributo tratado")
    
print("Programa encerrado")

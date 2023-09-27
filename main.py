from pprint import pprint
class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        
cliente = Cliente('Jhon Doe', '123.456.789-00', 'Desenvolvedor')
print(cliente.nome)
print(cliente.cpf)
print(cliente.profissao)

print(cliente.__dict__)
pprint(cliente.__dict__, width=40)

cliente.idade = 20
print(cliente.idade)
print(cliente.__dict__)
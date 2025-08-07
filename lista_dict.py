'''# Criando uma lista de frutas
frutas = ["maçã", "banana", "laranja"]

# Adicionando uma fruta
frutas.append("uva")
print("Lista após adicionar uva:", frutas)

# Removendo uma fruta
frutas.remove("banana")
print("Lista após remover banana:", frutas)

# Acessando o segundo item (índice 1)
print("Fruta na posição 2:", frutas[1])


# Criando uma tupla de cores
cores = ("vermelho", "azul", "verde")

# Tentando acessar um elemento
print("Primeira cor:", cores[0])

# Tentando modificar (isso vai causar um erro)
# cores[0] = "amarelo"  # Descomente para ver o erro

# Convertendo para uma lista se precisar alterar
cores_lista = list(cores)
cores_lista.append("amarelo")
print("Cores após converter para lista e adicionar amarelo:", cores_lista)


# Criando um dicionário com informações de uma pessoa
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando valores usando a chave
print("Nome:", pessoa["nome"])

# Modificando a idade
pessoa["idade"] = 31
print("Idade após modificação:", pessoa["idade"])

# Adicionando uma nova chave (profissão)
pessoa["profissao"] = "Engenheiro"
print("Dicionário após adicionar profissão:", pessoa)
'''

'''frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]

for fruta in frutas:
    print(fruta)'''

'''num = [2,2,2,4,4,5,5,5,8,9]

freq_num = []

for numero in num:
    if numero not in freq_num:
        freq_num.append(numero)
    
for numero in freq_num:
    contagem = num.count(numero)
    print(f"{numero} aparece {contagem} {'vez' if contagem == 1 else 'vezes'}")'''

'''alunos = [("Maria", 8.5), ("Pedro", 7.2), ("Ana", 9.0), ("João", 6.8)]

ordem = sorted(alunos, key=lambda aluno: aluno[1])

print(ordem)'''

dicionario = {'m1': {'m2': 'Olá Mundo'}}

'''chaves = dicionario.keys()
print(chaves)'''

"""print(dicionario['m1'])"""

dicionario2 = dicionario['m1']['m2']
print(dicionario2)
    
mensagem = dicionario.get('m1')
print(mensagem)

hello = mensagem.get('m2')
print(hello)
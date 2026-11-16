#1 Contagem Regressiva
"""
Solicite um número inteiro ao usuário.

Utilizando while, apresente uma contagem regressiva desse número até 0.

Exemplo:

Digite um número: 5

5
4
3
2
1
0
"""
"""
numero = int(input("Digite um número: "))

contador = numero

while contador  >= 0:
    print(contador)
    contador -= 1
"""
#2  Validação de Preço
"""
Solicite ao usuário o preço de um produto.

Enquanto o valor informado for menor ou igual a 0, o programa deverá solicitar o preço novamente.

Quando um valor válido for informado, apresente:

Produto cadastrado com sucesso.
"""
"""
preco = float(input("Digite o preço do produto: R$ "))

while preco <= 0:

    print("Digite um valor maior que zero.")
    preco = float(input("Digite o preço do produto: R$ "))

print("Produto cadastrado com sucesso")
"""
#3 Lista de Jogos
"""
Crie inicialmente a seguinte lista:

jogos = [
    "Minecraft",
    "Terraria",
    "Stardew Valley"
]
Solicite ao usuário o nome de mais dois jogos e adicione-os à lista.

Depois apresente:

A lista completa;
A quantidade total de jogos;
O primeiro jogo;
O último jogo.
"""
"""
jogos = [
    "Minecraft",
    "Terraria",
    "Stardew Valley"
]
jogo1 = input("Digite o nome de 1 jogo? ")
jogo2 = input("Digite o nome de outro jogo? ")
jogos.append(jogo1)
jogos.append(jogo2)
print(jogos)
quantidade = len(jogos)
print(quantidade)
print(jogos[0])
print(jogos[-1])
"""
# 4 Controle de Estoque
"""
Crie uma lista vazia:

produtos = []
Permita que o usuário cadastre produtos até digitar:

fim
Quando o cadastro terminar, apresente todos os produtos e a quantidade total cadastrada.
"""
"""
produtos = []

while True:

    produto = input("Digite o nome do produto ou 'fim': ")

    if produto == "fim":
        break

    produtos.append(produto)
print(produtos)    
"""
#5 Estatísticas de Notas
"""
Utilize a seguinte lista:

notas = [7.5, 8.0, 5.5, 9.0, 6.5, 10.0]
O programa deverá apresentar:

Quantidade de notas;
Soma das notas;
Média da turma;
Maior nota;
Menor nota.
Utilize:

len()
sum()
min()
max()
"""
"""
notas = [7.5, 8.0, 5.5, 9.0, 6.5, 10.0]

print("Soma:", sum(notas))
print("Média:", sum(notas) / len(notas))
print("Maior nota:", max(notas))
print("Menor nota:", min(notas))
"""
6# Busca em Lista
"""
Crie a seguinte lista:

usuarios = [
    "admin",
    "maria",
    "joao",
    "pedro"
]
Solicite um nome de usuário.

Utilizando while, percorra a lista procurando pelo nome informado.

O programa deverá apresentar:

Usuário encontrado.
ou:

Usuário não encontrado.
"""

"""
usuarios = [
    "admin",
    "maria",
    "joao",
    "pedro"
]



while True:

    usuario = input("Usuário: ")

    if usuario in usuarios:
        print("Usuário encontrado")
        break

    elif usuario == "sair":
        break 
   
    else:
        print("Usuário não encontrado")
"""

# 7 Carrinho de Compras
"""
Crie duas listas:

produtos = []
precos = []
O programa deverá permitir que o usuário cadastre produtos e seus respectivos preços.

O cadastro deverá continuar até o usuário digitar:

sair
Ao final, apresente:

Quantidade de produtos cadastrados;
Valor total da compra;
Produto mais barato;
Produto mais caro.
Dica: os índices das duas listas representam o mesmo produto.

Exemplo:

produtos = ["Mouse", "Teclado", "Monitor"]
precos = [80, 150, 900]
O índice 0 representa:

Mouse → R$ 80   
"""
"""
produtos = []
precos = []  

while True:

    produto = input("Digite o nome do produto ou 'fim': ")
    
    if produto == "fim":
        break
    
    preço = float(input("Digite o preço do produto:R$ "))
    
    produtos.append(produto)

    precos.append(preço)    
    
    print(produtos) 
    print(precos) 

    quantidade = len(produtos)
    total = sum(precos)
    menor = min(precos)
    maior = max(precos)
    
    print(f"Quantidade de produtos cadastrados: {quantidade}")
    print(f"Valor total da compra:R$ {total}")
    print(f"Produto mais barato: {menor}")
    print(f"Produto mais caro: {maior}")                
"""
#8 Sistema de Tarefas
"""
Desenvolva um programa com o seguinte menu:

1 - Adicionar tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Mostrar quantidade de tarefas
0 - Sair
As tarefas devem ser armazenadas em uma lista.

Exemplo:

1 - Adicionar tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Mostrar quantidade de tarefas
0 - Sair

Escolha uma opção: 1

Digite a tarefa: Estudar Python

Tarefa adicionada com sucesso.
O menu deve continuar aparecendo enquanto o usuário não escolher 0.

Utilize:

while True;
break;
if/elif;
Lista;
append();
remove() ou pop();
len().
"""
tarefas = []

while True:

    print("""
        1 - Adicionar tarefa
        2 - Listar tarefas
        3 - Remover tarefa
        4 - Mostrar quantidade de tarefas
        0 - Sair    
    """)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        break
    elif opcao == 1:
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
    elif opcao == 2:
        for t in tarefas:
            print(t)
    elif opcao == 3:
        tarefa = input("Digite a tarefa: ")
        tarefas.remove(tarefa)
    elif opcao == 4:
        quantidade = len(tarefas)
        print(quantidade)

    

   
      
    
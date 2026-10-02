import numpy as np
import pandas as pd
vendas = [1200, 1800, 1500, 2300]
print("Vendas:", vendas)

vendas[0]
print("Primeira venda:", vendas[0])
vendas[1]
print("Segunda venda:", vendas[1])
vendas[0] = 2000
print("Vendas atualizadas:", vendas)
print([0], [2])

# TUPLAS

coordenadas = (-7.12, -34.86)
print(coordenadas)
print(coordenadas[0])
print(type(coordenadas))
for coordenada in coordenadas:
    print(coordenadas)

# lista
preco = [100, 200, 150, 300, 400]
print(preco)


vendas2 = np.array([1000, 1500, 1200, 1800, 2000])
print(vendas2)
print(type(vendas2))
print(vendas2 * 2)

quantidades = np.array([100, 200, 300, 400, 500])
print(quantidades)

faturamento = np.array([vendas2 * quantidades])
print(faturamento)


vendas3 = np.array([
    [1, 2, 3],
    [4, 5, 6]
    ])
print(vendas3)

exames = np.array([1200, 1300, 500])
print(exames)
print(exames.sum())
for exame in exames:
    print(exame)


#dicionario

tabela = {

"Alface": 0.45,
"Batata": 1.20,
"Tomate": 2.30,
"Feijão": 1.50 
}
print(tabela)

tabela["Tomate"] = 2.50
print(tabela["Tomate"])
tabela["Cebola"] = 1.20
print(tabela)
tabela.values()

estoque: dict[str, dict[str, float | int]] = {
    "tomate": {"quantidade": 1000, "preco": 2.30},
    "alface": {"quantidade": 500, "preco": 0.45},
    "batata": {"quantidade": 2001, "preco": 1.20},
    "feijão": {"quantidade": 100, "preco": 1.50},
}
print(estoque)

for chave, valor in estoque.items():
    print(chave, valor)
####

df = pd.DataFrame.from_dict(estoque, orient="index")

print(df)

receita: list[float] = []

for quantidade, preco in zip(df["quantidade"], df["preco"]):
    receita.append(float(quantidade) * float(preco))
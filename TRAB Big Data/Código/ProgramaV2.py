import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Lista de anos
anos = list(range(2015, 2025))

# Lista de médias 
medias = []

consulta = 0

while consulta not in [1, 2, 3, 4]:
 print('Escolha um tipo de variavel para analizar:\n [1]Computadores \n [2]Alimentação \n [3]Laboratório \n [4]Sair')
 consulta = int(input("Sua opção: "))

 if (consulta == 1):
    escolha = 'QT_DESKTOP_ALUNO'

 elif (consulta == 2):
    escolha = 'IN_ALIMENTACAO'    

 elif (consulta == 3):
    escolha = 'IN_LABORATORIO_CIENCIAS' 

 elif (consulta == 4):
    print('Programa encerrado')
    sys.exit()   
 else:
   print("\nDigite uma opção válida") 
   input()

# Loop para gerar médias
for ano in anos:
    arquivo = f'Escolas Niteroi({ano}).xlsx'
    df = pd.read_excel(arquivo)
    soma = df[escolha].sum()
    quantidade = df[escolha].count()
    media = soma / quantidade if quantidade != 0 else 0
    medias.append(media)

# Dados do modelo
X = np.array(anos).reshape(-1, 1)
Y = np.array(medias)

# Regressão linear
modelo = LinearRegression()
modelo.fit(X, Y)

# Previsões
y_pred = modelo.predict(X)

# Exibir os coeficientes
print(f'Coeficiente angular (inclinação): {modelo.coef_[0]:.2f}')
print(f'Coeficiente linear (intercepto): {modelo.intercept_:.2f}')

# Criar uma figura com 2 subgráficos
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Subgráfico 1: Regressão Linear
axs[0].scatter(X, Y, color='blue', label='Média')
axs[0].plot(X, y_pred, color='red', label='Linha de regressão')
axs[0].set_title('Regressão Linear Simples')
axs[0].set_xlabel('Ano')
axs[0].set_ylabel('Média por aluno')
axs[0].legend()
axs[0].grid(True)

# Subgráfico 2: Distribuição de Frequência (Histograma)
axs[1].hist(Y, bins=5, color='darkblue', edgecolor='black')
axs[1].set_title('Distribuição de Frequência')
axs[1].set_xlabel('Média')
axs[1].set_ylabel('Frequência')
axs[1].grid(True)

plt.tight_layout()
plt.show()
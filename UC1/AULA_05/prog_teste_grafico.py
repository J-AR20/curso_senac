import matplotlib.pyplot as plt
import numpy as np

# Dados fictícios para ilustrar o exemplo
idades = np.arange(0, 101, 10)  # Idades de 0 a 100, em intervalos de 10 anos
populacao_masculina = np.array([500000, 600000, 700000, 800000, 900000, 800000, 700000, 600000, 500000, 400000])
populacao_feminina = np.array([450000, 550000, 650000, 750000, 850000, 750000, 650000, 550000, 450000, 350000])

# Criar a pirâmide etária
fig, ax = plt.subplots()

# Homens à esquerda, mulheres à direita
ax.barh(idades, populacao_masculina, height=8, color='blue', label='Masculino')
ax.barh(idades, -populacao_feminina, height=8, color='pink', label='Feminino')

ax.set_title('Pirâmide Etária - Rio de Janeiro (Censo 2010)')
ax.set_xlabel('População')
ax.set_ylabel('Idade')
ax.legend()

plt.show()

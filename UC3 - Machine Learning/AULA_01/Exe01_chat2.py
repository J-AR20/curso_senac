import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregamento dos dados
df_base = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='ISO-8859-1')

# Preprocessamento da base
df_crimes_correlatos = df_base[['ano', 'ameaca', 'lesao_corp_dolosa', 'roubo_celular', 'roubo_em_coletivo']].query("2018 <= ano <= 2023")

# Cálculo dos índices de correlação
crimes_sumarizados_por_ano = df_crimes_correlatos.groupby('ano').agg({
    'ameaca': 'sum', 
    'lesao_corp_dolosa': 'sum',
    'roubo_celular': 'sum',
    'roubo_em_coletivo': 'sum'
}).rename(columns={'ameaca': 'ameaca_sum', 'lesao_corp_dolosa': 'lesao_corp_dolosa_sum', 'roubo_celular': 'roubo_celular_sum', 'roubo_em_coletivo': 'roubo_em_coletivo_sum'}).reset_index()

corr_ameaca_lesao = crimes_sumarizados_por_ano['ameaca_sum'].corr(crimes_sumarizados_por_ano['lesao_corp_dolosa_sum'])
corr_roubCel_roubColetivo = crimes_sumarizados_por_ano['roubo_celular_sum'].corr(crimes_sumarizados_por_ano['roubo_em_coletivo_sum'])

# Visualização de dados
plt.figure(figsize=(18, 10))  # Ajuste no tamanho da figura para um layout lado a lado

# Gráfico 1 - Ameaça vs Lesão Corporal Dolosa
plt.subplot(1, 2, 1)
sns.regplot(x='ameaca', y='lesao_corp_dolosa', data=df_crimes_correlatos, color='orange')
plt.title('Correlação entre ameaça e lesão corporal dolosa')
plt.xlabel('Qt. ameaça')
plt.ylabel('Qt. lesão corporal dolosa')

# Gráfico 2 - Roubo de Celular vs Roubo em Coletivo
plt.subplot(1, 2, 2)
sns.regplot(x='roubo_celular', y='roubo_em_coletivo', data=df_crimes_correlatos)
plt.title('Correlação entre roubo de celular e roubo em coletivo')
plt.xlabel('Qt. roubo de celular')
plt.ylabel('Qt. roubo em coletivos')

# Adiciona os textos descritivos abaixo dos gráficos na posição indicada pelas setas
plt.figtext(0.25, 0.211, f'Correlação: {corr_ameaca_lesao:.4f} --> relação positiva muito forte entre ameaça e lesão corporal dolosa.', ha='center', fontsize=9)
plt.figtext(0.75, 0.211, f'Correlação: {corr_roubCel_roubColetivo:.4f} --> forte associação positiva entre roubos de celular e roubos em coletivo.', ha='center', fontsize=9)

# Ajuste do layout para evitar sobreposições e garantir que o título e a fonte dos dados sejam visíveis
plt.tight_layout(rect=[0, 0.15, 1, 0.95])  # Ajuste no retângulo para acomodar os textos descritivos

# Adicionando fonte dos dados na parte inferior central do gráfico
plt.figtext(0.5, 0.01, 'Fonte: Instituto de Segurança Pública do estado do Rio de Janeiro', horizontalalignment='center', fontsize=9)

plt.show()





'''Desenvolver um dashboard visualmente intuitivo para análise de dados dos roubos e recuperações de veículos,
cujo objetivo principal é permitir a análise e o monitoramento eficaz das ocorrências de roubo 
e recuperação de veículos, facilitando a tomada de decisões estratégicas e operacionais por parte dos gestores

Requisitos da análise:
• Utilizar os dados de: https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv
• Garantir que a análise esteja somente entre os anos de 2018 e 2023
• Apresentar a distribuição anual de roubos e recuperações de veículos (conforme o esboço)
• Apresentar tabelas com a média e a variação anual dos casos de roubo e recuperação de veículos (conforme esboço).

Entregas:
• Salvar o algoritmo com o seu nome completo e realizar o upload na pasta “ESTUDO DE CASO FINAL”, do drive da formação.
• Elaborar um breve relatório sobre suas observações acerca dos dados, para me auxiliar na análise, salvar com o seu 
nome completo e realizar o upload na pasta “ESTUDO DE CASO FINAL”, do drive da formação.'''

# 1) Importação das bibliotecas necessárias ao desenvolvimento da entrega:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2) Carregamento dos dados

df_base = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='ISO-8859-1')

# 3) Rotinas de preprocessamento da base
# 3.1) Descobrindo os nomes das colunas da base de dados

nomes_colunas = df_base.columns
print(nomes_colunas)

# Index(['cisp', 'mes', 'ano', 'mes_ano', 'aisp', 'risp', 'munic', 'mcirc',
#        'regiao', 'hom_doloso', 'lesao_corp_morte', 'latrocinio', 'cvli',
#        'hom_por_interv_policial', 'letalidade_violenta', 'tentat_hom',
#        'lesao_corp_dolosa', 'estupro', 'hom_culposo', 'lesao_corp_culposa',
#        'roubo_transeunte', 'roubo_celular', 'roubo_em_coletivo', 'roubo_rua',
#        'roubo_veiculo', 'roubo_carga', 'roubo_comercio', 'roubo_residencia',
#        'roubo_banco', 'roubo_cx_eletronico', 'roubo_conducao_saque',
#        'roubo_apos_saque', 'roubo_bicicleta', 'outros_roubos', 'total_roubos',
#        'furto_veiculos', 'furto_transeunte', 'furto_coletivo', 'furto_celular',
#        'furto_bicicleta', 'outros_furtos', 'total_furtos', 'sequestro',
#        'extorsao', 'sequestro_relampago', 'estelionato', 'apreensao_drogas',
#        'posse_drogas', 'trafico_drogas', 'apreensao_drogas_sem_autor',
#        'recuperacao_veiculos', 'apf', 'aaapai', 'cmp', 'cmba', 'ameaca',
#        'pessoas_desaparecidas', 'encontro_cadaver', 'encontro_ossada',
#        'pol_militares_mortos_serv', 'pol_civis_mortos_serv',
#        'registro_ocorrencias', 'fase'],
#       dtype='object')

# A partir dessa análise exploratória da base identifiquei os nomes das seguintes séries de dados de interesse:
# 'roubo_veiculo', 'recuperacao_veiculos', 'ano'

# 3.2) Criando um df auxiliar APENAS com o recorte temporal e séries de dados necessárias ao desenvolvimento da entrega

df_carros_surrupiados = df_base[['recuperacao_veiculos', 'roubo_veiculo', 'ano']].query("2018 <= ano <= 2023")
print(df_carros_surrupiados)

# 4) Calculo das médias e desvio padrão exigidos no painel de dados

medias_desvios = df_carros_surrupiados.groupby('ano').agg({'recuperacao_veiculos': ['mean', 'std'], 'roubo_veiculo': ['mean', 'std']})
medias_desvios.columns = ['recuperacao_veiculos_media', 'recuperacao_veiculos_desvio_padrao', 'roubo_veiculo_media', 'roubo_veiculo_desvio_padrao']
medias_desvios.reset_index(inplace=True)
medias_desvios['ano'] = medias_desvios['ano'].astype(int).astype(str)  # Convertendo o ano para texto

# 5) Visualização de dados
# 5.1) Iniciando a figura, plano de fundo para a visualização dos dados

plt.figure(figsize=(15, 10))

# 5.2) Atribuição de um título geral para o painel de dados

plt.suptitle('Análise dos dados de Roubo e Recuperação de veículos')

# 5.3) Gráfico 1 - Roubo de veículos

plt.subplot(2, 2, 1)  # Define o primeiro subplot na grade 2x2
sns.boxplot(data=df_carros_surrupiados, x='ano', y='roubo_veiculo')
plt.title('Distribuição dos Roubos de veículo por Ano')
plt.xlabel('Ano')  # Rótulo do eixo X
plt.ylabel('Nº de veículos roubados')  # Rótulo do eixo Y

# 5.4) Gráfico 2 - Recuperacao de veículos

plt.subplot(2, 2, 2)  # Define o segundo subplot na grade 2x2
sns.boxplot(data=df_carros_surrupiados, x='ano', y='recuperacao_veiculos')
plt.title('Distribuição das Recuperações de veículo por Ano')
plt.xlabel('Ano')  # Rótulo do eixo X
plt.ylabel('Nº de veículos recuperados')  # Rótulo do eixo Y

# 5.5) Tabelas de médias e desvios padrão - Roubo de Veículos

plt.subplot(2, 2, 3)  # Define o quarto subplot na grade 2x2
plt.axis('off')  # Desativa os eixos para este subplot
plt.table(cellText=medias_desvios[['ano', 'roubo_veiculo_media', 'roubo_veiculo_desvio_padrao']].round({'roubo_veiculo_media': 2, 'roubo_veiculo_desvio_padrao': 4}).values,
          colLabels=['Ano', 'Média', 'Desvio Padrão'], loc='center', cellLoc='center')
#plt.title('Roubos de veículo: Média e Desvio Padrão por Ano') # abandonei essa métrica porque o título estava ficando longe da tabela
plt.text(0.5, 0.95, 'Roubos de veículo: Média e Desvio Padrão por Ano', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12)

# 5.6) Tabelas de médias e desvios padrão - Recuperação de veículos

plt.subplot(2, 2, 4)  # Define o terceiro subplot na grade 2x2
plt.axis('off')  # Desativa os eixos para este subplot
plt.table(cellText=medias_desvios[['ano', 'recuperacao_veiculos_media', 'recuperacao_veiculos_desvio_padrao']].round({'recuperacao_veiculos_media': 2, 'recuperacao_veiculos_desvio_padrao': 4}).values,
          colLabels=['Ano', 'Média', 'Desvio Padrão'], loc='center', cellLoc='center')
#plt.title('Recuperações de veículo: Média e Desvio Padrão por Ano')
plt.text(0.5, 0.95, 'Recuperação de Veículos: Média e Desvio Padrão por Ano', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12)


# 5.7) Adicionando texto da fonte dos dados

plt.figtext(0.95, 0.01, 'Fonte: Instituto de Segurança Pública do estado do Rio de Janeiro', horizontalalignment='right')


# 5.8) Ajustando o layout e exibindo o apresentando o painel de dados

plt.tight_layout(rect=[0, 0, 1, 0.95])  # Ajusta o layout para deixar espaço para o título principal
plt.show()



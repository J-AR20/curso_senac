# 1) Importação das bibliotecas necessárias ao desenvolvimento da entrega:
# importando as bibliotecas necessarias para a atividade
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2) Carregamento dos dados
# caregando os dados
df_base = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='ISO-8859-1')
print(df_base.head(10))

# 3) Rotinas de preprocessamento da base
# 3.1) Descobrindo os nomes das colunas da base de dadosn
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
# 'ano', 'ameaca', 'lesao_corp_dolosa', 'roubo_celular', 'roubo_em_coletivo'

# 3.2) Criando um df auxiliar APENAS com o recorte temporal e séries de dados necessárias ao desenvolvimento da entrega

df_crimes_correlatos = df_base[['ano', 
                                'ameaca', 
                                'lesao_corp_dolosa', 
                                'roubo_celular', 
                                'roubo_em_coletivo']].query("2018 <= ano <= 2023")
print(df_crimes_correlatos.head(10))


# 4) Calculo dos índices de correlação
# 4.1) Criando uma tabela dos crimes sumarizados e agregados por ano
crimes_sumarizados_por_ano = df_crimes_correlatos.groupby('ano').agg({
    'ameaca': ['sum'], 
    'lesao_corp_dolosa': ['sum'],
    'roubo_celular': ['sum'],
    'roubo_em_coletivo': ['sum']
})

# 4.2) Renomeando as colunas para remover o MultiIndex
crimes_sumarizados_por_ano.columns = [
    'ameaca_sum', 
    'lesao_corp_dolosa_sum',
    'roubo_celular_sum',
    'roubo_em_coletivo_sum'
]

# Resetando o índice para transformar o índice 'ano' em uma coluna
crimes_sumarizados_por_ano.reset_index(inplace=True)

# Neste código, após agrupar e somar os valores por 'ano', nós renomeamos as colunas 
# para remover o MultiIndex resultante da operação agg. Então, usamos reset_index() 
# para fazer 'ano' voltar a ser uma coluna regular do DataFrame. Finalmente, calculamos a 
# correlação entre 'ameaca_sum' e 'lesao_corp_dolosa_sum'. Isso deve estar de acordo 
# com o padrão que você está tentando seguir.

# 4.3) Agora, podemos calcular a correlação entre as séries de interesse
# 4.3.1) Correlacao entre Ameaça e Lesão Corporal Dolosa
corr_ameaca_lesao = crimes_sumarizados_por_ano['ameaca_sum'].corr(crimes_sumarizados_por_ano['lesao_corp_dolosa_sum'])
print(corr_ameaca_lesao)
## 0.887368961954295
## Correlação positiva muito forte

# 4.3.2) Correlacao entre Roube de Celular e Roubo de Coletivo
corr_roubCel_roubColetivo = crimes_sumarizados_por_ano['roubo_celular_sum'].corr(crimes_sumarizados_por_ano['roubo_em_coletivo_sum'])
print(corr_roubCel_roubColetivo)
## 0.9151887694653777
## Correlação positiva muito forte


# 5) Visualização de dados
# 5.1) Iniciando a figura, plano de fundo para a visualização dos dados
plt.figure(figsize=(14, 7))  # Ajusta o tamanho para uma melhor proporção

# Gráfico 1 - Ameaça vs Lesão Corporal Dolosa
plt.subplot(1, 2, 1)
sns.regplot(x='ameaca', y='lesao_corp_dolosa', data=df_crimes_correlatos, color='orange')
plt.title('Correlação entre ameaça e lesão corporal dolosa')
plt.xlabel('Qt. ameaça')
plt.ylabel('Qt. lesão corporal dolosa')
plt.figtext(0.25, -0.1, f'A correlação de {corr_ameaca_lesao:.4f} indica uma relação positiva muito forte entre os crimes de ameaça e lesão corporal dolosa.', ha='center', fontsize=9, transform=plt.gcf().transFigure)

# Gráfico 2 - Roubo de Celular vs Roubo em Coletivo
plt.subplot(1, 2, 2)
sns.regplot(x='roubo_celular', y='roubo_em_coletivo', data=df_crimes_correlatos)
plt.title('Correlação entre roubo de celular e roubo em coletivo')
plt.xlabel('Qt. roubo de celular')
plt.ylabel('Qt. roubo em coletivos')
plt.figtext(0.75, -0.1, f'A correlação de {corr_roubCel_roubColetivo:.4f} sugere uma forte associação positiva entre os roubos de celular e em coletivos, indicando que tendem a aumentar ou diminuir juntos.', ha='center', fontsize=9, transform=plt.gcf().transFigure)

# Ajusta o layout para evitar sobreposições e garantir que o título e a fonte dos dados sejam visíveis
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Adicionando fonte dos dados na parte inferior do gráfico
plt.figtext(0.95, 0.001, 'Fonte: Instituto de Segurança Pública do estado do Rio de Janeiro', horizontalalignment='right', fontsize=9)

plt.show()
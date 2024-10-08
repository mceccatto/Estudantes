import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# 1. Carregar e Limpar os Dados
file_path = 'StudentsPerformance.csv'
data = pd.read_csv(file_path)
data_cleaned = data.copy()
data_cleaned['gender'] = data_cleaned['gender'].map({'female': 0, 'male': 1})
ethnicity_mapping = {f'group {chr(65 + i)}': i for i in range(5)}
data_cleaned['race/ethnicity'] = data_cleaned['race/ethnicity'].map(ethnicity_mapping)
education_mapping = {
    "some high school": 0,
    "high school": 1,
    "some college": 2,
    "associate's degree": 3,
    "bachelor's degree": 4,
    "master's degree": 5
}
data_cleaned['parental level of education'] = data_cleaned['parental level of education'].map(education_mapping)
data_cleaned['lunch'] = data_cleaned['lunch'].map({'standard': 1, 'free/reduced': 0})
data_cleaned['test preparation course'] = data_cleaned['test preparation course'].map({'completed': 1, 'none': 0})

# 2. Análise Exploratória
sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
sns.boxplot(x='test preparation course', y='math score', data=data_cleaned, ax=axes[0])
axes[0].set_title('Impacto da Preparação no Desempenho em Matemática')
axes[0].set_xticklabels(['None', 'Completed'])
sns.boxplot(x='test preparation course', y='reading score', data=data_cleaned, ax=axes[1])
axes[1].set_title('Impacto da Preparação no Desempenho em Leitura')
axes[1].set_xticklabels(['None', 'Completed'])
sns.boxplot(x='test preparation course', y='writing score', data=data_cleaned, ax=axes[2])
axes[2].set_title('Impacto da Preparação no Desempenho em Escrita')
axes[2].set_xticklabels(['None', 'Completed'])
plt.tight_layout()
plt.show()

# 3. Heatmap de Correlação
plt.figure(figsize=(10, 6))
correlation_matrix = data_cleaned.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlação entre Notas e Fatores Demográficos")
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')
plt.tight_layout()
plt.show()

# 4. Geração dos gráficos dinâmicos 2D e 3D
data_cleaned2 = data.copy()
data_cleaned2['gender'] = data_cleaned2['gender'].map({'female': 'Female', 'male': 'Male'})
ethnicity_mapping = {f'group {chr(65 + i)}': f'Group {chr(65 + i)}' for i in range(5)}
data_cleaned2['race/ethnicity'] = data_cleaned2['race/ethnicity'].map(ethnicity_mapping)
data_cleaned2['test preparation course'] = data_cleaned2['test preparation course'].map({'completed': 'Completed', 'none': 'None'})
fig2 = px.scatter(
    data_cleaned2,
    x='math score',
    y='reading score',
    color='gender',
    symbol='test preparation course',
    facet_col='race/ethnicity',
    hover_data=['writing score'],
    title='Desempenho de Estudantes por Gênero, Grupo Étnico e Preparação para o Exame'
)
fig2.show()
fig3 = px.scatter_3d(
    data_cleaned2,
    x='math score',
    y='reading score',
    z='writing score',
    color='gender',
    symbol='test preparation course',
    hover_name='race/ethnicity',
    title='Desempenho de Estudantes (Gráfico 3D)'
)
fig3.show()